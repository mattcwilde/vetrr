from setuptools import setup

setup(name='vetrr',
      version='0.1.2',
      description='vet redrock outputs',
      url='http://github.com/mattcwilde/vetrr',
      author='Matthew Wilde',
      author_email='mattcwilde@gmail.com',
      license='MIT',
      packages=['vetrr'],
      dependency_links=['https://github.com/linetools/linetools'],
      install_requires=[
        'matplotlib',
        'pyYAML',
        'astropy',
        'PyQt5',
        'future',
        'numpy'
        ],
      zip_safe=True)
