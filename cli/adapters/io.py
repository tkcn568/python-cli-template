"""Adapter for simulating IO-related operations.

This module provides an adapter for managing IO operation simulations,
including progress tracking with randomized values.
"""

import random


class IOAdapter:
    """Adapter for managing IO operation simulations."""

    def __init__(self) -> None:
        """Initialize the IOAdapter."""
        pass

    def get_progress_values(self) -> tuple[int, float]:
        """Generate randomized progress tracking values.

        Returns
        -------
        tuple[int, float]
            A tuple containing:
            - total (int): Total progress units (750-1250)
            - advance (float): Progress increment per step (0.0-1.0)
        """
        total = random.randint(750, 1250)
        advance = random.random()

        return total, advance
