"""CLI Driver

Handles the CLI.

Functions:
----------

- get_response: Helper function for making HTTP request
- cli: The actual cli function
- build_data: Helper function for generating list of data

"""
import os
import time
import traceback
import sys
from colorama import Style, Fore
from click import (
    command, echo, option, pass_context, prompt, version_option
)
from tqdm import tqdm
from .output import Status
from .__version__ import __version__

@command()
@option('-n',
        '--name',
        help='Your name')
@option('-f',
        '--flag',
        is_flag=True,
        default=False,
        help='A boolean flag (default: False)')
@option('-m',
        '--messages',
        multiple=True,
        help='Messages you want to send.')
@version_option(prog_name='{}clitool{}'.format(Style.BRIGHT, Style.RESET_ALL), version=__version__)
@pass_context
def cli(ctx,
        name,
        flag,
        messages):
    """Manages to CLI

    :param ctx: Program context
    :type ctx: Context
    :param name: Name
    :type name: str
    :param flag: Flag
    :type flag: bool
    :param messages: Messages
    :type messages: list(str)
    """
    try:
        echo('Current context: {}{}{}'.format(Style.BRIGHT, ctx.info_name, Style.RESET_ALL))

        if name == '' or name is None:
            name = prompt('Please give your name', type=str)
        else:
            echo(Status.success('Name param passed: {}'.format(name)))
        echo('Hi {}!'.format(name))

        if flag:
            echo(Status.info('Flag is set.'))
        else:
            echo(Status.warning('No flag set.'))

        if len(messages) > 0:
            echo(Status.info('Counted {}{}{} messages.'.format(Style.BRIGHT, len(messages), Style.RESET_ALL)))
            pbar = tqdm(messages)
            for m in pbar:
                time.sleep(0.5)
                pbar.set_description('Processing "{}"...'.format(m))
        else:
            echo(Status.info('No messages.'))
    except:
        echo(Status.error(traceback.format_exc()))
        sys.exit(1)
