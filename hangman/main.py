import random
import life_art
import random_word

print(life_art.logo)

chosen_word = random.choice(random_word.word_list)
players_life = 6;

player_alife = True

array_word = []

for letter in chosen_word:
    array_word.append(letter)
 
# print(array_word.index('w'))

dashes = []
for _ in range(len(chosen_word)):
    dashes.append("_")
while player_alife == True:
    print(dashes)
    print(life_art.stages[players_life])
    guess = input("Please Guess a letter: ").lower()
    if dashes.count("_") > 0:

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                dashes[position] = letter

        if array_word.count(guess) < 1:
            players_life -= 1
            if players_life == 0:
                print("Game Over, you loose😢")
                print(f"Answer was {chosen_word}")
                player_alife = False
                
        
    elif dashes.count("_") > 0 and players_life <= 0:
        print("Game Over, you loose😢")
        player_alife = False
    else: 
        players_life = 0
        print("Game Over, you won🎉")
        player_alife = False


# dashes = []
# for _ in range(len(chosen_word)):
#     dashes.append("_")
    
# if dashes.count("_") > 0:
#     while players_life > 0:

#             guess = input("Please Guess a letter: ").lower()

#             for position in range(len(chosen_word)):
#                 letter = chosen_word[position]
#                 if letter == guess:
#                     dashes[position] = letter

#             if array_word.count(guess) < 1:
#                 print("Not found in index")
#                 players_life -= 1
# else: 
#     print("Game Over, you won🎉")
            
# print(dashes)
# print(life_art.stages[players_life])
