# print directory tree
import os
import sys
import argparse

if sys.platform == "linux" or sys.platform == "linux2":
    directory_delimiter = '/'
elif sys.platform == "darwin":
    directory_delimiter = "/"
elif sys.platform == "win32":
    directory_delimiter = "\\"
elif sys.platform == "win64":
    directory_delimiter = "\\"
else:
    print "Error: the platform you are using is: {0}, guessing directory delimiter is /".format(sys.platform)
    directory_delimiter = "/"

try:
    parser = argparse.ArgumentParser(description='Display file tree.')
    parser.add_argument('dir', nargs='?', default='.', help='directory to scan')
    parser.add_argument('--len', nargs='?', default='2', type=int, help='length of each depth')
    parser.add_argument('--filter', nargs='?', default='', help='filter keywords, delimited by comma:\',\'')
    parser.add_argument('--dir-only', nargs='?', const=True, default=False, type=bool, help='show directory only')
    result = parser.parse_args()
except Exception as inst:
    print("error: {0}".format(inst))

offset = os.path.abspath(result.dir).count(directory_delimiter)*result.len - result.len

for dirname, subdir, files in os.walk(os.path.abspath(result.dir)):
    if result.filter and reduce(lambda x,y: x or y,map(lambda x: x in dirname, result.filter.split(','))):
        pass
    else:
        depth = dirname.count(directory_delimiter)
        length = result.len*depth-offset
        sublength = length+result.len
        print ('='*length+'['+dirname+']')
        for f in files:
            if result.dir_only or (result.filter and reduce(lambda x,y: x or y,map(lambda x: x in f, result.filter.split(',')))):
                pass
            else:
                print ('-'*sublength+f)
