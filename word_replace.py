def word_replace():
    sentence="Hi guys,i am learning coding with Python."
    word_replace=input("Enter the word to replace:")
    word_replacement=input("Enter the word to replacement:")
    sentence=sentence.replace(word_replace,word_replacement)
    print(sentence)

word_replace()