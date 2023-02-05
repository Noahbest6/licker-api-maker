import subprocess
import time
import os


def generate_ssh_key(key_file):
        # Redirect the output to os.devnull
    with open(os.devnull, 'w') as devnull:
        keyGen = subprocess.Popen(["ssh-keygen", "-t", "rsa", "-f", key_file, "-N", ""], stdout=devnull, stderr=devnull)


    print("Key making")
    time.sleep(5)
    print("key making 2")

    # Check if the process is still running
    if keyGen.poll() is None:
        # Terminate the process
        keyGen.terminate()
    print("key made")
    
def delete_ssh_key(key_file):
    # Delete the RSA key
    subprocess.run(["rm", key_file, key_file + ".pub"])

# Makes a temp key for localhost.run
key_file = "~/.ssh/tempRSAKeyForOnline"
generate_ssh_key(key_file)
Online_Command = "ssh -o StrictHostKeyChecking=no -R 80:localhost:1237 localhost.run"



Online_Command = "ssh -R 80:localhost:1237 localhost.run"
process = subprocess.Popen(Online_Command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(3)

while True:
    output = process.stdout.readline()
    if not output and process.poll() is not None:
        break
    if output:
        with open("output.txt", "w") as file:
            text = output.strip().decode("utf-8")
            start = text.find("tunneled with tls termination, ") + len("tunneled with tls termination, ")
            result = text[start:]
            file.write(result)


rc = process.poll()
print("Return code:", rc)



delete_ssh_key(key_file)