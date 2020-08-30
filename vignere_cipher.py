def vigenere_encrypt(plaintext, codeword):
    symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    code=""
    translated=""
    if len(codeword)>len(plaintext):
        for i in range(len(plaintext)):
            code+=(codeword[i])

    elif len(codeword)<len(plaintext):
        folds=len(plaintext)/len(codeword)
        codeword*=(folds+1)
        for i in range(len(plaintext)):
            code+=(codeword[i])
    
    else:
        code=codeword
    
    for letter, k in zip(plaintext, code):
        key=symbols.find(k)
        if letter in symbols:
            letterIndex=symbols.find(letter)
            translated+=symbols[(letterIndex+key)%26]

    print(translated)
    
vigenere_encrypt("ATTACKATDAWN","LEMON")
