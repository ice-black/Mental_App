from tkinter import filedialog
import whisper


filetypes = [("Audio Files", "*.mp3;*.wav;*.ogg;*.flac;*.aac")]
file_path = filedialog.askopenfilename(filetypes=filetypes)
print(file_path)

model = whisper.load_model("base")

result = model.transcribe(rf"{file_path}")
print(result["text"])

help(file_path)