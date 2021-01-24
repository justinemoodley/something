import os
# os.popen executes the command specified.
# echo refers to writing to the console line.
# This line of code writes the text Hello world!
# to the console window and returns a pipe / stream
# connection to the console window so that our script
# can read the output.
stream = os.popen("echo Hello world!")
output = stream.read()
print(output)
