from pydub import AudioSegment
import tkinter as tk
import os
import tkinter.font as tkFont
import ntpath
from tkinter.filedialog import askdirectory
def TruncateFile(inputLocation, outputLocation):
    print("Received:" + inputLocation);
    song = AudioSegment.from_mp3(inputLocation)
    length = len(song)
    newLength = length / 3
    truncated = song[:newLength]
    truncated.export(outputLocation, format="mp3")

def trimAlbum(foldername):
    trimmedPath = foldername + "/trimmed"
    if (not os.path.isdir(trimmedPath)):
        os.mkdir(trimmedPath)
    for filename in os.listdir(foldername):
        if filename.endswith(".mp3"):
            inputPath = foldername + "/" + filename
            outputPath = trimmedPath + "/" + filename
            print("Output: " + outputPath)
            print("Input: " + inputPath)
            print("Filename: " + filename)


            TruncateFile(inputPath, outputPath);
def onTrimPress():
    print('Pressed')
    foldername = askdirectory()



    print(foldername)
    for filename in os.listdir(foldername):
        filePath = foldername + "/" + filename
        if os.path.isdir(filePath):
            trimAlbum(filePath)
        else:
            if filename.endswith(".mp3"):
                trimmedPath = foldername + "/trimmed"
                if (not os.path.isdir(trimmedPath)):
                    os.mkdir(trimmedPath)
                inputPath = foldername + "/" + filename
                outputPath = trimmedPath + "/" + filename
                print("Output: " + outputPath)
                print("Input: " + inputPath)
                print("Filename: " + filename)

                TruncateFile(inputPath, outputPath);



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


