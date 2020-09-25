
if len(arr) <= 1:
    return arr
else:
    currentLetter = arr[0]
    found = False
    for i in range(1,len(arr)-1):
        while arr[i] == currentLetter:
            if arr[i] != currentLetter:
                break
            else:
                found = True
                i += 1
        if found == True:
            pass


