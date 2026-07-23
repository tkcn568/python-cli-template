"""Adapter for interactive user engagement.

This module provides an adapter for managing interactive prompts and responses,
including random prompt selection and personalized name-based responses with
Rich formatting support.
"""

import random

PROMPTS = [
    "What and what accessories do I sell?",
    "How do reptiles capitalize?",
    "Can you circle back with them?",
]


class InteractAdapter:
    """Adapter for managing interactive user prompts and responses."""

    def __init__(self) -> None:
        """Initialize the InteractAdapter."""
        pass

    def get_random_prompt(self) -> str:
        """Retrieve a random prompt from the available prompts.

        Returns
        -------
        str
            A random prompt string for user interaction
        """
        return PROMPTS[random.randint(0, 2)]

    def get_name_prompt(self) -> str:
        """Retrieve a formatted prompt asking for the user's name.

        Returns
        -------
        str
            A formatted Rich markup string prompting for name input
        """
        return "[bold dark_orange]What's your name?[/bold dark_orange]"

    def respond_to_name(self, name: str) -> str:
        """Generate a personalized greeting for the given name.

        Parameters
        ----------
        name : str
            The user's name

        Returns
        -------
        str
            A formatted Rich markup string with a personalized greeting
        """
        return f"Hello, [bold dark_orange]{name}[/bold dark_orange]!"
