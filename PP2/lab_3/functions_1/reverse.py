sentence = input()


def reverser (sentence):

    words = []
    words = sentence.split()

    reversed_words = words[::-1]

    return " ".join(reversed_words) #join makes it possible to put space between elements of set as it doesn't put space in the beginning and at the end of a sentence 

    
result = reverser(sentence)

print (result)
