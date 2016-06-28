from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='Frequently Used Tools',
      version='0.1',
      description='A bunch of stuff that I find useful.',
      url='https://github.com/RobTheOceanographer/futs.git',
      author='Robert Johnson',
      author_email='robtheoceanographer@gmail.com',
      license='MIT',
      packages=['futs'],
      test_suite='nose.collector',
      tests_require=['nose'],
      scripts=[
            'bin/funniest_joke',
            'bin/unpack',
            'bin/findin',
            'bin/findfile',
            'bin/deepsearch',
            ],
      install_requires=[
          "markdown",
          "pyorbital",
          "ephem",
          "datetime",
          "numpy",
          "tzwhere",
      ],
      zip_safe=False)
