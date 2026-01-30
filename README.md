# ComfyUI-ugleh-OpenAI

Minimal OpenAI API nodes for ComfyUI.

## Nodes

### Ugleh OpenAI - Responses Text

Calls the OpenAI **Responses API**.

Inputs:
- `model`: choose an OpenAI model (includes GPT‑4o/4.1 and GPT‑5 family)
- `reasoning_effort`: `low` / `medium` / `high`
- `instructions`: multi-line text
- `input`: multi-line text
- `max_output_tokens`

Outputs:
- `text_out`

## Setup

### Installation and Usage

1. Navigate to ComfyUI/custom_nodes folder in the terminal or command prompt.
2. Clone the repo using the following command:
   `git clone https://github.com/Ugleh/ComfyUI-ugleh-OpenAI`
3. Go to `custom_nodes/ComfyUI-ugleh-OpenAI` and install dependencies by running `pip install -r requirements.txt`
4. Restart ComfyUI

## License

MIT (see LICENSE)
