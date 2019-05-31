# Problem Statement 1

def frequency(lst):
    fre_dic={}
    for i in lst:
        if i not in fre_dic:
            fre_dic[i] =1
        else:
            fre_dic[i] +=1
    for key in fre_dic:
        print(key, " - ", fre_dic[key])


'''
    if input are like following:-
        kasol kasol manali delhi delhi manali kasol
        1 a c b c  1
'''
input_lst = list(map(str, input().strip().split()))
frequency(input_lst)


arr = [1,1]
def problem_staircase(n):
    if n == 0 or n == 1:
        return 1
    else:
        return problem_staircase(n-1) + problem_staircase(n-2)

problem_staircase(7)
print("No. of ways for stairCase are :- ",len(arr))


