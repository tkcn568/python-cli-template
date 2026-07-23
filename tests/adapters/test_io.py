"""Unit tests for IOAdapter."""

import pytest

from cli.adapters.io import IOAdapter


class TestIOAdapter:
    """Test suite for IOAdapter."""

    @pytest.fixture
    def adapter(self):
        """Create an IOAdapter instance for testing."""
        return IOAdapter()

    def test_init(self, adapter):
        """Test IOAdapter initialization."""
        assert adapter is not None

    def test_get_progress_values_returns_tuple(self, adapter):
        """Test that get_progress_values returns a tuple."""
        result = adapter.get_progress_values()
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_get_progress_values_returns_correct_types(self, adapter):
        """Test that get_progress_values returns int and float."""
        total, advance = adapter.get_progress_values()
        assert isinstance(total, int)
        assert isinstance(advance, float)

    def test_get_progress_values_total_range(self, adapter):
        """Test that total value is within expected range."""
        for _ in range(20):
            total, _ = adapter.get_progress_values()
            assert 750 <= total <= 1250

    def test_get_progress_values_advance_range(self, adapter):
        """Test that advance value is within expected range."""
        for _ in range(20):
            _, advance = adapter.get_progress_values()
            assert 0.0 <= advance <= 1.0

    def test_get_progress_values_variability(self, adapter):
        """Test that progress values vary across multiple calls."""
        values = [adapter.get_progress_values() for _ in range(10)]
        totals = [v[0] for v in values]
        advances = [v[1] for v in values]

        # Check that we get different values (not always the same)
        assert len(set(totals)) > 1 or len(set(advances)) > 1

    def test_get_progress_values_consistency(self, adapter):
        """Test that multiple calls return valid values."""
        for _ in range(100):
            total, advance = adapter.get_progress_values()
            assert isinstance(total, int)
            assert isinstance(advance, float)
            assert 750 <= total <= 1250
            assert 0.0 <= advance <= 1.0
