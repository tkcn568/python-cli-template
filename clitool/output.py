"""Message Manager

Handles messages sent to stdout.

Classes:
--------

- Output: A static class for sending output to stdout.
"""


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
    def console_message(msg: str,
                        icon: str,
                        prefix: str = '',
                        styles: str = '') -> str:
        """Prepares the string message with a given color and type.

        Parameters
        ----------
        msg : str
            The actual message to send.
        icon : str
            The output type to send with the message text.
        styles : str
            The styles of the box denoting the output type.
        
        Returns
        -------
        str
            The message with output type and colored text for output type.
        """
        if prefix != '':
            prefix += ' '
        if icon != '':
            icon = f'{icon} '
        styles_begin = styles
        styles_end = ""
        if styles_begin:
            styles_begin = f"[{styles_begin}]"
            styles_end = "[/]"
        output = (prefix
                  + icon
                  + styles_begin
                  + msg
                  + styles_end)

        return output

    @staticmethod
    def error(msg: str, prefix: str = ''):
        """Prepares error messages.

        Parameters
        ----------
        msg : str
            The actual message to send.

        Returns
        -------
        str
            The message with a red ERROR block preceding it.
        """
        return Status.console_message(msg, u'\u274C', prefix, "bright_red")

    @staticmethod
    def info(msg: str, icon: str = '', prefix: str = ''):
        """Prepares informational messages.

        Parameters
        ----------
        msg : str
            The actual message to send.

        Returns
        -------
        str
            The message with a blue INFO block preceding it.
        """
        return Status.console_message(msg, icon, prefix)

    @staticmethod
    def success(msg: str, prefix: str = ''):
        """Prepares success messages.

        Parameters
        ----------
        msg : str
            The actual message to send.

        Returns
        -------
        str
            The message with a green checkmark preceding it.
        """
        return Status.console_message(msg, u'\u2705', prefix, "green")

    @staticmethod
    def warning(msg: str, prefix: str = ''):
        """Prepares warning messages.

        Parameters
        ----------
        msg : str
            The actual message to send.
        
        Returns
        -------
        str
            The message with a yellow WARNING block preceding it.
        """
        return Status.console_message(msg, u'\u26D4', prefix, "yellow")
