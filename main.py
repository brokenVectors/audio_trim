from pydub import AudioSegment
import tkinter as tk
import os
import tkinter.font as tkFont
from tkinter.filedialog import askdirectory

def onTrimPress():
    print('Pressed')
    filename = askdirectory()
    os.mkdir("songs")
def tkLoop():
    root.geometry("200x100")
    root.resizable(0, 0)
    truncateButton = tk.Button(root, text="Trim MP3...", command = onTrimPress)
    title = tk.Label(root, text="The Trimmer", font=fontStyle)
    truncateButton.pack(side = tk.BOTTOM);
    title.pack(side = tk.TOP);
    title.configure(anchor="center")



root = tk.Tk()
fontStyle = tkFont.Font(family="Corbel Light", size=16)
tkLoop()
root.mainloop()
def TruncateFile(inputLocation, outputLocation):

    song = AudioSegment.from_mp3(inputName)
    length = len(song)
    newLength = length / 3
    truncated = song[:newLength]
    truncated.export(outputName, format="mp3")

