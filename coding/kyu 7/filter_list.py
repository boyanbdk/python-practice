def filter_list(l):
    return list(filter(lambda x: not isinstance(x,str), l))

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))