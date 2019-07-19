"""setup.py. Adapted from my old setup.py files and pipenv
(https://github.com/pypa/pipenv/blob/master/setup.py)
"""
import codecs
import json
import os
import pkg_resources
import sys
import setuptools
from setuptools import setup, find_packages, Command
from shutil import rmtree


def has_environment_marker_support():
    """
    Tests that setuptools has support for PEP-426 environment marker support.
    The first known release to support it is 0.7 (and the earliest on PyPI seems to be 0.7.2
    so we're using that), see: http://pythonhosted.org/setuptools/history.html#id142
    References:
    * https://wheel.readthedocs.io/en/latest/index.html#defining-conditional-dependencies
    * https://www.python.org/dev/peps/pep-0426/#environment-markers
    """
    try:
        return pkg_resources.parse_version(setuptools.__version__) >= pkg_resources.parse_version('0.7.2')
    except Exception as exc:
        sys.stderr.write("Could not test setuptool's version: %s\n" % exc)
        return False


cwd = os.path.dirname(os.path.abspath(__file__))

with codecs.open(os.path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

info = {}
with open(os.path.join(cwd, 'tool', '__version__.py')) as f:
    exec(f.read(), info)

required = [
    'setuptools>=36.2.1',
]
extras = {
    'dev': {
        'twine',
        'sphinx',
        'flake8',
    },
    'tests': ['pytest', 'mock']
}
with open(os.path.join(cwd, 'Pipfile.lock')) as f:
    data = json.load(f)
    for item in data['default']:
        dep = '{} {}'.format(item.strip(), data['default'][item]['version'])
        required.append(dep)

classifiers = [
   'Development Status :: 4 - Beta',
   'License :: OSI Approved :: Apache Software License',
   'Environment :: Console',
   'Topic :: Software Development',
   'Intended Audience :: Developers'
] + [('Programming Language :: Python :: %x') for x in '3.6 3.7'.split()]

if has_environment_marker_support():
    extras[':sys_platform=="win32"'] = ['colorama']
elif sys.platform == 'win32':
    required.append('colorama')

    
class UploadCommand(Command):
    """
    Support setup.py upload, if you plan to use it. Uploading via twine is disabled,
    because you may want to upload to other package repositories (e.g., Nexus or Github),
    so the command is just commented out.
    """

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold.
        :param s: Status message
        :type s: str
        """
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(cwd, 'dist'))
        except FileNotFoundError:
            pass
        self.status('Building source distribution...')
        os.system('{} setup.py sdist bdist_wheel'.format(sys.executable))
        self.status('If we were uploading to PyPI or whatever, we\'d do it here via twine...')
        # os.system('twine upload --repository-url https://pypi dist/*')
        self.status('Pushing git tags...')
        os.system('git tag v{}'.format(info['__version__']))
        os.system('git push --tags')
        sys.exit()


class DebCommand(Command):
    """
    Support building packages to .deb files. This happens locally, so it's okay as-is.
    """

    description = 'Build and publish as a .deb.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold.
        :param s: Status message
        :type s: str
        """
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(cwd, 'deb_dist'))
        except FileNotFoundError:
            pass
        self.status(u'Creating debian manifest...')
        os.system(
            '{} setup.py --command-packages=stdeb.command sdist_dsc -z artful --package3=clitool'.format(sys.executable)
        )
        self.status(u'Building .deb...')
        os.chdir('deb_dist/clitool-{}'.format(info['__version__']))
        os.system('dpkg-buildpackage -rfakeroot -uc -us')


setup(
    name='clitool',
    version=info['__version__'],
    description='A CLI tool for something.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Donald Wilcox',
    author_email='dw@angk.org',
    url='https://github.com/makiten/python-cli-template',
    packages=find_packages(exclude=['bin', 'tests', 'tests.*', 'tasks', 'tasks.*']),
    entry_points={
        'console_scripts': [
            'clitool=tool:cli',
        ]
    },
    package_data={
        '': ['LICENSE', 'NOTICES'],
    },
    python_requires='>=3.6.1',
    setup_requires=[],
    install_requires=required,
    extras_require=extras,
    include_package_data=True,
    license='Apache',
    classifiers=classifiers,
    cmdclass={'upload': UploadCommand, 'deb': DebCommand}
)
