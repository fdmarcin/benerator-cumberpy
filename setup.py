from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='benerator_cumberpy',
      version='0.1.2',
      description='A Ben Cumberbatch-like name generator',
      long_description=long_description,
      url='https://github.com/fdmarcin/benerator-cumberpy',
      download_url='https://github.com/fdmarcin/benerator-cumberpy/archive/0.1.2.tar.gz',
      author='Marcin Sędłak-Jakubowski',
      author_email='fdmarcin@gmail.com',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',

          # Indicate who your project is intended for
          'Intended Audience :: End Users/Desktop',
          'Topic :: Games/Entertainment',

          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],

      keywords='benedict cumberbatch word generator',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'hello-ben = benerator_cumberpy:hello'
          ]
      },
      )
