#list comprehension method
def array_diff_via_lc(a,b):
    return [x for x in a if x not in b]

a = [1,2,3,4,2]
b = [2]

print ("List comprehension method")
print(array_diff_via_lc(a,b),'\n')

#it could be solved via set method, like this
#set([1,2,6,8]) - set([2,3,5,8])
# >> set([1, 6])

#but, set doesn not preserve the order of elements, and cause any duplicated elements to be removed. 
# The elements also need to be hashable. If these restrictions are tolerable, this may often be the simplest and highest performance option.

#set method
def array_diff_via_set(a,b):
    return set(a) - set(b)

print ("Set method")
print(array_diff_via_set(a,b),'\n')
