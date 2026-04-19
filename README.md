# Text to Speech Converter using gTTS

This is a simple Python project that converts text into speech using the Google Text-to-Speech (gTTS) library. The output is saved as an MP3 audio file.

## 🚀 Features
- Converts text into speech
- Saves output as an MP3 file
- Easy to use and lightweight

## 🛠️ Technologies Used
- Python 3
- gTTS (Google Text-to-Speech)

## 📦 Installation

1. Clone the repository or download the files
2. Install required dependencies:

```bash
pip install -r requirements.txt
▶️ How to Run

Run the Python script:

python main.py

After running, an audio file named sample.mp3 will be created in the project folder.

📌 Example Code
from gtts import gTTS

text = "Hi, I am Gowshika, what's your name and where are you from?"
tts = gTTS(text=text)
tts.save("sample.mp3")

print("Output saved as sample.mp3")
🎧 Output
A file named sample.mp3 will be generated and can be played using any media player.
