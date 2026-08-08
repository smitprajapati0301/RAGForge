from app.llm.groq_client import GroqClient
from app.prompts.prompt_builder import PromptBuilder
from app.retrieval.retriever import Retriever


def main():

    retriever = Retriever()
    llm = GroqClient()

    while True:

        question = input("\nQuestion: ")

        if question.lower() == "exit":
            break

        results = retriever.retrieve(question)

        contexts = results["documents"][0]

        prompt = PromptBuilder.build(
            question,
            contexts,
        )

        answer = llm.generate(prompt)

        print("\nAnswer:\n")

        print(answer)

        print()


if __name__ == "__main__":
    main()