import random 
import string 
import youtube_dl
import os 
from scipy.io import wavfile
import argparse
import numpy as np 

"""
    step 1: Download and convert
    Step 2: Read and generate
"""
def gen_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,  # only keep the audio
    'audioformat': "wav",  # convert to wav
    'outtmpl': 'download.wav',
}

def download_mp3_youtube_from_url(url):
    buff_file = "{}.wav".format(gen_name())
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        os.system("""
        ffmpeg -y -i download.wav -acodec pcm_s16le -ar 16000 -ac 1 -f wav {}""".format(buff_file))
        os.remove("download.wav")
        return buff_file
    except:
        return ""

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-sp', '--save_path', default='./not-wakeword')
    parser.add_argument('-n', '--num_sample', default=100)
    parser.add_argument('-r', '--ratio', default=0.033)
    args = parser.parse_args()

    save_path = args.save_path
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    num_sample = int(args.num_sample)
    with open("url.txt", "r") as f:
        urls = [i.strip() for i in f.readlines()]

    with open("used_urls.txt", "r+") as used_f:
        used_urls = [i.strip() for i in used_f.readlines()]
    
    print("All: ", len(urls))
    urls = [i for i in urls if i not in used_urls]
    print("After: ", len(urls))

    print(len(urls), urls[0])
    iter = 1
    while(num_sample>=iter):
        filename = download_mp3_youtube_from_url(urls[0])
        if filename:
            r, data = wavfile.read(filename)
            num_slicing = len(data)//1600
            num_saving = round(num_slicing * float(args.ratio))
            saving_index = np.random.choice([i for i in range(num_slicing)], size=num_saving, replace=False)
            print(num_saving)
            for i in saving_index:
                wavfile.write(os.path.join(save_path, 'not_nachimo_{}.wav'.format(iter)), 16000, data[i*1600: i*1600 + 16000])
                iter += 1
                if iter >= num_sample: break
            with open("used_urls.txt", "a") as used_f:
                poped_url = urls.pop(0)
                print("="*10, poped_url)
                used_f.write(poped_url+'\n')
            os.remove(filename)
    print("Done! ", len(os.listdir(save_path)))
