def hangman():
       from random import choice
       #Enter any word you like
       wordlist=['god','developer','dinosaur','vivo','school','king','queen','speed']
       a=choice(wordlist)
       blank=[]
       word=[]
       count=1
       for letter in a:
              word.append(f'{letter}')
       for _ in range(len(word)):
              blank.append("_")
       while True:
              for l in blank:
                     print(l,end="")
              print()             
              w=input("Enter a letter :")
              k=0
              for i in word:
                     if i==w:
                            blank[k]=word[k]
                     k=k+1    
              count=count+1
              print("Attempts :",count)
              print()
              p=0
              for s in blank:
                     if  s != '_' :
                            p=p+1
              if p==(len(word)):
                     for l in blank:
                            print(l,end="")
                     print()             
                     print("*** You Won ***")
                     break


hangman()













































