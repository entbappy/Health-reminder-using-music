#Imported some significant modules
from pygame import mixer
from datetime import datetime
from time import time

def music_function(music_file,stop_command):
    '''
    This is a function for play Music
    '''
    mixer.init()
    mixer.music.load(music_file)
    mixer.music.play()
    while True:
        user = input("Enter:")
        if user == stop_command:
            mixer.music.stop()
            break

def mylog_function(msg):
    '''
    This function for log my response
    '''
    with open("myLog.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == "__main__":
    
    #For getting seconds
    init_water = time()
    init_eyes = time()
    init_ex = time()
    
    #Setting the actual times
    water_sec = 40*60
    eyes_sec = 30*60
    ex_sec = 45*60

    while True:
        if time() - init_water > water_sec:
            print("Drink Water Sir..!   Write 'd' to stop the music.")
            music_function("waters.mp3","d")
            init_water = time()
            mylog_function("Drank water at")

        if time() - init_eyes > eyes_sec:
            print("Relax your eyes Sir..!   Write 'e' to stop the music.")
            music_function("eyes.mp3","e")
            init_eyes = time()
            mylog_function("Relaxed eyes at")

        if time() - init_ex > ex_sec:
            print("Do Exercise Sir..!   Write 'ex' to stop the music.")
            music_function("excercise.mp3","ex")
            init_ex = time()
            mylog_function("Exercise did at")








    # print("Everything is ok!!")