import sys

print("Begin!")

print(sys.argv)

assert sys.argv[1] == "--learning-rate"
assert sys.argv[2] == "5"
print("Passed!")

assert sys.argv[2] == "5"

import os.path

assert os.path.exists('data')
assert os.path.exists('data/check.txt')

print("End!")