from setuptools import setup

setup(name='fbrecog',
      version='1.2',
      description="An unoffcial wrapper for Facebook's recognition endpoint",
      url='http://github.com/samj1912/fbrecog',
      author='Sambhav Kothari',
      author_email='sambhavs.email@gmail.com',
      license='MIT',
      packages=['fbrecog'],
      install_requires=[
          'facepy',
          'requests',
          'six',
      ],
      zip_safe=False)
