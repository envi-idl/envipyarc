"""

"""
import os
from distutils.core import Command as BaseCommand
from unittest import TestLoader, TextTestRunner
from setuptools import setup


class TestCommand(BaseCommand):
    """Runs the package tests."""
    description = 'Runs all package tests.'

    user_options = [
        ('junit=', None,
         'outputs results to an xml file.'),
        ('pattern=', None,
         'The test pattern. Defaults to test*.py')
    ]

    def initialize_options(self):
        self.junit = None
        self.pattern = 'test*.py'

    def finalize_options(self):
        pass

    def run(self):
        # Import xmlrunner here so it's not a setup requirement
        import xmlrunner
        test_suite = TestLoader().discover('.', pattern=self.pattern)
        if self.junit:
            with open(self.junit, 'wb') as output:
                runner = xmlrunner.XMLTestRunner(output)
                runner.run(test_suite)
        else:
            runner = TextTestRunner(verbosity=2)
            runner.run(test_suite)

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(name='envipyarc',
      version='1.0.7',
      description='ENVI Python Tools for ArcGIS',
      long_description=long_description,
      url='https://github.com/envi-idl/envipyarc',
      author='Exelis Visual Information Solutions, Inc.',
      packages=['envipyarc',
                'envipyarc.templates'],
      install_requires=['envipyengine>=1.0.5', 'envipyarclib'],
      cmdclass=dict(test=TestCommand),
      license='MIT',
      keywords='envi idl',
      scripts=['scripts/createenvitoolbox.py'],
      package_data={'envipyarc': [
          'esri/toolboxes/*.pyt',
          'esri/toolboxes/*.xml',
          'esri/projecttemplates/*.aptx',
          'esri/projecttemplates/*.md'
          ]
      }
)
