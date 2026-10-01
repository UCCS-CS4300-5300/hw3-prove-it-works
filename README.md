# HW3 Starter — PeakPass

**Do not work directly in this shared starter repository.**

## Get the starter into your private course repository

1. Download this repository as a ZIP from GitHub.
2. Extract the ZIP on your computer.
3. In your existing private CS 4300/5300 repository, create an `hw3` directory.
4. Copy the **contents** of the extracted starter repository into your private repository's `hw3/` directory.
5. Commit that untouched starter baseline in your private repository **before making substantive changes**.
6. Do all HW3 work, commits, and pushes in your private course repository.

**Shared repository = where you GET HW3. Your private repository = where you DO and SUBMIT HW3.**

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
python -m pip install -r requirements.txt
```

If you prefer to use a virtual environment, you may do so, but it is not required in Codespaces.

## Tool quick reference

### Run the tests

```bash
python -m pytest
```

To see each test named individually:

```bash
python -m pytest -v
```

To run one particular test while investigating it:

```bash
python -m pytest tests/test_peakpass.py::test_name_here -v
```

Verbose mode is not a debugger; it simply gives you more detailed test-by-test output.

### Coverage

```bash
python -m pytest --cov=peakpass --cov-branch --cov-report=term-missing
```

The `Missing` information identifies lines or branches that were not exercised. Treat those as places to **investigate**, not automatic instructions to add tests.

Optional HTML view:

```bash
python -m pytest --cov=peakpass --cov-branch --cov-report=html
```

This creates `htmlcov/index.html`.

### Mutation testing

Use mutation testing after it is introduced in class:

```bash
python -m mutmut run
```

The easiest way to investigate the results is the interactive browser:

```bash
python -m mutmut browse
```

You can also list results in the terminal:

```bash
python -m mutmut results
```

To inspect one particular mutant:

```bash
python -m mutmut show <mutant-name>
```

In the run summary, **🎉 means a mutant was killed** (at least one test noticed the change) and **🙁 means a mutant survived** (the current suite stayed green).

**You are not expected to kill every surviving mutant.** Investigate survivors that represent meaningful behavioral changes according to `SPECIFICATION.md`. Ask what changed, whether it matters, and why the current tests did not notice it. A survivor may reveal a missing case, a weak assertion, an equivalent mutation, or a difference that does not justify additional testing.

### Cyclomatic complexity

```bash
python -m radon cc peakpass -s -a
```

The number in parentheses is Radon's cyclomatic-complexity score. The letter is its rank:

- A = 1–5
- B = 6–10
- C = 11–20
- D = 21–30
- E = 31–40
- F = 41+

A higher score is a reason to inspect the code more carefully, **not proof that the code is defective or must be refactored**. The `-s` option shows the numeric score and `-a` shows the overall average.

### Maintainability Index

```bash
python -m radon mi peakpass -s
```

Radon reports a numerical Maintainability Index and a classification:

- A = 20–100
- B = 10–19
- C = 0–9

The number is **not a percentage of maintainability**. Use it as a comparative/investigative signal rather than a quality grade.

## What to do with the tools

The tools are evidence, not a checklist and not a set of target scores. You do not need every tool to reveal a problem.

Ask:

- What question does this output help answer?
- What does it **not** tell me?
- Does it point to something worth investigating?
- Did the evidence change what I think about the test suite?

Read `SPECIFICATION.md` before changing tests. Keep the important decisions and discoveries from your investigation in `TESTING_NOTES.md`.
