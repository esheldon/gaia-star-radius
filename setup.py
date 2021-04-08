import glob
from setuptools import setup

scripts = glob.glob('bin/*')
scripts = [s for s in scripts if '~' not in s]


setup(
    name="gaia-star-radius",
    author="Erin Sheldon",
    url="https://github.com/esheldon/gaia-star-radius",
    description=(
        'Code to measure the radius at which the '
        'star profile reaches the noise level'
    ),
    scripts=scripts,
    version='0.1.0',
)
