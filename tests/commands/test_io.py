"""Unit tests for io command group."""

import pytest
from click.testing import CliRunner

from cli.commands.io import io


class TestIOCommandGroup:
    """Test suite for io command group."""

    @pytest.fixture
    def runner(self):
        """Create a Click CLI test runner."""
        return CliRunner()

    def test_io_group_help(self, runner):
        """Test that io group help is accessible."""
        result = runner.invoke(io, ["--help"])
        assert result.exit_code == 0
        assert "Simulate executing IO-related functionality" in result.output

    def test_simulate_download_command_help(self, runner):
        """Test that simulate-download command help is accessible."""
        result = runner.invoke(io, ["simulate-download", "--help"])
        assert result.exit_code == 0

    def test_simulate_process_command_help(self, runner):
        """Test that simulate-process command help is accessible."""
        result = runner.invoke(io, ["simulate-process", "--help"])
        assert result.exit_code == 0

    def test_simulate_download_requires_filename(self, runner):
        """Test that simulate-download requires a filename argument."""
        result = runner.invoke(io, ["simulate-download"])
        assert result.exit_code != 0

    def test_simulate_process_requires_filename(self, runner):
        """Test that simulate-process requires a filename argument."""
        result = runner.invoke(io, ["simulate-process"])
        assert result.exit_code != 0
