from gtts import gTTS
text = "Hi, I am Gowshika, what's your name and where are you from?"
tts = gTTS(text=text)
tts.save("sample.mp3")
print("Output saved as sample.mp3")