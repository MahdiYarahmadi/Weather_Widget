
import tkinter as tk
import math


class Weather_Widget(tk.Frame):

    def __init__(self, master=None, city='CITY',size='medium', **kwargs):
        super().__init__(master,bg='#4d4d4d',bd=5, relief="sunken", **kwargs)
        # Initialize object properties
        self.city = city
        self.widget_size = size
        self.current_description = None
        self.current_temperature = None
        self.current_humidity = None
        # Adjust widget size and create the layout
        self.adjust_widget_size()
        self.create_frame_layout()

    def adjust_widget_size(self):
        '''
        Sets the size of the canvas and the symbols based on the
        size of frame (big, medium, small). Also adjusts the font sizes
        of the labels in the frame which indirectly affects the label's sizes.
        '''
        if self.widget_size == "big":         # Adjust the parameters for widgets with size "big"
            self.canvas_width, self.canvas_height = 250, 250
            self.sun_symbol_size, self.cloud_symbol_size = 55, 100
            self.font_size_city_label, self.font_size_condition_label = 35, 20

        elif self.widget_size == "medium":    # Adjust the parameters for widgets with size "medium"
            self.canvas_width, self.canvas_height = 150, 150
            self.sun_symbol_size, self.cloud_symbol_size = 30, 60
            self.font_size_city_label, self.font_size_condition_label = 20, 16

        elif self.widget_size == "small":     # Adjust the parameters for widgets with size "small"
            self.canvas_width, self.canvas_height = 80, 80
            self.sun_symbol_size, self.cloud_symbol_size = 17, 30
            self.font_size_city_label, self.font_size_condition_label = 14, 10

    def create_frame_layout(self):
        '''
        Create the layout of the Weather_widget.
        Each Weather_widget is composed of a canvas (for displaying weather symbols)
        and two labels (to display the city name and weather conditions). This method
        creates these elements and arranges them in the frame.
        '''
        # Create the canvas
        self.canvas = tk.Canvas(self, width=self.canvas_width,
                                height=self.canvas_height, bd=3,
                                relief="raised", bg="skyblue")
        # Place the canvas using grid geometry manager
        self.canvas.grid(row=0, column=0, rowspan=2)

        # Create and place the layers
        self.city_label = tk.Label(self, text=self.city, bd=5, relief="sunken",
                                   font=('Times', self.font_size_city_label, 'bold'))
        self.city_label.grid(row=0, column=1)

        self.condition_label = tk.Label(self, width=20, bg="yellow", fg="green",
                                        font=('Arial', self.font_size_condition_label, 'italic'))
        self.condition_label.grid(row=1, column=1)

    def create_sun_symbol(self, x, y, radius):
        '''
        Designs the sun symbol on the canvas
        :param x: x coordinate of the center of canvas (center of the sun, too)
        :param y: y coordinate of the center of canvas (center of the sun, too)
        :param radius: radius of the sun body
        '''
        # Clear what's on the canvas
        self.canvas.delete("all")

        # Draw sun body
        x = x + radius / 7        # Shift the center of the sun slightly to the right
        self.canvas.create_oval(x - radius, y - radius,
                                x + radius, y + radius,
                                fill='yellow', outline='orange', width=2)
        # Draw a white disk with a smaller radius on the sun body
        small_radius = radius / 4
        self.canvas.create_oval(x - small_radius, y - small_radius,
                                x + small_radius, y + small_radius,
                                fill='white', outline='')

        # Draw 24 sun rays
        for i in range(24):
            angle_in_deg = i * 15                            # 24 * 15° = 360°
            angle_in_rad = math.radians(angle_in_deg)        # Convert degree to radian
            # Calculate the coordinates of the vertices for each ray
            x1 = x + radius * math.cos(angle_in_rad)
            y1 = y - radius * math.sin(angle_in_rad)
            x2 = x + 1.9 * radius * math.cos(angle_in_rad)   # 1.9 and 1.3 specify how thin and
            y2 = y - 1.9 * radius * math.sin(angle_in_rad)   # how long the rays are
            x3 = x + 1.3 * radius * math.cos(math.radians(angle_in_deg + 5))
            y3 = y - 1.3 * radius * math.sin(math.radians(angle_in_deg + 5))
            # Set the color of even rays to "orange" and the odd rays to "yellow"
            if i % 2 == 0:
                color = 'orange'
            else:
                color = 'yellow'
            # Draw the ray using the coordinates
            self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)

    def create_cloud_symbol(self, x, y, size):
        '''
        Draws two clouds. Each cloud is made up of several ovals. The ovals
        are positioned and scaled relative to the parameter 'size'.
        :param x: x coordinate of the center of canvas (not the shape)
        :param y: y coordinate of the center of canvas (not the shape)
        :param size: a parameter to control the shape size
         note:  approximate total width of the shape: (1.8 * size)
                approximate total height of the shape: (0.8 * size)
        '''
        # Clear what's on the canvas
        self.canvas.delete("all")

        # Calculate the coordinates of the reference point of first
        # cloud (top left of the white cloud) by subtracting half of
        # the total width and total height of the shape from the
        # coordinates of the center point of canvas
        x = x - (0.9 * size)     # (1.8 * size) / 2 = (0.9 * size)
        y = y - (0.4 * size)     # (0.8 * size) / 2 = (0.4 * size)

        # Initialize the list "first cloud" to store the coordinates (x1, y1, x2, y2) of
        # the ovals that form the first cloud
        first_cloud = [(x, y, x + size, y + size / 2),                            # 1st oval
                       (x + size / 6, y - size / 4, x + 2 * size / 3, y + size / 1.8),
                       (x + size / 2, y - size / 4, x + 2.2 * size / 3, y + size / 2),
                       (x + size / 2, y + size / 8, x + 3 * size / 2, y + 1.2 * size / 2),
                       (x + 2 * size / 3, y - size / 4, x + 3.5 * size / 3, y + size / 1.7),
                       (x + 3.3 * size / 3, y - size / 8, x + 4.7 * size / 3, y + size / 3)]   # 6th oval
        # Move the reference point of the first cloud to the reference point
        # of the second cloud (top left point of it), where it's first oval will be drawn
        x = x + size / 2
        y = y + size / 2
        # Initialize the list "second cloud"
        second_cloud = [(x, y, x + size, y + size / 2),                          # 1st oval
                        (x + size / 6, y - size / 4, x + 2 * size / 3, y + size / 2),
                        (x + size / 2, y - size / 3, x + 2.5 * size / 3, y + size / 2),
                        (x + size / 2, y + size / 8, x + 3 * size / 2, y + 1.1 * size / 2),
                        (x + 2 * size / 3, y - size / 4, x + 4 * size / 3, y + size / 2)]     # 5th oval

        # Loop through each set of coordinates (x1, y1, x2, y2) in the both lists and
        # draw an oval at these coordinates to construct the clouds
        for part in first_cloud:
            self.canvas.create_oval(part, fill='white', outline='')
        for part in second_cloud:
            self.canvas.create_oval(part, fill='#e3e7e8', outline='')

    def create_new_symbol(self):
        '''
        The next symbol can be designed here
        '''

    def create_temporary_symbol(self, condition):
        '''
        Writes the input parameter "condition" on the canvas as a temporary symbol.
        Note: The method is used when the symbol that corresponds to
        the current weather condition is not yet designed.
        This method can be deleted after all symbols are designed.
        :param condition: weather condition of a city
        '''
        # Clear what's on the canvas
        self.canvas.delete("all")

        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2,
                                font=("Arial", self.font_size_condition_label),
                                text=condition + "\nsymbol", fill="blue")

    def update_frame(self, condition, temperature, description, humidity):
        '''
        Update the frame with the new weather information
        Note: If the condition is not "Clear" or "Clouds", a temporary
        symbol will be displayed as the weather symbol on canvas.
        '''
        # Update the current weather details of the frame
        self.current_description = description
        self.current_temperature = temperature
        self.current_humidity = humidity
        # Update the condition_label with the new weather details
        self.condition_label.config(text="{} ,  {:.0f}°C".format(description, temperature) +
                                    "\nhumidity: {}%".format(humidity))

        # Update the weather symbol on the frame according to the condition.
        # If the condition is "Clear", draw the sun symbol using "create_sun_symbol" method
        if condition == "Clear":
            self.create_sun_symbol(self.canvas_width/2, self.canvas_height/2, self.sun_symbol_size)
        # if the condition is "Clouds", draw the cloud symbol using "create_cloud_symbol" method
        elif condition == "Clouds":
            self.create_cloud_symbol(self.canvas_width/2, self.canvas_height/2, self.cloud_symbol_size)

        # When the new symbol is designed, it should be created (only for the corresponding condition) as follows:
        #    elif condition == "the condition that corresponds to the new symbol":
        #        self.create_new_symbol()

        # In case there are no designed symbols for the current condition, create the temporary symbol
        else:
            self.create_temporary_symbol(condition)


