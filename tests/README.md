# Testing and author tools

All authoring checks, evaluation code, fixtures and research evidence live here.
Run commands from the repository root; no GitHub Actions workflows are installed.

| Directory or file | Purpose |
| --- | --- |
| [scripts/](scripts/) | Build, validation, capture and analysis commands |
| [unit/](unit/) | Unit and regression tests |
| [evals/](evals/README.md) | Test cases, frozen protocols, results and raw evidence |
| [sources/](sources/) | Source dossiers and maintenance evidence, not prompt modules |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Authoring and evidence-preservation conventions |
| `requirements-dev.txt` | Local author-tool dependencies |
| `requirements-simulation.txt` | Optional model-capture dependencies |

```sh
.venv/bin/python -m tests.scripts.build --write-quick-guide
.venv/bin/python -m tests.scripts.check
.venv/bin/python -m tests.scripts.evaluate validate
.venv/bin/python -m unittest discover -s tests/unit -t .
```

Use `tests.scripts.check --recount` after changing instruction bodies. Edit
`stop-the-slop/prompts/task.md` and the operating sections of the six
`stop-the-slop/` modules rather than editing `quick-guide.md` directly.
Writer-facing profiles are under [domains/profiles/](../domains/profiles/).

Evaluation runs and private runtime state stay in ignored `tests/evals/runs/`.
Published captures, hashes, protocols and results are historical evidence:
relocation must not change the captured text or pretend that old runs used
new instructions. See [the evaluation archive notes](evals/README.md#historical-paths).
