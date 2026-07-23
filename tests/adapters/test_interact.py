"""Unit tests for InteractAdapter."""

import pytest

from cli.adapters.interact import InteractAdapter, PROMPTS


class TestInteractAdapter:
    """Test suite for InteractAdapter."""

    @pytest.fixture
    def adapter(self):
        """Create an InteractAdapter instance for testing."""
        return InteractAdapter()

    def test_init(self, adapter):
        """Test InteractAdapter initialization."""
        assert adapter is not None

    def test_get_random_prompt(self, adapter):
        """Test that get_random_prompt returns a prompt from PROMPTS."""
        prompt = adapter.get_random_prompt()
        assert isinstance(prompt, str)
        assert prompt in PROMPTS

    def test_get_random_prompt_returns_string(self, adapter):
        """Test that get_random_prompt always returns a string."""
        for _ in range(10):
            prompt = adapter.get_random_prompt()
            assert isinstance(prompt, str)
            assert len(prompt) > 0

    def test_get_name_prompt(self, adapter):
        """Test that get_name_prompt returns a formatted prompt."""
        prompt = adapter.get_name_prompt()
        assert isinstance(prompt, str)
        assert "name" in prompt.lower()
        assert "[bold dark_orange]" in prompt

    def test_get_name_prompt_format(self, adapter):
        """Test that get_name_prompt contains Rich formatting."""
        prompt = adapter.get_name_prompt()
        assert prompt == "[bold dark_orange]What's your name?[/bold dark_orange]"

    def test_respond_to_name(self, adapter):
        """Test that respond_to_name returns a personalized greeting."""
        response = adapter.respond_to_name("Alice")
        assert isinstance(response, str)
        assert "Alice" in response
        assert "Hello" in response

    def test_respond_to_name_with_various_inputs(self, adapter):
        """Test respond_to_name with different names."""
        test_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        for name in test_names:
            response = adapter.respond_to_name(name)
            assert name in response
            assert "Hello" in response
            assert "[bold dark_orange]" in response

    def test_respond_to_name_format(self, adapter):
        """Test that respond_to_name response has Rich formatting."""
        name = "TestUser"
        response = adapter.respond_to_name(name)
        assert response == f"Hello, [bold dark_orange]{name}[/bold dark_orange]!"

    def test_respond_to_name_empty_string(self, adapter):
        """Test respond_to_name with empty string."""
        response = adapter.respond_to_name("")
        assert "Hello" in response
        assert "[bold dark_orange][/bold dark_orange]" in response
