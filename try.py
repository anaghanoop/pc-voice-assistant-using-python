import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
url = "http://api.openweathermap.org/data/2.5/weather?q=chennai&appid=e8a3a523e79023d08279bb463b488ab1"
response = requests.get(url)
data = response.json()
current_temperature = data["main"]["temp"]
T_1=current_temperature-273.15
t_1=round(T_1,2)
cur_temp_feels = data["main"]["feels_like"]
T_2=cur_temp_feels-273.15
t_2=round(T_2,2)
max_temp=data["main"]["temp_max"]
T_3=max_temp-273.15
t_3=round(T_3,2)
min_temp=data["main"]["temp_min"]
T_4=min_temp-273.15
t_4=round(T_4,2)
speak(f"in chennai the current temprature is {t_1} degree celsius , it feels like{t_2} degree celsius , and the maximum temprature is{t_3} degree celsius, and the minimum temprature is {t_4} degree celsius")
