import random
word_list=['Hangman',
'Acrobat',
'Microbiology',
'Experiment',
'Psychology',
'Random']


guessed= False
orig=random.choice(word_list).upper()
x=list(orig)
prot='*'*len(x)
prot=list(prot)
i=0
no=len(x)
ind=0
attempts=len(x)+3
while(i<attempts):
    guess1= False
    str1=''
    str1=str1.join(prot)
    while True:
        try:
            inp=input("Guess an alphabet:\n").upper()
            if len(inp)==1:
                break
            else:
                raise "Enter a single alphabet"
        except:
            print("Enter a single alphabet")
    j=0
    while(j<len(x)):
        if x[j]==inp:
            prot[j]=inp
            guess1=True
        j=j+1

    '''ind=orig.find(inp)
    if ind==-1:
        print("Wrong answer")
    else:
        if(str1.find(inp)!=-1):
            ind=orig[str1.find(inp):].find(inp)
            if ind==-1:
                print("Wrong answer")
                continue
        prot[ind]=inp
        str1=''
        str1=str1.join(prot)
        print(str1)'''
    if guess1==True:
        str3=''
        str3=str3.join(prot)
        print(str3)
    else:
        print("Wrong answer")

    i=i+1
    att=attempts-i
    if prot==x:
        guessed= True
        break
    print("Attempts remaining= ",att)
str2=''
str2=str2.join(prot)

if guessed:
    print("You guessed the word!!!!!!")
else:
    print("You lose!")
