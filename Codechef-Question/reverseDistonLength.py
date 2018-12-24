#this function will reverse the dictonary base on the length of the items
#it except only integer key, values pair.

#tree = {1: [2, 3, 6], 2: [3], 3: [4, 5], 4: [], 5: [], 6: []}

import operator
def revDistLen(tr):
    newtree = {}
    #sorted_tree_list  = sorted(tr)
    #sorted_tree_list_len = []
    len_tree = {}
    for i in tr:
        len_tree[i] = len(tr[i])
    #{1: 3, 2: 1, 3: 2, 4: 0, 5: 0, 6: 0}

    for key in sorted(len_tree.items(),key=operator.itemgetter(1)):
        newtree[key[0]] = tr[key[0]]
        
    return newtree


#print (revDistLen(tree))
