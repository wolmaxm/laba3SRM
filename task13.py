list1 = ['KPI','FICE','candicii', 'Kyiv','Khust']
list2 = ['chicken', 'candicii', 'Kyiv', 'Maksym', 'Khust']

def words(list1, list2):
    new = list(set(list1) ^ set(list2))
    return new

result= words(list1,list2)
print(result)
