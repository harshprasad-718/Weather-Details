import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        elif response.status_code == 401:
            messagebox.showerror("Error", "Invalid API key. Please check your API key.")
            return None
        else:
            messagebox.showerror("Error", f"Error: {data['message']}")
            return None

    except requests.ConnectionError:
        messagebox.showerror("Error", "Connection error. Please check your internet connection.")
        return None

def display_weather(weather_data):
    if weather_data:
        city_name = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        result_label.config(text=f"Weather in {city_name}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nConditions: {description}")
    else:
        result_label.config(text="Failed to fetch weather data.")

def on_submit():
    location = entry.get()
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

# Replace with your actual OpenWeatherMap API key
api_key = "131b3c4ead684b21e2cc790685488e46"

# GUI Setup
root = tk.Tk()
root.title("Weather App")
icon = ImageTk.PhotoImage(file="logo.png")
root.iconphoto(True, icon)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter city or ZIP code:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, background='beige')
entry.grid(row=0, column=1, padx=5, pady=5)

submit_button = tk.Button(frame, text="Get Weather", command=on_submit, bg='lightGreen')
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)
root.geometry("300x200")
root.resizable(False, False)
root.mainloop()
