import random 

def move_pointer(text, position):
    # Print the text
    print(text)
    # Create a string of spaces to align the '^' with the desired 
    # position
    pointer_line = " " * position + "^"
    # Print the pointer line
    print(pointer_line)

wordlist= ["algorithm", 
    "function", "variable", "compile", "iterate", 
    "recursion", "binary", "array", "syntax",
    "pointer"]

while True:
 r = random.randint(0, len(wordlist)-1)
 selected_word = wordlist[r]

 title = 'HANGMAN'
 move_pointer(title, 0)
 k = 1 
 i = 0
 while i<len(selected_word):
   guess = str(input('your guess: '))
   if len(guess) > 1:
    print('Guess only  single letter') 
   else:
    if guess == selected_word[i]:
     print(selected_word[i])
     i += 1
    else:
     move_pointer(title,k)
     print('wrong')
     k +=1
   if k == 7:
     print('You are hanged')
     break;


   if(i == len(selected_word) ):
     print('You are safe')

 code = input('you want to play again: (y/n): ')
 if code.lower()=='n':
   break
 else:
   continue

