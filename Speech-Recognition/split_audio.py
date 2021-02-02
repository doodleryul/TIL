from pydub import AudioSegment
from os import listdir
from os.path import isfile, join
import os
from tqdm import tqdm

def split_sound(filepath, savepath):
    '''
    1. Make directory
    2. Start cut sound
    3. export cut sound file
    '''
    files = [f for f in listdir(filepath) if isfile(join(filepath, f))]
    
    try:
        if not os.path.exists(savepath):
            os.makedirs(savepath)
            print('Create directory for cut audio')
    except OSError:
        print('Error: Creating directory')

    for idx in tqdm(range(len(files))):
        sound = AudioSegment.from_file('{}/{}'.format(filepath, files[idx]))
        n = len(sound) // 18000 #cut 20sec
        cut_len = len(sound) // n

        for i in range(n):
            if i <= n-1:
                sound_cut = sound[cut_len*(i):cut_len*(i+1)]
            else:
                sound_cut = sound[cut_len*(i):]
            sound_cut.export('{}/{}_{}.wav'.format(savepath, files[idx].split('.')[0], i), format='wav')
