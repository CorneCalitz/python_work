def Min_(list_num):
    if len(list_num) == 1:
        return list_num[0]
    else:
        m = Min_(list_num[1:])
        if m < list_num[0]:
            return m
        else:
            return list_num[0]

def Max_(list_num):
    if len(list_num) == 1:
        return list_num[0]
    else:
        m = Max_(list_num[1:])
        if m > list_num[0]:
            return m
        else:
            return list_num[0]
       

nums = [1, 3, 5, 6, 2]

print(f'min: {Min_(nums)}\t max: {Max_(nums)}')
