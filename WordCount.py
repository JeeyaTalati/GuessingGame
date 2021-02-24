def countWordsFromFile():
    fileName=input(str("Enter The File Name"))
    wordCount=0
    file=open(fileName,"r")
    for line in file:
        words=line.split()
        wordCount=wordCount+len(words)
    print(wordCount)
countWordsFromFile()