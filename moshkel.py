import random
words=["apple","chest","book","monkey","donkey","umbrella","war","road","car","note book","workbook","choice"]
#i=random.randit(0,len(words)-1)
#word=word[i]
i=()
word=random.choice(words)#clock

while True:
    print('- ' * len(word))# - - - - - 
    a=input()
    if  a in  word:
       word[i]=a
