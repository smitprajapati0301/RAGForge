"""
Ragas LLM Configuration

Creates the LLM used by Ragas for evaluation.

RAGForge normally uses the Groq Python client directly.
For Ragas, we use Groq's OpenAI-compatible API through
AsyncOpenAI so that Ragas can perform asynchronous
metric evaluation.
"""

import os

from dotenv import load_dotenv
from openai import AsyncOpenAI
from ragas.llms import llm_factory

from app.core.config import config


# Load environment variables from .env
load_dotenv()


def create_ragas_llm():
    """
    Create an asynchronous Ragas evaluator LLM.

    Groq provides an OpenAI-compatible API endpoint,
    allowing Ragas to use its Instructor-based LLM
    adapter.

    AsyncOpenAI is required because Ragas 0.4.3
    collection metrics use asynchronous evaluation.
    """

    # Get Groq API key from .env
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is not configured "
            "in the .env file."
        )

    # --------------------------------------------------
    # Create asynchronous OpenAI-compatible client
    # --------------------------------------------------
    #
    # The request is actually sent to Groq.
    #
    # OpenAI SDK
    #      ↓
    # Groq OpenAI-compatible API
    #
    # --------------------------------------------------

    client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

    # --------------------------------------------------
    # Create Ragas-compatible evaluator
    # --------------------------------------------------

    return llm_factory(
        model=config["llm"]["model_name"],
        provider="openai",
        client=client,

        # Use deterministic evaluation.
        temperature=0.0,

        # Reuse the configured token limit.
        max_tokens=config["llm"]["max_tokens"],
    )