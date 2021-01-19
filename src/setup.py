from setuptools import setup

setup(
  name="smp",
  version="0.1",
  py_modules=['smp'],
  install_requires=[
    'Click',
  ],
  entry_points='''
    [console_scripts]
    smp=smp:smp
  '''
)