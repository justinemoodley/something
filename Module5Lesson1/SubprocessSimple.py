import os
import subprocess
process = subprocess.Popen(["echo", "Let's try this again"],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     universal_newlines=True)
stdout, stderr = process.communicate()
print("Output:",stdout)
print("Errors:",stderr)

