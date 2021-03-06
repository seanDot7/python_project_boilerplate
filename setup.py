'''
python_project_boilerplate
-------------------------

python_project_boilerplate is a boilerplate for python project.
Python projects can be futhure developed based on this project.
'''
import re
import ast
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

# Class Tox is for integrated with `setuptools` so that `python setup.py test runs tox tests.
#  class Tox(TestCommand):
    #  def finalize_options(self):
        #  TestCommand.finalize_options(self)
        #  self.test_args = []
        #  self.test_suite = True
        #  def run_tests(self):
            #  #import here, cause outside the eggs aren't loaded
            #  import tox
            #  errcode = tox.cmdline(self.test_args)
            #  sys.exit(errcode)


_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Get version from project module attr __version__
with open('PROJECT_NAME_AS_SRC_DIRECTORY/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='python_project_boilerplate',
    version=version,
    url='http://github.com/seanDot7/python_project_boilerplate/',
    license='MIT',
    author='Qi Wang',
    author_email='seandot7.qi.wang@gmail.com',
    description='A project boilerplate for python '
                'and includes test component',
    long_description=__doc__,
    packages=['python_project_boilerplate'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    install_requires=[
        #  'click>=2.0',
    ],
    classifiers=[
        #  'Programming Language :: Python',
        #  'Development Status :: 4 - Beta',
        #  'Natural Language :: English',
        #  'Environment :: Web Environment',
        #  'Intended Audience :: Developers',
        #  'License :: OSI Approved :: Apache Software License',
        #  'Operating System :: OS Independent',
        #  'Topic :: Software Development :: Libraries :: Python Modules',
        #  'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)
