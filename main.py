import sys
import os.path
from clusterone import get_data_path

print("Begin!")

print(sys.argv)

assert sys.argv[1] == "--learning-rate"
assert sys.argv[2] == "5"
print("Passed!")

assert sys.argv[2] == "5"

print(os.listdir("/"))

assert os.path.exists('/data')
assert os.path.exists('/data/check.txt')

print("End!")