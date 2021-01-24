#!usr/bin/env
import argparse

parser = argparse.ArgumentParser()

# The add_argument( ) method allows us to specify the command line options that the program is willing to accept
# Argparse treats the options as strings, so we can specify the data type that we want to work with
parser.add_argument("-a", "--add", help="add the input to a preset number", type=int, default=0)
parser.add_argument("-s", "--sub", help="subtracts the input from a preset number", type=int, default=0)
parser.add_argument("-d", "--div", help="divides the input by a preset number", type=float, default=0)

# The parse_args( ) method returns some data from the options specified
args = parser.parse_args()
resultAdd = int(args.add+5)
resultSub = int(10-args.sub)
resultDiv = float(args.div/3)


if args.add:
    print("The random addition results to {}".format(resultAdd))
elif args.sub:
    print("The random subtraction results to {}".format(resultSub))
elif args.div:
    print("The random division leads to {}".format(resultDiv))
else:
    print(args)
