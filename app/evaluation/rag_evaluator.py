"""
RAG Evaluation Runner

Runs the complete RAGForge pipeline against
a manually verified evaluation dataset.

The output contains:

- User question
- Ground-truth answer
- Generated answer
- Retrieved contexts

These results are then passed to Ragas.
"""

import json
from pathlib import Path

from app.citations.citation_builder import CitationBuilder
from app.core.config import config
from app.llm.groq_client import GroqClient
from app.prompts.prompt_builder import PromptBuilder
from app.reranking.reranking_pipeline import RerankingPipeline


class RAGEvaluator:
    """
    Runs RAGForge questions for evaluation.
    """

    def __init__(self):
        """
        Initialize the components required
        to run the RAG pipeline.
        """

        # Hybrid retrieval + RRF + re-ranking
        self.pipeline = RerankingPipeline()

        # LLM used to generate the final answer
        self.llm = GroqClient()

    def load_dataset(self) -> list[dict]:
        """
        Load the manually verified evaluation dataset.

        Returns:
            List of evaluation questions and
            their ground-truth answers.
        """

        # Get dataset path from config.yaml
        dataset_path = Path(
            config["evaluation"]["dataset_path"]
        )

        # Make sure the dataset exists
        if not dataset_path.exists():
            raise FileNotFoundError(
                f"Evaluation dataset not found: "
                f"{dataset_path}"
            )

        # Read JSON dataset
        with open(
            dataset_path,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    def run(self) -> list[dict]:
        """
        Run every question through RAGForge.

        Returns:
            A list containing:
            - question
            - ground_truth
            - answer
            - retrieved contexts
        """

        # Load evaluation questions
        dataset = self.load_dataset()

        records = []

        total = len(dataset)

        # Process every question
        for index, item in enumerate(
            dataset,
            start=1,
        ):

            question = item["question"]

            ground_truth = item["ground_truth"]

            print(
                f"[{index}/{total}] "
                f"Evaluating: {question}"
            )

            # ------------------------------------------
            # STEP 1
            # Retrieve and re-rank documents
            # ------------------------------------------

            results = self.pipeline.retrieve(
                question
            )

            # ------------------------------------------
            # STEP 2
            # Extract retrieved text
            #
            # Ragas needs the actual context that
            # was provided to the LLM.
            # ------------------------------------------

            contexts = [
                result["chunk"].text
                for result in results
            ]

            # ------------------------------------------
            # STEP 3
            # Generate citations
            # ------------------------------------------

            citations = CitationBuilder.build(
                results
            )

            # ------------------------------------------
            # STEP 4
            # Build grounded prompt
            # ------------------------------------------

            prompt = PromptBuilder.build(
                question=question,
                results=results,
                citations=citations,
            )

            # ------------------------------------------
            # STEP 5
            # Generate final RAG answer
            # ------------------------------------------

            answer = self.llm.generate(
                prompt
            )

            # ------------------------------------------
            # STEP 6
            # Store evaluation information
            # ------------------------------------------

            records.append(
                {
                    "question": question,
                    "ground_truth": ground_truth,
                    "answer": answer,
                    "contexts": contexts,
                }
            )

        return records