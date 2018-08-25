#!/usr/bin/env python
from mutators import P
p1 = P(200)
#print "p1 = {0}".format(p1.get_x())
p2 = P(-5)
print p1.x
print p2.x
print "#####################"
p1.x=-99

p1.x=(p1.x + p2.x)
print p1.x
