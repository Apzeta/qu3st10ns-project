from gtts import gTTS
import os

# Open the text file
with open('/home/samsepi01/Desktop/responses.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Create a gTTS object with the text
tts = gTTS(text=contents, lang='en')

# Save the speech as an MP3 file
tts.save('output.mp3')

# Play the speech using the default media player
os.system('xdg-open output.mp3')  # for Linux
# os.system('start output.mp3')  # for Windows

