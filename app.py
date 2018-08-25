from mutators import P
p1 = P(3333)
#print "p1 = {0}".format(p1.get_x())
p2 = P(4711)
print p1.get_x()
p1.set_x(99)
p1.set_x(p1.get_x() + p2.get_x())
print p1.get_x()
