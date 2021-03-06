from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(name='cocomoco',
      version='0.1.0',
      description='Cocomo Metric Calculator',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/hgn/cocomoco',
      author='Hagen Paul Pfeifer',
      author_email='hagen@jauu.net',
      license='MIT',
      packages=['cocomoco'],
      test_suite='tests',
      classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.7',
        ],
      entry_points={
          'console_scripts': [
              'cocomoco = cocomoco.__main__:main'
          ]
      },
      zip_safe=False
     )
