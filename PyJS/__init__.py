import subprocess
import tempfile

def exec(data):

    with open("test.js", "w") as text_file:
        text_file.write(data)

    cmd = ['node', 'test.js']
    output_string = ""

    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(cmd, stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output_string += tempf.read().decode('utf-8')

    return output_string
