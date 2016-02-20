#_*_ coding: utf-8 _*_

import sys

args = sys.argv

script = args[0]
input_file = args[1]


def print_all(file):
	print file.object.read();

