def count_chars(text):
    return len(text)

def count_words(text):
    count = 0
    
    if text == '':
        return count
    
    for x in range (len(text)):
        if text[x] == ' ':
            count += 1
    return count + 1