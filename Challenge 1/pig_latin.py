def translate_sentence(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    words = []

    current = ""
    for i in range(len(sentence)):
        if sentence[i].isalnum():
            current += sentence[i]
        else:
            words.append(current)
            current = ""
            current += sentence[i]

            if current == " ":
                words.append(current)
                current = ""

            elif i == len(sentence) - 1:
                words.append(sentence[i])
                
    modified = []
    for i in range(len(words)):
        modified.append(translate_word(words[i]))

    for i in range(len(modified)):
        if modified[i].isalpha():
            for j in modified[i]:
                if j.isupper():
                    modified[i] = modified[i].capitalize()
                    break
    sentence2 = ""
    for i in modified:
        sentence2 += i

    return sentence2
    
def translate_word(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if word.isalpha() != True:
        return word

    count = 0
    while count < len(word) and word[0] not in vowels:
        word = word[1:] + word[0]
        count += 1
    if count == 0 and word[0] in vowels:
        word += "yay"
    else:
        word += "ay"
    return word

def translate(eng_word):
    if eng_word.isalpha():
        return translate_word(eng_word)

    return translate_sentence(eng_word)


print(translate("Do you like me?"))



    
