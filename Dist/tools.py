pyDist = {'a':5,'d':8,'c':4,'h':2,'e':1}

# reversing the dictonary by its values
import operator
print (sorted(pyDist.items(), key=operator.itemgetter(1)))
# [('e', 1), ('h', 2), ('c', 4), ('a', 5), ('d', 8)]
