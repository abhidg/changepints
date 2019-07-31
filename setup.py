from setuptools import setup

setup(name='changepints',
      version='0.1',
      description='ChangePINTS is a changepoint library for PINTS functional testing',
      url='https://github.com/abhidg/changepints',
      author='Abhishek Dasgupta',
      author_email='abhishek.dasgupta@cs.ox.ac.uk',
      packages=['changepints'],
      install_requires=[
          'ruptures',
          'fire'
      ],
      entry_points={
          'console_scripts': ['changepints=changepints:main']
      },
      zip_safe=False)
