# JSPy ![Build Status](https://travis-ci.org/rithik/JSPy.svg?branch=master)

## Run JavaScript through Python

## Usage

To use this library, you must first install the library (`pip3 install JSPy`)

In your code, you must import JSPy package by including `import JSPy`.

To execute JavaScript, use the command `JSPy.exec(JAVASCRIPT_STRING)`, where the `JAVASCRIPT_STRING` is the JavaScript you would like to run. This will automatically run the file and return anything that the system returns.

If you would like to execute a JavaScript File, use the command `print(JSPy.exec("FILE_PATH", "file"))`, where `FILE_PATH` is the complete path from the root directory. This will automatically run the file and return anything that the system returns.

## Common Errors

If you get a JavaScript Runtime Error, you can use the following commands:
```
sudo apt-get install npm
sudo apt-get install nodejs
```

If you do not have sudo permissions, you can use the following commands: 
```
curl https://raw.githubusercontent.com/creationix/nvm/v0.25.0/install.sh | bash
nvm install stable
nvm alias default stable
```

If you are using a Windows Computer/Server, download `nodejs` from [https://nodejs.org/](https://nodejs.org/en/). You may have to restart your computer/server for this to be configured.

## Unnoticed Errors

If you would like to report any errors, please open an issue. If you know how to fix the issue, please submit appropiate changes.
