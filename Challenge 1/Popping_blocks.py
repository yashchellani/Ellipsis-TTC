a = ['B', 'B', 'B', 'A', 'C', 'A', 'A', 'C']
b = [1, 1, 1, 1, 1]


def check_all_equal(array):
    count = 0
    num = array[0]
    for i in range(1, len(array)):
        if array[i] != num:
            count += 1

    return count

def popping2(array):
    if len(array) <= 1:
        print(array)
        return

    if len(array) % 2 == 0:
        result = check_all_equal(array)
        if result == 0:
            print([])
            return

    i = 1
    while i < len(array) - 1:
        #print(array)
        
        if array[i] == array[i - 1]:
            array = array[:i-1] + array[i+1:]
            #print(array)
            i = 1
        elif array[i] == array[i + 1]:
            array = array[:i] + array[i+2:]
            #print(array)
            i = 1
        else:
            i += 1
            
        #print(len(array))
        #print(i)
        #print(array)

    if len(array) == 2:
        if array[0] == array[1]:
            print([])
            return

    print(array)
   
print(popping2(a))
   
