from pathlib import Path
import toml


__details = toml.load('../pyproject.toml')['tool']['poetry']
__location__ = Path(os.path.join(os.path.dirname(os.path.realpath('./__version__.py'))), '..')
__pkgname__ = __details['name']
__version__ = __details['version']
