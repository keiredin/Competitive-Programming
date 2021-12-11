def sortSentence(s):
    listOfWords = s.split(' ')
    sortedS = s.split()
    result = []
    for word in listOfWords:
        wordIndex = listOfWords.index(word)
        n = word[-1]
        numberIndex = int(n)
        sortedS[numberIndex -1] = word
        # listOfWords[numberIndex-1],listOfWords[wordIndex] = word,listOfWords[numberIndex-1]

    for i in sortedS:
        result.append(i[:-1])
    s = ' '.join(result)    
    return s


print(sortSentence("KTFkUVVrmYMSo2 wXlQraUqblfhCfDLK3 IfTuftYVualQ6 NhpQ5 HlRjClVtQrTFcwbx4 fi1"))