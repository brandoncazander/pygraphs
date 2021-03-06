from codecs import open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='pygraphs',
      version='0.0.1',
      description="Draw and analyze graphs",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Brandon Cazander',
      author_email='brandon@bcdynamic.com',
      url='https://github.com/brandoncazander/pygraphs',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      pygraphs=pygraphs.scripts:cli
      """
      )
