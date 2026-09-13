# Transparent Adaptive Taxation under Limited Information

Yichen Shen's individual PS1 research proposal for COMSCI/ECON 206 Computational Microeconomics, Autumn 2026 Session 1.

The project studies an eight-round taxpayer-authority game in which the taxpayer chooses Comply or Avoid and the authority chooses Transparent or Opaque. It separates the one-shot Nash benchmark from trust-based and continuation-incentive explanations.

## Reproduce the computational checks

The Python model uses only the standard library:

```bash
cd companion
python -m unittest discover -s tests
python -m src.run_validation
```

The expected programmed outputs are:

| Path | Taxpayer payoff | Authority payoff | Final trust |
|---|---:|---:|---:|
| Transparent cooperation | 24 | 24 | 100 |
| Opaque breakdown | 7 | 11 | 0 |
| Mixed recovery | 23 | 19 | 90 |

These results verify implementation and event-log completeness; they are not evidence about real taxpayer behavior.

## Research artifacts

- [Google Colab notebook](https://colab.research.google.com/github/cccc-0212/yichen-ps1-overleaf/blob/yichen_proposal/companion/notebooks/adaptive_tax_game.ipynb)
- [Interactive Hugging Face game](https://huggingface.co/spaces/dku-comsci-econ206-2026/yichenshendemo)
- `main.tex`: ACM-format proposal source
- `figures/ps1_teaser.drawio`: editable Figure 1 master

## Template attribution

The Overleaf structure is adapted from the COMSCI/ECON 206 PS1 class template by Prof. Luyao Zhang: <https://github.com/sunshineluyao/ps1-overleaf-template>. ACM class and bibliography files retain their original notices.
