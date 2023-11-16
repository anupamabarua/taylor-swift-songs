from random import randint

try:
    file = open("songs.dat")
except:
    print("no songs.dat file found")

songs = file.read().splitlines()

for song in range(len(songs)):
    songs[song] = songs[song].split()

while True:
    while True:
        ask = input("\nDo you want a random Taylor Swift song (y/n)? ")
        if ask.lower() == "yes" or ask.lower() == "y" or ask.lower() == "no" or ask.lower() == "n":
            break
    if ask.lower() == "yes" or ask.lower() == "y":
        indx = randint(0, len(songs)-1)
        print(f'{songs[indx][0].replace("-", " ")} is from the album {songs[indx][1].replace("-", " ")}, and was made in {songs[indx][2]}.')
    else:
        print()
        break
