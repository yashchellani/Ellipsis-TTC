import random

def createSubstrings(s):
    #print(string)
    us = set(); 
    for i in range(len(s)):
        # One by one generate subStrings ending 
        # with s[j] 
        ss = ""
        for j in range(i, len(s)): 
            ss = ss + s[j]
            us.add(ss)
    return len(us)
       
print(createSubstrings("aaaa"))


def countSubstrings(string, queries):
    allQueries = []
    for query in queries:
        allQueries.append(query)
    for i in range(len(queries)):
        #print(queries[i])
        #print(string[queries[i][0]:queries[i][1]+1])
        number = len(createSubstrings(string[queries[i][0]:queries[i][1]+1]))
        print(number)

#countSubstring("aaaaa", [[1, 1], [1, 4], [1, 1], [1, 4], [0, 2]])


