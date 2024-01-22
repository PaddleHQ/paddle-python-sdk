"""
Release script to upload paddle-billing-python-sdk to PyPi
"""

import click
import requests
from os         import environ
from pathlib    import Path
from shutil     import rmtree
from subprocess import check_call, Popen
from sys        import exit


PYPI_PACKAGE_NAME = 'paddle-billing-python-sdk'
PYPI_URL          = 'https://pypi.org/pypi/{package}/json'
DIST_PATH         = 'dist'
DIST_PATH_DELETE  = 'dist_delete'
CONTEXT_SETTINGS  = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


@cli.command()
@click.option('--force/--no-force', default=False, help='Will force a new build removing the previous ones')
def build(force):
    """
    Builds the distribution files: wheels and source
    """

    dist_path = Path(DIST_PATH)
    if dist_path.exists() and list(dist_path.glob('*')):
        if force or click.confirm(f"{dist_path} is not empty - delete contents?"):
            dist_path.rename(DIST_PATH_DELETE)
            rmtree(Path(DIST_PATH_DELETE))
            dist_path.mkdir()
        else:
            click.echo('Aborting')
            exit(1)

    check_call(['python', 'setup.py', 'bdist_wheel'])
    check_call(['python', 'setup.py', 'sdist', '--formats=gztar'])


@cli.command()
@click.option('--release/--no-release', default=False, help='--release to upload to pypi otherwise upload to test.pypi')
@click.option('--rebuild/--no-rebuild', default=True,  help='Will force a rebuild of the build files (src and wheels)')
@click.pass_context
def upload(ctx, release, rebuild):
    """
    Uploads distribution files to pypi or pypitest
    """

    dist_path = Path(DIST_PATH)
    if rebuild is False:
        if not dist_path.exists() or not list(dist_path.glob('*')):
            print("No distribution files found. Please run 'build' command first")
            return
    else:
        ctx.invoke(build, force=True)

    if release:
        args = ['twine', 'upload', 'dist/*']
    else:
        repository = 'https://test.pypi.org/legacy/'
        args       = ['twine', 'upload', '--repository-url', repository, 'dist/*']

    env = environ.copy()

    p = Popen(args, env=env)
    p.wait()


@cli.command()
def check():
    """ Checks the long description. """
    dist_path = Path(DIST_PATH)
    if not dist_path.exists() or not list(dist_path.glob('*')):
        print("No distribution files found. Please run 'build' command first")
        return

    check_call(['twine', 'check', 'dist/*'])


@cli.command()
@click.option('--annotate/--no-annotate', default=False, help='Annotate coverage on files')
@click.option('--coverage/--no-coverage', default=False, help='Run coverage')
@click.option('-v/-nv',                   default=False, help='Verbose')
@click.option('-vv/-nvv',                 default=False, help='Very verbose')
def test(annotate, coverage, v, vv):
    """
    Runs tests and optionally creates annotated files of coverage
    """

    args = ['python3', '-m', 'pytest', 'tests/']
    if coverage:
        args.append('--cov=O365')
        if annotate:
            args.append('--cov-report')
            args.append('annotate')
        if v:  # Verbose
            args.append('-v')
        if vv and not v:  # Very verbose
            args.append('-vv')

    env = environ.copy()

    p = Popen(args, env=env)
    p.wait()


def _get_releases():
    """
    Retrieves all releases on pypi
    """
    releases = None

    response = requests.get(PYPI_URL.format(package=PYPI_PACKAGE_NAME))
    if response:
        data = response.json()

        releases      = []
        releases_dict = data.get('releases', {})

        if releases_dict:
            for version, release in releases_dict.items():
                release_formats   = []
                published_on_date = None
                for fmt in release:
                    release_formats.append(fmt.get('packagetype'))
                    published_on_date = fmt.get('upload_time')

                release_formats = ' | '.join(release_formats)
                releases.append((version, published_on_date, release_formats))

    releases.sort(key=lambda x: x[1])

    return releases


@cli.command(name='list')
def list_releases():
    """
    Lists all releases published on pypi
    """

    releases = _get_releases()

    if releases is None:
        print(f"Package '{PYPI_PACKAGE_NAME}' not found on Pypi.org")
    elif not releases:
        print(f"No releases found for '{PYPI_PACKAGE_NAME}'")
    else:
        for version, published_on_date, release_formats in releases:
            print(f"{version:<10}{published_on_date:>15}{release_formats:>25}")
