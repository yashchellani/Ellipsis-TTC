def popping(a):
    if a == []:
        return a
    
    capacity = len(a)
    top = 0
    items = [None] * capacity

    for i in range(len(a)):
        if top == 0:
            items[top] = a[i]
            top += 1
            #print(items)
        else:
            if a[i] == items[top - 1]:
                items[top - 1] = None
                top -= 1
                #print(items)
            else:
                items[top] = a[i]
                top += 1
                #print(items)

    result = []
    for i in range(len(items)):
        if items[i] != None:
            result.append(items[i])
            
    return result
