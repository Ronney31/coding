#https://www.codechef.com/DEC18B/problems/DLDAG
n,m=map(int,input().strip().split())
tree = {}
for _ in range(m):
    u,v=map(int,input().strip().split())
    if u not in tree:
        tree[u] = [v]
    else:
        tree[u].append(v)
    if v not in tree:
        tree[v] = []

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

def cal(tre,res,p):
    print (res)
    if len(tre) == 0:
        return (res,p)
    itra = 0
    rs=[]
    for i in tre:
        if itra == 2:
            break
        if len(tre[i]) == 0:
            rs.append(i)
            itra+=1
            
    for i in rs:
        if i in tre:
            del(tre[i])
    for key in tre:
        for i in rs:
            if i in tre[key]:
                tre[key].remove(i)
    p+=1
    res.append(rs)
    return cal(tre,res,p)
    
print (tree)
sortedtree = revDistLen(tree)
print (sortedtree)
result = cal(sortedtree,[],0)
it = result[1]
print (it)
for i in range(it):
    if( i <  int(it/2)):
        print (2,end=" ")
    else:
        print (1,end=" ")
    for j in result[0][i]:
        print (j,end=" ")
    print()


'''
input
6 6
1 2
2 3
1 3
3 4
3 5
1 6
output
4
2 4 5 
2 6 3 
1 2 
1 1
'''
