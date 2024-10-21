import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random 

print ("Players stand")
sleep_time = random.randrange(10, 26)

sat_down_players = []

start_time = time.time()

while time.time() - start_time < sleep_time:
    name = input("Enter name of player who sat down: ")
    if name:
        sat_down_players.append(name)
 
print("Time is up! Here are the players who sat down:")
print(sat_down_players)

winner = sat_down_players[-1]
print(f"The winner is: {winner}!")

