# Weather Dashboard

This is a simple weather dashboard written in Python. The dashboard allows users to search for the weather in different cities and view their search history.

# Approach
The code uses a dictionary DUMMY_WEATHER to store weather data for different cities. The fetch_weather function retrieves the weather data for a given city, and the save_history function saves the search history to a JSON file.

# How to Run
1. Save the code in a file named weather_dashboard.py.
2. Open a terminal or command prompt and navigate to the directory where the file is saved.
3. Run the program using the command python weather_dashboard.py.

# Example Input/Output
Search Weather
Enter choice: 1
Enter city name: delhi
Weather in Delhi, India: 32°C, sunny

Show Last Searches
Enter choice: 2
=== Last 5 Searches ===
Delhi (India) - 32°C, sunny

Exit the Program
Enter choice: 3

# Challenges Faced
1. Data Persistence: One of the challenges faced was implementing data persistence using a JSON file. This required careful consideration of how to serialize and deserialize the search history data.
2. Error Handling: Another challenge was handling errors that may occur during file operations or user input. This required implementing try-except blocks to catch and handle exceptions.


