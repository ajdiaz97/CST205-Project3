#http://effbot.org/librarybook/csv.htm
#http://matplotlib.org/basemap/users/geography.html
#http://www.uvm.edu/~jbagrow/dsv/heatmap_basemap.html
#http://matplotlib.org/basemap/api/basemap_api.html#module-mpl_toolkits.basemap
#https://www.youtube.com/watch?v=8v3how07th4&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF&index=28
#https://pypi.python.org/pypi/geocoder

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import geocoder


global cityofinterest #so you can search a city specifically
#Makes a map of specifically California
#llcrnrlat = lower leftcorner latitude, urcrnrlat = upper right corner latitude, llcrnerlon = lower leftcorner longitude, upper right corner longitude
map = Basemap(projection = 'mill', llcrnrlat = 31, urcrnrlat = 43, llcrnrlon = -130, urcrnrlon = -109, resolution = 'h')
map.drawcoastlines()
map.drawmapboundary(fill_color = '#000080')
map.fillcontinents(color = '#84BE6A', lake_color = '#000080')
map.drawstates(linewidth = 1)
map.drawcountries(linewidth = 1)



#Lists
date = []
time = []
city = []
state = []
shape = []
duration = []

description = []
#Reads the CSV file and seperates the data into lists
#goes through the csv and puts them in a list
with open('Sightings.csv') as data:
    reader = csv.reader(data)
    for row in reader:
        date.append(row[0])
        time.append(row[1])
        city.append(row[2])
        state.append(row[3])
        shape.append(row[4])
        duration.append(row[5])
        description.append(row[6])


#For city search
def citysearch():
    flag = 0 #A flag variable
    global cityofinterest
    lengthofstring = len(city)
    searchforcity = input("What city would you like to look for? Make sure that the city is capitalized when writing it in \n")
    #Goes through the list of cities and checks to see if the city is in the list
    for x in range(0, lengthofstring):
        #If the city is in the list it will tell you about it
        if(city[x] == searchforcity):
            print(" = ", searchforcity, " = ")
            print("A UFO sighting has happened on", date[x], "at the time", time[x], ". The ship was", shape[x], "shaped", "and showed up for", duration[x], ".", "The description the person who saw the ship is", description[x], " \n")
            flag = 1

    #Since you can only use geocoder 2500 times a day it will allow you to find an exact city
    if (flag == 1):
        cityofinterest = (geocoder.google(searchforcity))
        print(cityofinterest)
        print("GENERATING MAP NOW \n")
        xpt, ypt = map(cityofinterest.lng, cityofinterest.lat)
        map.plot(xpt,ypt, 'c*', markersize = 15, color = '#FFFFFF')

        if(cityofinterest == "None None"):
            print("Sorry Geocoder cannot be used at this moment. Please try again in a few minutes")
            quit()

    #Since the flag is already is 0 it will come here if the city is not found and quit the program
    else:
        print("Sorry that city was not found. Please try again")
        ask = input("Would you like to quit or try again? \n")
        if(ask == "try again" or ask == "Try again"):
            citysearch()
        elif(ask == "quit" or ask == "Quit"):
            quit()
#Start the process
def beginning():
    print(" \nYou can search by 'city' or 'shape'") #Maybe date later but that's beta
    question = input("How would you like to search for UFO's? \n ")

    if(question == "city" or question == "City" or question == "CITY"):
        citysearch()

    #if(question == 'shape' or 'Shape' or 'SHAPE'): will work on this now
    else:
        print("Invalid response please try again \n")
        beginning()


beginning()
plt.title('UFO SIGHTINGS IN CALIFORNIA')
plt.show()
