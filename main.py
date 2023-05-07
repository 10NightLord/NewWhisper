import pytube
from moviepy.editor import VideoFileClip
import pywhisper
import os
import static_ffmpeg
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def convert_to_mp3(filename):
    print("iniciando processo de recebimento de video!")
    clip = VideoFileClip(filename)
    print(" processamento de video finalizado!")
    audio = clip.audio.write_audiofile(filename.replace(".mp4",".mp3"))
    print('processo do audio concluido!')
    clip.close()
    return audio

def AudiotoText(filename):
    model = pywhisper.load_model("base")
    result = model.transcribe(filename)
    print(result["text"])
    sonuc = result["text"]
    return sonuc

def main(video, model):
    print('''
    This tool will convert .mp4 videos to mp3 files and then transcribe them to text using Whisper.
    ''')
    print("Começando app... " )
    print("MODEL: " + model)
    # FFMPEG installed on first use.
    print("Initializing FFMPEG...")
    static_ffmpeg.add_paths()

    audio = None
    print("loading video... Please wait.")
    try:
        print("video was loaded as: sucess! ")
    except:
        print("Not a valid file..")
        return
    try:
        
        audio = video.audio
        if audio is not None:
            audio.write_audiofile('audiofile.mp3')
            print(f"a conversao do arquivo foi um sucesso")
    except:
        print("Error converting video to mp3")
        return
    try:
        mymodel = pywhisper.load_model(model)
        result = mymodel.transcribe('audiofile.mp3')
        print(result["text"])
        result = result["text"]
        video.close()
        os.remove('temp_video.mp4')
        os.remove('audiofile.mp3')
        print("Removed video and audio files")
        print("Done!")
        return result
    except Exception as e:
        print("Error transcribing audio to text")
        print(e)
        return
    

if __name__ == "__main__":
    main()
