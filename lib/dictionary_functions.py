import string

def word_frequency(sentence):
    word_dict = {}
    translator = str.maketrans("", "", string.punctuation)

    words = sentence.translate(translator).lower().split()

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict
