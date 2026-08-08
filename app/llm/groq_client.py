"""
Groq Client

Handles communication with the Groq API.
"""

import os

from dotenv import load_dotenv
from groq import Groq

from app.core.config import config

# Load environment variables from a .env file so secrets like GROQ_API_KEY are available.
load_dotenv()


class GroqClient:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, prompt: str) -> str:
        """
        Generate an answer from the LLM.
        """

        response = self.client.chat.completions.create(
            model=config["llm"]["model_name"],
            temperature=config["llm"]["temperature"],
            max_tokens=config["llm"]["max_tokens"],
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content