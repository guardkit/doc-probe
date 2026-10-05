Status: accepted — 5 October 2026, Rich (throwaway factory test project)

# doc-probe: technical decisions

- **Language:** Python 3.12, standard library only; no third-party runtime dependencies.
- **Layout:** one package, `src/doc_probe/`; tests in `tests/`, run with pytest.
- **Public API:** plain functions in `src/doc_probe/__init__.py`, each with type hints and a docstring.
- **The one check command:** `qa/run-tests.sh` (installs the test extra into the project's `.venv` and
  runs pytest). Exit code 0 means the work is done.
- **Skills:** none required.
