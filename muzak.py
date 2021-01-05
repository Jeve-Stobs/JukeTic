import random
from replit import audio

genre = input(
    "1. Meglovania \n2. Gas Gas Gas\n3. DejaVu \n4. Running in the 90s\n5. Pigstep\n6. Never Gonna Give You Up\n Select your Music:"
)

if genre == "1":

    source = audio.play_file('Meglovania.mp3')
    print("Now Playing Meglovania, by Undertale. Enjoy Your Game!")

if genre == "2":

    source = audio.play_file('Gas.mp3')
    print("Now Playing Gas Gas Gas, by Initial D. Enjoy Your Game!")

if genre == "3":

    source = audio.play_file('DejaVu.mp3')
    print("Now Playing Deja Vu, by Initial D. Enjoy Your Game")

if genre == "4":

    source = audio.play_file('Running.mp3')
    print(
        "Now Playing Running in the 90s, by Maurizio De Jorios. Enjoy Your Game!"
    )

if genre == "5":

    source = audio.play_file('pigstep.mp3')
    print("Now Playing Pigstep, by Lena Raine. Enjoy Your Game!")

if genre == "6":
  source = audio.play_file('Never.mp3')
  print("Now playing Never Gonna Give You Up, by Rick Astley")