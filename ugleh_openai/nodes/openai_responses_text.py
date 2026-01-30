from __future__ import annotations

from ..constants import MODELS
from ..services.openai_service import OpenAIService


class OpenAIResponsesText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": (MODELS,),
                "reasoning_effort": (["low", "medium", "high"],),
                "instructions": (
                    "STRING",
                    {
                        "default": "You are a helpful assistant.",
                        "multiline": True,
                    },
                ),
                "input": (
                    "STRING",
                    {
                        "default": "",
                        "multiline": True,
                    },
                ),
                "max_output_tokens": ("INT", {"default": 300}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    CATEGORY = "ugleh/openai"
    FUNCTION = "respond"

    def __init__(self):
        self._service = OpenAIService()

    def respond(self, model, reasoning_effort, instructions, input, max_output_tokens):
        output_text = self._service.responses_text(
            model=model,
            reasoning_effort=reasoning_effort,
            instructions=instructions,
            input_text=input,
            max_output_tokens=max_output_tokens,
        )
        return (output_text,)
