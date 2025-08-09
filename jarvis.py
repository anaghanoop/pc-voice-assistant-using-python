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

# Function to wish the user based on the time of the day
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening!")
    speak("I am Jarvis, sir. Please tell me how may I help you?")

# Function to take voice command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        listening_label.config(text="Listening...", fg="white")
        listening_label.grid(row=1, column=0, columnspan=2, pady=(10, 0))  # Make the label visible  # Update listening label
        root.update_idletasks()  # Update the GUI
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        recognizing_label.config(text="Recognizing...", fg="white")
        recognizing_label.grid(row=1, column=0, columnspan=2, pady=(10, 0))  # Update recognizing label
        root.update_idletasks()  # Update the GUI
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        status_label.config(text="", fg="white")  # Reset text and text color
    except Exception as e:
        print(e)
        print("Say that again please...")
        status_label.config(text="Say that again please...", fg="white")  # Change text color to white
        return "None"
    finally:
        # Hide the labels after processing
        listening_label.config(text="", fg="white")  # Reset listening label
        recognizing_label.config(text="", fg="white")  # Reset recognizing label
    return query

# Function to execute commands based on user input
def execute_user_command(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        speak("Opening Google")
        webbrowser.open("google.com")
    elif 'open map' in query:
        speak("Opening maps")
        webbrowser.open("https://www.google.com/maps/@12.8072907,80.2369727,14.5z?entry=ttu")
    elif 'open stack overflow' in query:
        speak("Opening Stack Overflow")
        webbrowser.open("stackoverflow.com")
    elif 'play music' in query:
        speak("Playing music..")
        music_dir = 'C:\\Users\\Anagh\\OneDrive\\Desktop\\programming\\musiccc'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        print(strTime)
    elif 'open chrome' in query:
        speak("Opening Chrome app..")
        codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)
    elif 'weather' in query:
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
        speak(f"in chennai the current temprature is {t_1} degree celsius , it feels like {t_2} degree celsius , and the maximum temprature is {t_3} degree celsius, and the minimum temprature is {t_4} degree celsius")
        print(f"in chennai the current temprature is {t_1} degree celsius , it feels like {t_2} degree celsius , and the maximum temprature is {t_3} degree celsius, and the minimum temprature is {t_4} degree celsius")
    elif  ' news' in query:
        url_1="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=29fe516d782e40bc82d5ea848565617d"
        response_1=requests.get(url_1)
        data_1=response_1.json()
        news=[article['description'] for article in data_1['articles']]
        #print(news)
        speak("the latest news headlines are , ")
        i=0
        for description in news:
            i=i+1
            if i<=3:
                NeWs=description
                print(description)
                speak(description)

# Function to process user query
def process_query():
    q_1 = takeCommand()
    query = q_1.lower()
    execute_user_command(query)

def execute_command(event):
    process_query()

# Function to close the application
def close_app():
    root.destroy()

# Main application loop
if __name__ == "__main__":

    root = tk.Tk(wishMe())
    root.title("Jarvis - Your Personal Assistant")
    root.geometry("300x550")  # Adjusted window size for mobile
    root.configure(bg="#1f1f1f")  # Dark background color

    # Disable resizing
    root.resizable(False, False)

    # Main frame
    main_frame = tk.Frame(root, padx=20, pady=20, bg="#000000")  # Dark background color
    main_frame.pack(fill=tk.BOTH, expand=1)
    

    # Load and display image
    image = Image.open("D:/Projects/Jarvis/j_icon.png")
    image = image.resize((260, 400))  # Stretch the image to fit window width
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(main_frame, image=photo, bg="#000000")  # Dark background color
    label.image = photo
    label.grid(row=0, column=0, columnspan=1, pady=(5, 0))  # Center the image in the frame
    

    # Status label for listening and recognizing
    status_label = tk.Label(main_frame, text="", bg="#000000", fg="white")
    status_label.grid(row=1, column=0, columnspan=2)
    

    # Labels for listening and recognizing
    listening_label = tk.Label(main_frame, text="Listening...", bg="#000000", fg="white")
    recognizing_label = tk.Label(main_frame, text="Recognizing...", bg="#000000", fg="white")

    # Place labels in the middle of the UI
    listening_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))
    recognizing_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

    # Hide the labels initially
    listening_label.grid_remove()
    recognizing_label.grid_remove()
    
    

    canvas = tk.Canvas(main_frame, width=80, height=80, bg="#000000", bd=0, highlightthickness=0)
    canvas.create_oval(5, 5, 75, 75, fill="white", outline="white")  # Adjusted oval dimensions

    # Load and display image inside the circle
    icon_image = Image.open("D:/Projects/Jarvis/mic.jpeg")  # Replace "your_icon.png" with the path to your image
    icon_image = icon_image.resize((80, 80))  # Resize the image to fit inside the circle
    icon_photo = ImageTk.PhotoImage(icon_image)
    canvas.create_image(40, 40, image=icon_photo)  # Place the image at the center of the circle
    

    canvas.grid(row=2, column=0, pady=(0, 0), sticky="s")
    canvas.bind("<Button-1>", execute_command)
    

    

    root.mainloop()
    
