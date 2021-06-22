"""Message Manager

Handles messages sent to stdout.

Classes:
--------

- Output: A static class for sending output to stdout.
"""
from colorama import (Back, Style)


class Status:
    """
    Handling messages sent via stdout.
    
    Methods
    -------
    
    console_message(msg, output_type, color)
        Base method for preparing data to be sent to stdout.
    error(msg)
        Prepares error output.
    info(msg)
        Prepares normal, informational output.
    success(msg)
        Prepares output for successful operations.
    warning(msg)
        Prepares warning messages for output.
    """

    @staticmethod
    def console_message(msg, output_type, color):
        """Prepares the string message with a given color and type.
        
        :param msg: The actual message to send.
        :type msg: str
        :param output_type: The output type to send with the message text.
        :type output_type: str
        :param color: The color of the box denoting the output type.
        :type color: colorama.Back
        :returns: The message with output type and colored text for output type.
        :rtype: str
        """
        output = (color
                  + Style.BRIGHT
                  + ' {0} '.format(output_type.upper())
                  + Style.RESET_ALL
                  + ' '
                  + msg)

        return output

    @staticmethod
    def error(msg):
        """Prepares error messages.
        
        :param msg: The actual message to send.
        :type msg: str
        :returns: The message with a red ERROR block preceding it.
        :rtype: str
        """
        return Status.console_message(msg, 'error', Back.RED)

    @staticmethod
    def info(msg):
        """Prepares informational messages.
        
        :param msg: The actual message to send.
        :type msg: str
        :returns: The message with a blue INFO block preceding it.
        :rtype: str
        """
        return Status.console_message(msg, 'info', Back.BLUE)

    @staticmethod
    def success(msg):
        """Prepares success messages.
        
        :param msg: The actual message to send.
        :type msg: str
        :returns: The message with a green SUCCESS block preceding it.
        :rtype: str
        """
        return Status.console_message(msg, 'success', Back.GREEN)

    @staticmethod
    def warning(msg):
        """Prepares warning messages.
        
        :param msg: The actual message to send.
        :type msg: str
        :returns: The message with a yellow WARNING block preceding it.
        :rtype: str
        """
        return Status.console_message(msg, 'warning', Back.YELLOW)
