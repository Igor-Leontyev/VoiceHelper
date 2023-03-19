# -*- coding: utf-8 -*-


import speech_recognition
import os
import random
import pyglet
import pyautogui as pg


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

is_music = True

pg.FAILSAFE = False


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            querry = sr.recognize_google(
                audio_data=audio, language='ru-RU').lower()
        return querry
    except speech_recognition.UnknownValueError:
        return 'Не понял чё ты сказал:/'


def greeting():

    return 'Привет !'


def create_task():
    print("какие дела запишем?")
    querry = listen_command()
    with open('todo-list.txt', 'a', encoding='utf-8') as file:
        file.write(f'-- {querry}\n')
    return f'Задача {querry} добавлена в список'


def play_music():
    if is_music:
        song = pyglet.resource.media('music/Roy Jones Jr.mp3')
        song.play()
        pyglet.app.run()
        return f'Танцуй под Roy Jones Jr'
    else:
        print('музыка выключена')
        return


def off_pc():
    os.system("shutdown /s /t 2")


def open_broweser():
    pg.move(701, 1050, 0.2)
    pg.click(701, 1050)


def main():
    while True:
        querry = listen_command()
        if querry == 'привет':
            print(greeting())
        elif querry == 'добавить задачу':
            print(create_task())
        elif querry == 'включи музыку':
           
            print(play_music())
            
        elif querry == 'выключи музыку':
            is_music = False
        elif querry == 'выключи комп':
            print(off_pc())
        elif querry == 'перестань':
            print('отключаюсь')
        elif querry == 'открой браузер':
            print(open_broweser())
            break
        else:
            print('Как жизнь ?')


if __name__ == '__main__':
    main()
