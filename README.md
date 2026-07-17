# python-cli-template

A modern command-line interface framework for building scalable CLI applications in Python. This template demonstrates best practices for organizing commands, managing dependencies, and integrating with external APIs.

## Features

- **Click-based command framework** — Simple and intuitive CLI structure using the Click library
- **Rich output formatting** — Beautiful, colorized terminal output with table support
- **Modular architecture** — Organized command groups and HTTP adapters for external services
- **End-of-Life data integration** — Example integration with the endoflife.date API for querying product lifecycle information
- **Docker support** — Containerized deployment with Dockerfile included
- **Modern Python packaging** — Uses Poetry for dependency management and packaging

## Installation

### From source

```bash
git clone <repository>
cd python-cli-template
pip install -e .
```

### With Poetry

```bash
git clone <repository>
cd python-cli-template
poetry install
```

### With Docker

```bash
docker build -t python-cli-template .
docker run python-cli-template --help
```

## Usage

### General command structure

```bash
clitool [COMMAND] [OPTIONS]
```

### Available commands

#### Version information

```bash
clitool --version
```

#### End-of-Life data queries

The CLI includes a full-featured subcommand group for querying product lifecycle data:

```bash
clitool endoflife --help
```

##### Endpoints

List all available API endpoints:

```bash
clitool endoflife endpoints
```

##### Products

Query all products:

```bash
clitool endoflife products
```

Query a specific product:

```bash
clitool endoflife products --product python
```

Query a specific product release:

```bash
clitool endoflife products --product python --release 3.11
```

Get full product details:

```bash
clitool endoflife products --full
```

##### Categories

List all categories:

```bash
clitool endoflife categories
```

Query a specific category:

```bash
clitool endoflife categories --category language
```

##### Tags

List all tags:

```bash
clitool endoflife tags
```

Query a specific tag:

```bash
clitool endoflife tags --tag lts
```

## Project structure

```
python-cli-template/
├── cli/
│   ├── __init__.py              # Package initialization
│   ├── __main__.py              # Entry point for python -m invocation
│   ├── __version__.py           # Version management
│   ├── config.py                # Configuration file paths
│   ├── main.py                  # Root command group
│   ├── adapters/                # External service adapters
│   │   ├── __init__.py
│   │   └── endoflife.py         # endoflife.date API client
│   └── commands/                # CLI command groups
│       ├── __init__.py
│       └── endoflife.py         # End-of-Life data commands
├── tests/                       # Unit tests
├── pyproject.toml              # Project metadata and dependencies
├── Dockerfile                   # Docker configuration
└── README.md                    # This file
```

## Development

### Setting up the development environment

```bash
poetry install --with dev
```

### Running tests

```bash
pytest
```

### Code quality checks

Linting with ruff:

```bash
ruff check cli/ tests/
```

Formatting with ruff:

```bash
ruff format cli/ tests/
```

### Building the package

```bash
poetry build
```

## Architecture

### Command structure

Commands are organized in a hierarchical group structure using Click's command groups. The main entry point is defined in `cli/main.py`, with subcommand groups in the `cli/commands/` directory.

### Adapters

The `cli/adapters/` package contains adapter classes that provide clean interfaces for external APIs. The `EndOfLifeAdapter` class wraps the endoflife.date API, handling HTTP requests and response parsing.

### Error handling

Error handling uses Rich for formatted error display and Click's `Abort` exception to gracefully exit the program on errors.

## Dependencies

### Core

- **click** — CLI framework and command decorator system
- **requests** — HTTP client for API requests
- **rich** — Terminal formatting and colored output
- **tqdm** — Progress bar support

### Development

- **pytest** — Testing framework
- **ruff** — Fast Python linter and formatter
- **sphinx-click** — Sphinx extension for Click command documentation
- **stdeb** — Debian package builder for Python

## Configuration

Configuration files are searched in the following order:

1. `~/.local/python-cli-template/settings.conf`
2. `~/.python-cli-templaterc`
3. `~/.python-cli-template/settings.conf`
4. `./.python-cli-template/settings.conf`

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug reports and feature requests.

### AI-Assisted Development

This project may include AI-assisted contributions for documentation, testing, and docstring enhancement. See [CLAUDE.md](CLAUDE.md) for detailed guidelines on what AI systems can and cannot modify in this codebase.
