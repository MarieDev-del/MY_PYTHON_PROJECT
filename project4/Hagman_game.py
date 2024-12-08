import random
Word_list = ['Onomatopeia','Quixotic','Ubiquitous','Sycophant','Auspicious','Ebullient']
live=6
Chosen_word = random.choice(Word_list)
display_list=[]
for char in Chosen_word:
    display_list+='_'
display=' '
for i in display_list:
    display+='_'
print(display) 

game_over = False
while not game_over:
    Guess_letter = input("Guess a letter: ").lower()
    for i in range(len(Chosen_word)):
        i = Chosen_word[i]
        if i==Guess_letter:
            display[i]=Guess_letter
    print(display)
if Guess_letter not in Chosen_word:
    live-=1
    if live==0:
        game_over=True
        print("You lose")
if '-' not in display:
    game_over = True
    print("You Won")
