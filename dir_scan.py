# print directory tree
import os
import sys
import argparse

try:
    parser = argparse.ArgumentParser(description='Display file tree.')
    parser.add_argument('dir', nargs='?', default='.', help='directory to scan')
    parser.add_argument('--len', nargs='?', default='2', type=int, help='length of each depth')
    parser.add_argument('--filter', nargs='?', default='', help='filter keywords, delimited by comma:\',\'')
    result = parser.parse_args()
except Exception as inst:
    print("error: {0}".format(inst))

for dirname, subdir, files in os.walk(result.dir):
    if result.filter and reduce(lambda x,y: x or y,map(lambda x: x in dirname, result.filter.split(','))):
        pass
    else:
        depth = len(dirname.split('/'))
        length = result.len*depth
        sublength = length+result.len
        print ('='*length+'['+dirname+']')
        for f in files:
            if result.filter and reduce(lambda x,y: x or y,map(lambda x: x in f, result.filter.split(','))):
                pass
            else:
                print ('-'*sublength+f)
