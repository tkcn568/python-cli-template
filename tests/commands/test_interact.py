"""Unit tests for interact command group."""

from unittest.mock import patch

import pytest
from click.testing import CliRunner

from cli.commands.interact import interact


class TestInteractCommandGroup:
    """Test suite for interact command group."""

    @pytest.fixture
    def runner(self):
        """Create a Click CLI test runner."""
        return CliRunner()

    def test_interact_group_help(self, runner):
        """Test that interact group help is accessible."""
        result = runner.invoke(interact, ["--help"])
        assert result.exit_code == 0
        assert "Engage with interactive prompts" in result.output

    def test_prompt_command_help(self, runner):
        """Test that prompt command help is accessible."""
        result = runner.invoke(interact, ["prompt", "--help"])
        assert result.exit_code == 0

    def test_ask_command_help(self, runner):
        """Test that ask command help is accessible."""
        result = runner.invoke(interact, ["ask", "--help"])
        assert result.exit_code == 0

    @patch("cli.commands.interact.adapter.get_random_prompt")
    def test_prompt_command_with_input(self, mock_prompt, runner):
        """Test prompt command with user input."""
        mock_prompt.return_value = "What is your name?"
        result = runner.invoke(interact, ["prompt"], input="Alice\n")
        assert result.exit_code == 0
        assert "Your response:" in result.output
        assert "Alice" in result.output

    @patch("cli.commands.interact.adapter.get_name_prompt")
    @patch("cli.commands.interact.adapter.respond_to_name")
    def test_ask_command_with_input(self, mock_respond, mock_prompt, runner):
        """Test ask command with user input."""
        mock_prompt.return_value = "What's your name?"
        mock_respond.return_value = "Hello, Alice!"
        result = runner.invoke(interact, ["ask"], input="Alice\n")
        assert result.exit_code == 0
        assert "Hello" in result.output
        assert "Alice" in result.output

    @patch("cli.commands.interact.adapter.get_name_prompt")
    @patch("cli.commands.interact.adapter.respond_to_name")
    def test_ask_command_various_names(self, mock_respond, mock_prompt, runner):
        """Test ask command with various names."""
        mock_prompt.return_value = "What's your name?"
        for name in ["Bob", "Charlie", "Diana"]:
            mock_respond.return_value = f"Hello, {name}!"
            result = runner.invoke(interact, ["ask"], input=f"{name}\n")
            assert result.exit_code == 0
            assert name in result.output
