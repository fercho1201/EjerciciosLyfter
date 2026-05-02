def sort_words(w):
    w_list = w.split("-")
    print (f'your given list is {w_list}')
    w_list.sort()
    sentence = '-'.join(w_list)
    return (f'this is the alphabetically sorted string: {sentence}')

word= 'casa-perro-gato-manzana-arbol'

print (sort_words(word))

words = ["I", "love", "Python"]
sentence = " ".join(words)

print(sentence)