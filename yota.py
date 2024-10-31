import speech_recognition
import webbrowser
import os
import wikipedia
import datetime
from sp import speak
from rot13 import rot13


sr = speech_recognition.Recognizer() # Создаем объект SR

# Текущие доступные команды #
questions_dic = {'commands': {
    'hi' : ['привет', 'хай', 'приветик', 'прив', 'прувит'],
    'user' : ['стёпа', 'степан', 'степа', 'степ', 'стёп', 'помощник стёпа', 'помощник степа'],
    'shutka' : ['шутку', 'расскажи шутку', 'пошути', 'шутка', 'рассмеши меня', 'рассмеши'],
    'other_commands' : {
        'browser' : ['открой браузер', 'браузер', 'хром', 'открой хром'],
        'music' : ['музыка', 'открой музыку', 'музыка', 'музыку', 'включи музыку', 'мюзика', 'music', 'поставь музыку'],
        'task' : ['блокнот', 'блакнот', 'открой блокнот', 'заметки', 'открой заметки'],
        'create task': ['создай заметку', 'создать заметку', 'новая заметка'],
        'add task': ['добавь заметку', 'добавь к заметке', 'напиши заметку', 'нужно записать', 'запиши заметку'],
        'save_audio' : ['сохрани звук', 'запиши звук', 'запиши на диктофон', 'включи диктофон'],
        'tg' : ['телеграм', 'открой телеграм', 'тг', 'телеграмм', 'запусти телеграм'],
        'yt' : ['ютюб', 'youtube', 'ютуб', 'скачай видео', 'скачать видео', 'скачай видео с ютуба', 'скачай видео с ютуб', 'скачай видео с youtube'],
        'wiki' : ['википедия', 'что такое', 'что значит', 'найди', 'распознай'],
        'time' : ['время', 'какое время', 'какое сейчас время', 'текущее время', 'текущий час', 'какой час'],
        'dt' : ['дата', 'число', 'какое сейчас число', 'какая сегодня дата', 'какая дата'],
        'rot13' : ['зашифруй', 'создай шифр', 'зашифруй текст', 'шифр текста'],
        'al' : ['алиса', 'запусти алису', 'нужна алиса', 'алиса лучше', 'алису'],
        'rot13_2' : ['расшифруй', 'нужно расшифровать', 'расшифровать']

    }
}}


# Функция для прослушивания задачи и обработки задачи
def listen(txt):
         with speech_recognition.Microphone() as micro:
             sr.adjust_for_ambient_noise(source = micro, duration = 0.5)
             audio = sr.listen(source = micro)
             txt = sr.recognize_google(audio_data = audio, language = 'ru-RU').lower()

             main(txt) # Передаем в main, где будем обрабатывать саму команду

def main(txt):
    # Куча if else просто чекаем где может быть то, что сказал человек
    if txt in questions_dic['commands']['hi']:
        speak('Приветствую')

    elif txt in questions_dic['commands']['user']:
        speak('Слушаю вас')

    elif txt in questions_dic['commands']['shutka']:
        speak('Искусственный интелект скоро захватит мир! Теперь думайте, шутка это или нет.')

    elif txt in questions_dic['commands']['other_commands']['browser']:
        speak('Выполняю')
        webbrowser.open('https://www.google.ru')

    elif txt in questions_dic['commands']['other_commands']['music']:
        speak('Потанцуем!')
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PotPlayer\PotPlayer 64 bit.lnk")

    elif txt in questions_dic['commands']['other_commands']['create task']:
        speak('Скажите что нужно записать...')
        with speech_recognition.Microphone() as micro:
            sr.adjust_for_ambient_noise(source = micro, duration = 0.5)
            audio = sr.listen(source = micro)
            txt = sr.recognize_google(audio_data = audio, language = 'ru-RU').lower()
            with open('user.txt', 'w', encoding = 'utf-8') as file:
                 file.write(f'{txt}\n')
        speak('Заметка создана')

    elif txt in questions_dic['commands']['other_commands']['add task']:
        speak('Что нужно записатььь...')
        with speech_recognition.Microphone() as micro:
            sr.adjust_for_ambient_noise(source = micro, duration = 0.5)
            audio = sr.listen(source = micro)
            txt = sr.recognize_google(audio_data = audio, language = 'ru-RU').lower()
            with open('user.txt', 'a', encoding = 'utf-8') as file:
                 file.write(f'{txt}\n')
        speak('Добавлено к заметкаммм!')

    elif txt in questions_dic['commands']['other_commands']['wiki']:
        wikipedia.set_lang('ru')
        res = wikipedia.summary(txt, sentences = 2)
        speak(res)


    # Тут ты должен подстроить под себя, указать пути со своего компьютера
    # ---------------------------------------------------------------------------------------------------------------------------------- #

    # elif txt in questions_dic['commands']['other_commands']['tg']:
    #     speak('Выполняю...')
    #     os.startfile(r"C:\Users\TM\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk") 

    # elif txt in questions_dic['commands']['other_commands']['yt']:
    #     speak('Принято, выполняю...')
    #     speak('Запускаю вашу программу которая даже не оптимизирована и всегда зависает ха-ха-ха...')
    #     os.startfile(r'C:\Users\TM\Desktop\Files\youtube.py')

    # ---------------------------------------------------------------------------------------------------------------------------------- #

    elif txt in questions_dic['commands']['other_commands']['time']:
        time = datetime.time()
        print(time)

    elif txt in questions_dic['commands']['other_commands']['dt']:
        dt = datetime.date()
        print(dt)

    elif txt in questions_dic['commands']['other_commands']['rot13']:
        speak('Чтобы сохранить конфиденциальность советую записать текст который хотите зашифровать, или вы хотите чтобы все слышали какой текст вы шифруетеее?')
        rt = input('Введите текст для шифра: ')
        rt = rot13(rt)
        with open('user.txt', 'a', encoding = 'utf-8') as file:
            file.write(f'{rt}\n')
        speak('Готово! Проверьте ваши заметки.')

    elif txt in questions_dic['commands']['other_commands']['al']:
        speak('Ага но кто такая Алиса? Может лна устаревший инструмент или старый компьютеррр?')

    elif txt in questions_dic['commands']['other_commands']['rot13_2']:
        speak('Введите зашифрованный текст а я постараюсь расшифровать...')
        t = input('Текст: ')
        t = rot13(t)
        speak('Готово, спасибо за ожидание')
        print(t)

    else:
        speak('Пока не могу отвечать на такие запросы...')



txt = ''
def listen2():
        while txt.lower() != 'конец работы':
            listen(txt)
try:
    speak('Йота вас приветствуетт')
    listen2()

except speech_recognition.UnknownValueError:
    listen2()