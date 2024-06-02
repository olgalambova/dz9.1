def popular_words (text, words):
    d = {}
    for word in text.split():
        word = word.lower()
        if word in words:
            d[word] = d.get(word, 0) + 1
    else:
        for w in words:
            if w not in d:
                d[w] = 0
    return d
print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))

#assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1' print('OK')
