from tkinter import font
import requests
from tkinter import *

def weather():
    city = city_listbox.get()
    print("Selected city:", city)
    
    # Make sure to replace spaces in city names with '%20' if the API expects it
    city = city.replace(" ", "%20")
    
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=08d42d7508f4de84f1894ff5951ca6f9"
    res = requests.get(url)
    output = res.json()

    weather_status = output["weather"][0]["description"]
    temp = output["main"]["temp"]
    humidity = output["main"]["humidity"]
    wind_speed = output["wind"]["speed"]

    weather_status_label.config(text="Weather: " + weather_status)
    temp_label.config(text="Temperature: " + str(temp))
    humidity_label.config(text="Humidity: " + str(humidity))
    wind_speed_label.config(text="Wind Speed: " + str(wind_speed))

window = Tk()
window.geometry("400x300")

city_name_list = ["lucknow", "delhi", "bangalore", "pune"]
city_listbox = StringVar(window)
city_listbox.set("SELECT THE CITY : ")
option = OptionMenu(window, city_listbox, *city_name_list)
option.grid(row=2, column=2, padx=150, pady=10)

b1 = Button(window, text="Submit", width=15, command=weather)
b1.grid(row=5, column=2, padx=150)

weather_status_label = Label(window, font=("times", 10, "bold"))
weather_status_label.grid(row=6, column=2)

temp_label = Label(window, font=("times", 10, "bold"))
temp_label.grid(row=7, column=2)

humidity_label = Label(window, font=("times", 10, "bold"))
humidity_label.grid(row=8, column=2)

wind_speed_label = Label(window, font=("times", 10, "bold"))
wind_speed_label.grid(row=9, column=2)

window.mainloop()
