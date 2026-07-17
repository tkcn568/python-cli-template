# AI-Assisted Development Guidelines

This document defines the scope of AI-assisted changes in this repository using large language models (LLMs) like Claude.

## Overview

This project welcomes AI-assisted contributions within defined boundaries. These guidelines preserve code quality, maintainability, and ensure that analytical and architectural decisions remain under direct human review.

---

## Permitted AI-Assisted Operations

### Documentation

LLMs may freely create and edit:

- `README.md` and other markdown documentation
- `CHANGELOG.md` or version history
- Inline code comments and docstrings
- API documentation
- Usage guides and tutorials
- Architecture documentation

### Testing

LLMs may create and edit:

- Unit tests (`tests/test_*.py`)
- Functional tests
- Integration tests
- End-to-end (e2e) tests
- Test fixtures and utilities
- Test configuration files

### Code Enhancement

LLMs may add to existing code files only:

- Docstrings (module, class, function, method)
- Type hints (parameter and return annotations)
- Import organization (fixing circular imports, reorganizing)

---

## Restricted Operations

### Code Implementation and Refactoring

LLMs must NOT:

- Modify function bodies or implementation logic
- Refactor code structure or organization
- Rename functions, classes, or variables
- Change algorithm implementations
- Reorder code beyond what docstrings require
- Add new functions or classes without explicit instruction

**Exception:** If a refactor is explicitly requested in the prompt, the LLM should:
1. Propose the refactoring to the user first
2. Explain the rationale and trade-offs
3. Wait for explicit approval before implementing

### Configuration and Dependencies

LLMs must NOT modify without explicit instruction:

- `pyproject.toml` (except adding docstring-related dependencies)
- `setup.py` or build configuration
- `pyproject.toml` dependency versions (use `pip install -u` or `uv sync` to manage)
- Environment configuration files
- CI/CD pipelines

---

## Workflow for Code Changes

When working on code files:

1. **If the task is adding docstrings:** Proceed directly
2. **If the task requires refactoring:** Stop and propose to the user first
3. **If the task is unclear:** Ask for clarification with specific examples
4. **If changes affect multiple files:** Coordinate across files but stay within permitted scope

---

## File-Level Permissions

| File/Directory | Can Add Docstrings | Can Refactor | Can Add Tests | Can Edit Docs |
|---|:---:|:---:|:---:|:---:|
| `cli/` source code | ✅ | ❌ | ✅ | ✅ |
| `tests/` | ✅ | ✅ | ✅ | ✅ |
| `README.md` | N/A | N/A | N/A | ✅ |
| `CHANGELOG.md` | N/A | N/A | N/A | ✅ |
| `pyproject.toml` | ❌ | ❌ | ❌ | ❌ |
| `*.md` documentation | N/A | N/A | N/A | ✅ |

---

## Communication

When an LLM encounters a restricted operation:

```
"This task requires refactoring [specific_file.py]. I can propose this change 
with the following rationale: [explanation]. Would you like me to proceed?"
```

---

## Rationale

These guidelines ensure:

- **Code integrity:** Business logic and algorithms remain under human oversight
- **Maintainability:** Refactoring decisions are intentional and documented
- **Quality:** Tests and documentation receive AI support for efficiency
- **Accountability:** Core logic changes are traceable to human decisions
- **Collaboration:** AI enhances velocity without replacing judgment

---

## Questions or Updates

If you encounter a scenario not covered by these guidelines, please:

1. Stop and ask for clarification
2. Propose how to handle it
3. Wait for explicit instruction

These guidelines are living documentation and can be updated as needed.
