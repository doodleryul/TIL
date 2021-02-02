from os import listdir
from os.path import isfile, join
import speech_recognition as sr
import sys


# Reading Audio file as source
# listening the audio file and store in audio_text variable

def stt(file_path, wave_file):
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    with sr.AudioFile('{}/{}'.format(file_path, wave_file)) as source:
        audio_text = r.listen(source)
      
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text, language="ko-KR")
        print('{}, {}'.format(wave_file, text))
      
    except:
        print('{}, failed'.format(wave_file))


# Run
# file path
file_path = 'audio files directory'
# Save to file_list
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

sys.stdout = open('save_result_file.txt', 'w')
for wav in files:
    stt(file_path, wav)
