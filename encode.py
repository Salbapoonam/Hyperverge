def encode_word(word):
    if len(word) == 1:
        return str(ord(word)) + word
    elif len(word) == 3:
        return word[1] + word[0] + word[2]
    elif len(word) == 5:
        return word[2:] + word[:2]
    elif len(word) == 6:
        return word[::-1]
    else:
        return word

def process_file(filename):
    with open(filename, 'r+') as f:
        text = f.read()
        # Check if file is already encoded
        if text[0] == '$' and text[-1] == '$':
            # Decode file
            text = text[1:-1]
            words = text.split()
            decoded_words = [encode_word(word) for word in words]
            decoded_text = ' '.join(decoded_words)
            f.seek(0)
            f.write(decoded_text)
            f.truncate()
        else:
            # Encode file
            words = text.split()
            encoded_words = [encode_word(word) for word in words]
            encoded_text = ' '.join(encoded_words)
            f.seek(0)
            f.write('$' + encoded_text + '$')
            f.truncate()

process_file('input.txt')
