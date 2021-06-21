import os
import toml


__buildname__ = 'tool'
__details = toml.load('../pyproject.toml')[__buildname__]['poetry']
__pkgname__ = __details['name']
__location__ = os.path.split(os.path.dirname(os.path.realpath('./__version__.py')))[-1]
__version__ = __details['version']
