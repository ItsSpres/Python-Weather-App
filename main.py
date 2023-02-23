# Ian Spresney
# Weather App
# Class CIS 245

import json, requests
from urllib.parse import quote
import config
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")
window.title("Weather App!")


def main():
    apiKey = config.api_Key # Getting API key from config file.
    # User will now select whether they want to search using zipcode or city name.
    userSelect = input('Enter Z to search using zipcode or C to search using city name: ')

    # This statement checks for what the user wants to do. Then it will also collect the proper data.
    if userSelect != 'Z':
        countryCode = input('Please enter your country code. (ex: US): ').lower()
        stateCode = input('Please enter your state code. (ex: CA): ').lower()
        cityName = input('Please enter your city name: ').lower()
        apiUrl = f'https://api.openweathermap.org/data/2.5/weather?q={quote(cityName)},{stateCode},{countryCode}&appid={apiKey}&units=imperial'
        # print(apiUrl)
        get_weather(apiUrl)
    elif userSelect == 'Z':
        zipcode = input('Please enter your zipcode: ').lower()
        countryC = input('Please enter your country code. (ex: US): ').lower()
        # building the URL.
        apiUrlZipcode = f'https://api.openweathermap.org/data/2.5/weather?zip={quote(zipcode)},{countryC}&appid={apiKey}&units=imperial'
        # print(apiUrl)
        get_weather_by_zip(apiUrlZipcode)
    else: # If there is a mistake then the program will start over.
        print('Try again...')
        main()

# Get weather data with city name
def get_weather(url):
    try: # We are going to use this try block to guard against possible errors from trying to connect.
        responseFromApi = requests.get(url).json() # getting the json data from the api.
        if responseFromApi['cod'] == 200: # Checking if we got a good status code.
            # print(responseFromApi)

            # printing all the data.
            print('Connection was successful!')
            print(f"Name of City: {responseFromApi['name']}")
            print(f"Weather Type: {responseFromApi['weather'][0]['main']}")
            print(f"Temperature: {responseFromApi['main']['temp']}°F")

            # this is extra stuff I wanted to play around with. This prints to a separate window.
            city_name = tk.Label(text=f"{responseFromApi['name']}")
            city_name.pack()
            weatherType = tk.Label(text=f"{responseFromApi['weather'][0]['main']}")
            weatherType.pack()
            temp = tk.Label(text=f"{responseFromApi['main']['temp']}°F")
            temp.pack()

        else:
            print('there was an error, please try again')
    except:
        print('failed')
    finally:
        start_over() # Run this function after everything has finished.

# Get weather data with zipcode
def get_weather_by_zip(url):
    try:
        responseFromApi = requests.get(url).json()
        if responseFromApi['cod'] == 200:
            # print(responseFromApi)
            print('Connection was successful!')
            print(f"Name of City: {responseFromApi['name']}")
            print(f"Weather Type: {responseFromApi['weather'][0]['main']}")
            print(f"Temperature: {responseFromApi['main']['temp']}°F")

            # this is extra stuff I wanted to play around with
            city_name = tk.Label(text=f"{responseFromApi['name']}")
            city_name.pack()
            weatherType = tk.Label(text=f"{responseFromApi['weather'][0]['main']}")
            weatherType.pack()
            temp = tk.Label(text=f"{responseFromApi['main']['temp']}°F")
            temp.pack()

        else:
            print('there was an error, please try again')
    except:
        print('failed')
    finally:
        start_over()

def start_over(): # Asking user if they would like to start over and add another location.
    userInput = input('Ready to try again? Type Y for yes and N to quit: ')
    if userInput == 'Y':
        main()
    elif userInput == 'N':
        print('Program has ended. Have a nice day.')

print('---Program Start---')
print('Welcome to the Weather App!')
print('At the end of this program, all searches will display on a separate window.')

main()
window.mainloop()
