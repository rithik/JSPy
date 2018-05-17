import os
import subprocess
import tempfile

def exec(data, jstype='string'):

    output_string = ""

    if jstype == "string":
        with open("test.js", "w") as text_file:
            text_file.write(data)
            cmd = ['node', 'test.js']

    if jstype == 'file':
        cmd = ['node', data]

    if not jstype == 'string' and not jstype == 'file':
        raise ValueError("The jstype must be either 'string' or 'file'!")

    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(cmd, stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output_string += tempf.read().decode('utf-8')
    
    if jstype == "string": 
        os.remove('test.js')

    return output_string

