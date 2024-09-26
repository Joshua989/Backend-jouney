#word replacement program 
#user input sentence and want to replace a word in the sentence
#input sentence
inputSentence = input('enter a sentence: ')
print('your sentence is: ', inputSentence)
#input word to replace
wordToReplace = input('enter the word to replace: ')
#input word to replace with
wordToReplaceWith = input('enter the word to replace with: ')
#replace the word
print(inputSentence.replace(wordToReplace, wordToReplaceWith))

