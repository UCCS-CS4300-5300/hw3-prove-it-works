# HW3 Starter — PeakPass

**Do not work directly in this shared starter repository.**

## Get the starter into your private course repository

1. Download this repository as a ZIP from GitHub.
2. Extract the ZIP on your computer.
3. In your existing private CS 4300/5300 repository, create an `hw3` directory.
4. Copy the **contents** of the extracted starter repository into your private repository's `hw3/` directory.
5. Commit that untouched starter baseline in your private repository **before making substantive changes**.
6. Do all HW3 work, commits, and pushes in your private course repository.

Your private repository should end up looking roughly like:

```text
your-private-repo/
├── hw1/
├── hw2/
└── hw3/
    ├── peakpass/
    ├── tests/
    ├── README.md
    ├── SPECIFICATION.md
    ├── TESTING_NOTES.md
    ├── pyproject.toml
    └── requirements.txt
```

The existing automated test suite passes. Your job is to decide how much confidence it deserves and improve the testing evidence where it matters.

## Setup

From inside your private repository's `hw3/` directory:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run tests

```bash
python -m pytest
```

## Coverage

```bash
python -m pytest --cov=peakpass --cov-branch --cov-report=term-missing
```

## Mutation testing

Use this after mutation testing is introduced in class:

```bash
mutmut run
mutmut results
```

## Code metrics

```bash
radon cc peakpass -s -a
radon mi peakpass -s
```

Read `SPECIFICATION.md` before changing tests. Keep important investigation decisions in `TESTING_NOTES.md`.
