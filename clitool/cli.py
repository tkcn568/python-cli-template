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
from click import (
    command, echo, option, pass_context, prompt, version_option
)
from rich import print
from tqdm import tqdm
from .output import Status
from .__version__ import (__pkgname__, __version__)


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
@version_option(
    prog_name=f'[bold]{__pkgname__}[/]',
    version=__version__
)
@pass_context
def cli(ctx,
        name,
        flag,
        messages):
    """Manages to CLI

    Parameters
    ----------
    ctx : Context
        Program context
    name : str
        Name
    flag : bool
        Flag
    messages : list(str)
        Messages
    """
    try:
        print(f'Current context: [bold]{ctx.info_name}[/bold]')

        if name == '' or name is None:
            print(Status.error('I didn\'t find a name, so I\'m going to ask you for one.'))
            name = prompt('Please give your name', type=str)
        else:
            print(Status.success(f'Name param passed: {name}'))
        print(f'Hi {name}!')

        if flag:
            print(Status.info('Flag is set.'))
        else:
            print(Status.warning('No flag set.'))

        if len(messages) > 0:
            print(Status.info(f'Counted {len(messages)} messages.'))
            pbar = tqdm(messages)
            for m in pbar:
                time.sleep(0.5)
                pbar.set_description('Processing "{}"...'.format(m))
        else:
            print(Status.info('No messages.'))

        print(Status.success(f'Alright, {name}. Everything is done.'))
    except:
        print(Status.error(traceback.format_exc()))
        sys.exit(1)
