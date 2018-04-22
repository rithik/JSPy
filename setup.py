from setuptools import setup

setup(name='JSPy',
      description='Python Library that runs Javascript',
      version='0.4',
      url='https://github.com/rithik/JSPy',
      author='Rithik Yelisetty',
      author_email='rithik@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      packages=['JSPy'],
      install_requires=[
      ],
      entry_points={
          'console_scripts': [
              'JSPy=JSPy.main:run'
          ]
      }
)
