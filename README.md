# ComfyUI-ugleh-OpenAI

Minimal OpenAI API nodes for ComfyUI.

This repo intentionally exposes *building-block* OpenAI APIs (not opinionated workflow helpers), so you can compose your own pipelines in ComfyUI.

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

### 1) Install

From your ComfyUI install:

- Put this folder in `ComfyUI/custom_nodes/ComfyUI-ugleh-OpenAI`
- Install dependencies:

`pip install -r requirements.txt`

### 2) API key

Set `OPENAI_API_KEY`.

Option A: `.env` in your ComfyUI root:
```
OPENAI_API_KEY=your_api_key_here
```

Option B: OS environment variable.

### 3) Restart ComfyUI

After restart, the node should appear under the `ugleh/openai` category.

## ComfyUI-Manager linking (for shared workflows)

When someone downloads a workflow that uses your nodes, ComfyUI-Manager can only offer an "Install Missing Custom Nodes" button if it can map the workflow's node `class_type` names (e.g. `Ugleh.OpenAI.ResponsesText`) to a known node pack (your GitHub repo or a Comfy Registry entry).

To make that work reliably:

1) **Keep your node keys stable**
	- The mapping keys in `NODE_CLASS_MAPPINGS` (the `class_type` stored in workflows) should remain stable across versions.

2) **Add a `node_list.json` (optional but recommended)**
	- This repo includes `node_list.json` so scanners can always detect your node names even if your code structure changes.

3) **Get indexed by ComfyUI-Manager / Registry**
	- Preferred: publish/register your node pack on the Comfy Registry (CNR): https://registry.comfy.org/
	- Legacy: submit a PR to ComfyUI-Manager adding your repo to their database (`custom-node-list.json`). Once merged, Manager can auto-suggest/install your repo when those nodes are missing.

Notes:
- ComfyUI-Manager now normalizes the install folder name based on the `name` field in `pyproject.toml` (so avoid relying on folder name for imports).

## Repo prep checklist

- Rename the folder to `ComfyUI-ugleh-OpenAI`
- Update this README with screenshots/examples if desired
- Keep MIT license + attribution if you started from another repo
- Create a GitHub repo and push

## License

MIT (see LICENSE)
