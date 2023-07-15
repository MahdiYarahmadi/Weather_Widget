
import tkinter as tk
import requests
from weather_widget_class import Weather_Widget


# Define a function to get and update weather information
def update(frame):
    '''
    Get and update weather data from the OpenWeatherMap API for
    the city specified in the input frame at 10-second intervals.
    :param frame: a Weather_widget
    '''
    # Construct the url for sending the API request
    base_url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid="
    API_key = "..."                                # Insert the API key here
    city = frame.city                              # Get the city's name
    url = base_url + API_key + "&q=" + city        # Concatenate the strings to construct the url
    response = requests.get(url).json()            # Send request and convert the response to JSON

    # Extract relevant information from the server's response
    condition = response['list'][0]['weather'][0]['main']
    description = response['list'][0]['weather'][0]['description']
    temperature_in_Kelvin = response['list'][0]['main']['temp']
    humidity = response['list'][0]['main']['humidity']

    # Convert Kelvin to Celcius
    temperature_in_Celcius = temperature_in_Kelvin - 273.15

    # Update the frame if there is new data
    if (description != frame.current_description or
        temperature_in_Celcius != frame.current_temperature or
        humidity != frame.current_humidity):
        frame.update_frame(condition, temperature_in_Celcius, description, humidity)

    # Schedule this function to be called again after 10 seconds
    frame.after(10000, update, frame)

if __name__ == '__main__':

    # Initialize the root window
    root = tk.Tk()

    # Specify the size and location of window(root)
    window_width = 900                                 # Width of window
    window_height = 600                                # Height of window
    screen_width = root.winfo_screenwidth()            # Get width of screen
    screen_height = root.winfo_screenheight()          # Get height of screen
    # Calculate the coordinates of the top left for the window
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

    # Set the title and icon of the window
    root.title("Weather App")
    icon = tk.PhotoImage(file='images/icon.png')
    root.iconphoto(True, icon)

    # Set a background image for the window
    background_image = tk.PhotoImage(file='images/window_background.png')
    background_label = tk.Label(image=background_image).place(x=0, y=0, relwidth=1, relheight=1)

    # Create Weather_widget objects for different cities.
    # The "size" attribute of the Weather_widget is set
    # to "medium" by default but there are available
    # in 3 different sizes: "big", "medium" and "small".
    frame1 = Weather_Widget(root, city="MUNICH", size="big")   # Create frame1 with "big" size
    frame1.pack(side="top", pady=10)   # Add frame1 to the window using pack geometry manager

    frame2 = Weather_Widget(root, city="CHICAGO")     # Create the frame2 object with "medium" size (by default)
    frame2.pack(side="left", padx=10, pady=10)

    frame3 = Weather_Widget(root, city="ROME", size="small")  # Create the third object with "small" size
    frame3.pack(side="right", padx=10, pady=10)

    # Call the update function for each object
    update(frame1)
    update(frame2)
    update(frame3)

    # Start the tkinter event loop
    root.mainloop()
