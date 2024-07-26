# Weather App

A simple weather application built using Python's Tkinter library and the OpenWeatherMap API.

## Description

This Weather App allows users to get the current weather information for a specified city. It provides details such as temperature, weather condition, pressure, humidity, wind speed, and sunrise/sunset times.

## Features

- Fetches real-time weather data from OpenWeatherMap API.
- Displays current temperature, weather condition, pressure, humidity, wind speed, and sunrise/sunset times.
- Simple and intuitive user interface.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required Python packages:
  ```bash
  pip install requests tkinter
  ```

## Usage
1. Obtain an API key from OpenWeatherMap.
2. Replace the placeholder API key in the script with your own API key:
```python
api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=YOUR_API_KEY"
```
3. Run the script:
```bash
python weather_app.py
```
4. Enter the city name in the text field and press Enter to get the weather information.

## Converting to an Executable
To convert the script to an executable, you can use auto-py-to-exe, a GUI tool for PyInstaller. Install it using:
```bash
pip install auto-py-to-exe
```
Run auto-py-to-exe and follow the instructions to convert your Python script into a standalone executable.

## Contribution

Contributions are welcome! If you have any ideas or suggestions, please let me know!
