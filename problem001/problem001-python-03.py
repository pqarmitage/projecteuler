#!/usr/bin/python

import time

start = time.time()

for i in range(100000):
    s = 166833 + 99500 - 33165
    
elapsed = time.time() - start

print "result %s found in %s seconds for 100000 iterations" % (s, elapsed)
