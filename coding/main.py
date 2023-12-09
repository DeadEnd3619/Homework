class CaesarCipher:
    def __init__(self):
        pass
    
    def encrypt(text, shift):
        characters = ["a","b","c","d","e","f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", 't', 'u', "v", "w", "x", "y", "z"]
        i = 0 
        output = ""
        value = len(text)
        while i < value:
            if text[i] == ' ':
                output += ' '
            else:
                x = characters.index(text.lower()[i]) + shift
                if x > 26:
                    x -= 26
                output += characters[x]
            i += 1

        print(output)


    def decrypt(text,shift):
        characters = ["a","b","c","d","e","f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", 't', 'u', "v", "w", "x", "y", "z"]
        i = 0 
        output = ""
        value = len(text)
        while i < value:
            if text[i] == ' ':
                output += ' '
            else:
                x = characters.index(text.lower()[i]) - shift
                output += characters[x]
            i += 1

        print(output)



CaesarCipher.encrypt("Hello my friend", 3)
CaesarCipher.decrypt("khoor pb iulhqg", 3)























































































