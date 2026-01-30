"""ComfyUI node registry.

Keep this file small: it acts as a stable public entrypoint for ComfyUI,
while actual node implementations live in per-node modules.
"""

from .ugleh_openai.nodes.openai_responses_text import OpenAIResponsesText


NODE_CLASS_MAPPINGS = {
    "Ugleh.OpenAI.ResponsesText": OpenAIResponsesText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Ugleh.OpenAI.ResponsesText": "Ugleh OpenAI - Responses Text",
}
