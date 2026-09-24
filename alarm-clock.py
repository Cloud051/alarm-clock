from tkinter import *
import datetime
import time
from threading import *
from pygame import mixer

root = Tk()
root.geometry("560x320")

def Threading():
    t = Thread(target=alarm)
    t.start()

def alarm():
    while True:
        set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm)
        
        if current_time == set_alarm:
            print("Wake up!")
            mixer.init()
            mixer.music.load("bro.wav")
            mixer.music.play(-1)
            break

def stop_alarm():
    mixer.music.stop()
    print("5 more minutes...")

Label(root, text="Alarm Clock", font=("sans-serif", 20, "bold"), fg="purple").pack(pady=10)
Label(root, text="Set Time", font=("sans-serif", 16, "bold"), fg="black").pack()

frame = Frame(root)
frame.pack(pady=10)

hour = StringVar(root)
hours = (
    '00',
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24'
)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = (
    '00',
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31',
    '32',
    '33',
    '34',
    '35',
    '36',
    '37',
    '38',
    '39',
    '40',
    '41',
    '42',
    '43',
    '44',
    '45',
    '46',
    '47',
    '48',
    '49',
    '50',
    '51',
    '52',
    '53',
    '54',
    '55',
    '56',
    '57',
    '58',
    '59',
    '60'
)
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = (
    '00',
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31',
    '32',
    '33',
    '34',
    '35',
    '36',
    '37',
    '38',
    '39',
    '40',
    '41',
    '42',
    '43',
    '44',
    '45',
    '46',
    '47',
    '48',
    '49',
    '50',
    '51',
    '52',
    '53',
    '54',
    '55',
    '56',
    '57',
    '58',
    '59',
    '60'
)
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("sans-serif", 16, "bold"), command=Threading).pack(pady=10)
Button(root, text="Stop", font=("sans-serif", 16, "bold"), command=stop_alarm).pack(pady=10)

root.mainloop()
