# Adaptive-tax computational companion

This folder contains Yichen Shen's deterministic Python reconstruction of the eight-round taxpayer-authority game used in the PS1 proposal. It replaces the class template's unrelated LLM strategic-reasoning example.

## What each artifact does

- `src/games.py`: source of truth for the payoff table, bounded trust update, event log, three preset paths, and one-shot benchmark.
- `tests/test_models.py`: boundary, invalid-input, equilibrium, event-log, and expected-output tests.
- `notebooks/adaptive_tax_game.ipynb`: self-contained notebook intended for Google Colab.
- `outputs/adaptive_tax_results.json`: saved deterministic results from a fresh local run.

## Reproduce locally

No third-party packages or API keys are required.

```bash
cd companion
python -m unittest discover -s tests
python -m src.run_validation
```

Expected preset results are taxpayer payoff / authority payoff / final trust:

- Transparent cooperation: `24 / 24 / 100`
- Opaque breakdown: `7 / 11 / 0`
- Mixed recovery: `23 / 19 / 90`

These are programmed demonstrations and implementation checks, not estimates of real taxpayer behavior.

## GitHub, Colab, and Hugging Face

- GitHub project: <https://github.com/cccc-0212/yichen-ps1-overleaf/tree/yichen_proposal>
- Colab notebook on `yichen_proposal`: <https://colab.research.google.com/github/cccc-0212/yichen-ps1-overleaf/blob/yichen_proposal/companion/notebooks/adaptive_tax_game.ipynb>
- Interactive Static Space: <https://huggingface.co/spaces/dku-comsci-econ206-2026/yichenshendemo>

The Python/Colab companion verifies the model. The Hugging Face Space provides the interactive learning interface. Neither replaces the other.
