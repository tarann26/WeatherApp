import tkinter as tk
import requests
import time
 

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=79437de239a2ce1fda02e6a58028811f"
    
    json_data = requests.get(api).json()
    cond = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pres = json_data['main']['pressure']
    hum = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sr = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    ss = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    final_info = cond + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pres) + "\n" +"Humidity: " + str(hum) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sr + "\n" + "Sunset: " + ss
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("500x400")
canvas.title("Weather App")
f = ("Helvetica", 15, "bold")
t = ("Helvetica", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()