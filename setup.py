from setuptools import setup

setup(name='PyJS',
      description='Python Library that runs Javascript',
      version='0.2',
      url='https://github.com/rithik/PyJS',
      author='Rithik Yelisetty',
      author_email='rithik@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      packages=['PyJS'],
      install_requires=[
      ],
      entry_points={
          'console_scripts': [
              'PyJS=PyJS.main:run'
          ]
      }
)
