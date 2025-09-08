# DSPCT — Distributed Systems and Parallel Computing Technologies

This repository contains assignment code for the "Distributed Systems and Parallel Computing Technologies" course. The example assignment in this repo demonstrates simple image processing using multiple processes.

Project layout
- src/assignment_1/main.py — 1st assigment

Requirements
- Python >= 3.12 (see [pyproject.toml](pyproject.toml))
- Pillow (installed via Poetry)

Poetry setup
1. Install Poetry (if not installed):
   - pip: `python -m pip install --upgrade poetry`
   - see https://python-poetry.org/ for other install options
2. Install dependencies and create the virtual environment:
   - `poetry install`
3. Run the assignment script:
   - `poetry run python -m src.assignment_1.main`

