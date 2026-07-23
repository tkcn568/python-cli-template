# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Comprehensive NumPy-style docstrings for all modules, classes, and functions
- Module-level docstrings for improved code documentation and IDE support
- Enhanced method documentation for all classes with Parameters and Returns sections
- Detailed README with comprehensive usage examples and project structure
- CHANGELOG.md for tracking version history and changes
- Interactive command group (`interact`) for user engagement with random prompts
- Interactive name-based response system for personalized user interactions
- IO simulation command group (`io`) for demonstrating download and process operations
- `InteractAdapter` class for managing interactive prompts and responses
- `IOAdapter` class for IO operation simulations with progress tracking

### Changed

- Refactored package structure from `clitool` to `cli` for cleaner organization
- Updated `pyproject.toml` to reference `cli` package instead of `clitool`
- Improved Status class and command docstrings with clearer parameter documentation
- Enhanced CLI function documentation with parameter types and exceptions
- Expanded README with usage examples for interact and IO commands

### Removed

- Removed legacy `clitool` package in favor of modern `cli` package structure

## [20250825]

### Fixed

- Fixed dependency version constraints

### Changed

- Replaced colorama with rich for improved terminal formatting
- Upgraded deprecated dependencies to latest versions

## [20250801]

### Changed

- Refactored build configuration to use Docker and Poetry

### Removed

- Removed setup.py in favor of pyproject.toml

## [20250715]

### Changed

- Migrated from Pipenv to Poetry for dependency management

## [20250710]

### Added

- Docker support with Dockerfile
- dockerignore configuration

## [20250705]

### Changed

- Improved CLI naming and user-facing output

### Fixed

- Fixed package versioning logic

## [20250702]

### Added

- Quality of life improvements to setup.py

### Fixed

- Fixed PyPI package URL configuration

## [20250630]

### Added

- Initial Docker configuration

## [20250625]

### Changed

- Refactored Click dependency imports and usage patterns

### Fixed

- Fixed package dependency resolution

## [20250620]

### Fixed

- Fixed current working directory handling

## [20210621] - Initial Release

Initial release of python-cli-template with:

- Click-based CLI framework with command groups and subcommands
- Rich terminal output formatting with colorized messages
- End-of-Life (endoflife.date) API integration with full query support
- Modular adapter architecture for external services
- Configuration file path management
- Version management system
- Error handling with Rich-formatted error display
- Poetry-based packaging and dependency management
- Docker containerization support
- Pytest test infrastructure
