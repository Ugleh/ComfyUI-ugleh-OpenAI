from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv
import openai


@dataclass(frozen=True)
class OpenAIService:
    """Tiny wrapper around the OpenAI SDK.

    Centralizes env loading and client construction so nodes can stay focused.
    """

    api_key_env_var: str = "OPENAI_API_KEY"

    def _get_api_key(self) -> str:
        # Allow either .env or environment variables.
        load_dotenv()
        api_key = os.getenv(self.api_key_env_var)
        if not api_key:
            raise ValueError(
                f"{self.api_key_env_var} is not set. Add it to your .env file or environment variables."
            )
        return api_key

    def create_client(self) -> openai.OpenAI:
        return openai.OpenAI(api_key=self._get_api_key())

    def responses_text(
        self,
        *,
        model: str,
        reasoning_effort: str,
        instructions: str,
        input_text: str,
        max_output_tokens: int,
    ) -> str:
        client = self.create_client()
        response = client.responses.create(
            model=model,
            reasoning={"effort": reasoning_effort},
            instructions=instructions,
            input=input_text,
            max_output_tokens=max_output_tokens,
        )

        output_text = getattr(response, "output_text", None)
        if not output_text:
            raise ValueError("No output_text in response")

        return output_text
