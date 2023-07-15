# Python Weather Widget

This is a simple weather application that provides real-time weather updates for multiple cities. The application is built with Python and uses the Tkinter library for the GUI and the OpenWeatherMap API to get the weather data.

## Files

- `main.py`: This script is the main entry point for the application. It sets up the GUI, creates Weather_Widget objects for different cities and handles the API calls and updates to the widgets.

- `weather_widget_class.py`: This file defines the Weather_Widget class. The Weather_Widget class is a subclass of the tkinter LabelFrame widget that is designed to display the current weather conditions of a city.

## Features

- Real-time weather updates every 10 seconds.
- Display of weather condition, temperature (in Celsius), and humidity.
- Supports any city available in the OpenWeatherMap API.
- Comes with 3 different widget sizes: "big", "medium", and "small".

## Usage 

1. Sign up on OpenWeatherMap to get an API key.
2. Insert your API key in the `main.py` script in the API_key variable inside the "update()" function.
3. Run the main.py script to start the application.
