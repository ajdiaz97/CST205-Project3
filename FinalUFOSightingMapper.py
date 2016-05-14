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
import numpy as np
global cityofinterest #so you can search a city specifically
global searchforcity




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
citywiththings = [] #vague because its for shapes and date searches

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
    counter = 0
    cityer = 0 #A flag variable
    global cityofinterest
    global searchforcity
    lengthofstring = len(city)
    print("\n")
    print("---------------------------------------------------------------------------------------------------")
    #Goes through the list of cities and checks to see if the city is in the list
    for x in range(0, lengthofstring):
        #If the city is in the list it will tell you about it
        if(city[x] == searchforcity):
            print(" = ", searchforcity, " = ")
            print("A UFO sighting has happened on", date[x], "at the time", time[x], ". The ship was", shape[x], "shaped", "and showed up for", duration[x], ".", "The description the person who saw the ship is", "'", description[x],"'", " \n")
            cityer = 1
            counter = counter+1

    print("There are ",counter, " sightings above that match the city ", searchforcity)

    print("----------------------------------------------------------------------------------------------------")
    #Since you can only use geocoder 2500 times a day it will allow you to find an exact city
    if (cityer == 1):
        textformap = searchforcity
        searchforcity = searchforcity + " CA" #To make sure that geocoder is using California
        cityofinterest = (geocoder.google(searchforcity))
        print(cityofinterest)
        print("GENERATING MAP NOW \n")
        xpt, ypt = map(cityofinterest.lng, cityofinterest.lat)
        map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
        plt.text(xpt,ypt, textformap , fontsize = 10, fontweight = 'bold', color = '#FFFFFF')
        plt.title('UFO SIGHTINGS IN CALIFORNIA')
        plt.show()
        #Geocoder can only be used 2500 times and after that it will make city of interest None None
        if(cityofinterest == "None None"):
            print("Sorry Geocoder cannot be used at this moment. Please try again in a few minutes")
            quit()

    #Since the flag is already is 0 it will come here if the city is not found and it will do nothing
    if(cityer == 0):
        print("")



#For Shape Search and Date Search
def advancedsearch():
    counter = 0
    searcher = 0
    global question
    if(question == 'Shape'):
        lengthofstring = len(shape)
        print("---------------------------------------------------------------------------------------------------")
        #Goes through the list of shapes and checks to see if the shape is in the list
        for x in range(0, lengthofstring):
            #If the shape is in the list it will tell you about it
            if(shape[x] == searchforshape):

                print(" = ", city[x], " = ")
                print("A UFO sighting has happened on", date[x], "at the time", time[x], ". The location was in ", city[x], "California", "and showed up for", duration[x], ".", "The description the person who saw the ship is", "'", description[x],"'", " \n")
                citywiththings.append(city[x])
                searcher = 1
                counter = counter + 1
        print("There are ", counter, " sightings above that match the shape of ", searchforshape)

    if(question == 'date' or question == 'Date'):
        lengthofstring = len(date)
        dash = '/' #for the string
        year1 = '2014' #for the string becuase it won't searchwithout all parameters
        year2 = '2015' #other year and needed to search
        #adds all the parameters to be able to search the dates list
        finalforsearch = searchformonth + dash + searchforday + dash + year1
        finalforsearch2 = searchformonth + dash + searchforday + dash + year2

        #Searches the dates and finds the occurances that happen
        for d in range(0, lengthofstring):
            if(date[d] == finalforsearch or date[d] == finalforsearch2):
                print(" = ", city[d], " = ")
                print(" = ", date[d], " = ")
                print("The shape of the UFO was", shape[d], "at the time", time[d], ". The location was in ", city[d], "California", "and showed up for", duration[d], ".", "The description the person who saw the ship is", "'", description[d],"'", " \n")
                citywiththings.append(city[d])
                searcher = 1
                counter = counter + 1
        print("There are ", counter, " sightings above that match the date of ", searchformonth, "/", searchforday)
        #Goes through the list of dates the puts the days in a list

    print("----------------------------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #To plot the map of the cities. If a city matches a description of either date or shape it will plot the city
    #Long but necessary
    if(searcher == 1):
        lengthofcitywiththings = len(citywiththings)

        for y in range(0, lengthofcitywiththings):

            if(citywiththings[y] == 'Alameda'):
                Alemlng, Alemlat  = ( -122.3, 37.76)
                xpt, ypt = map(Alemlng, Alemlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Alameda" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Alamo'):
                Alamolng, Alamolat = (37.85, -122.03)
                xpt,ypt = map(Alamolng, Alamolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Alamo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Aliso Viejo'):
                Alilng, Alilat  = ( -117.7, 33.56)
                xpt, ypt = map(Alilng, Alilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Aliso Viejo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Alta Loma'):
                Altlng, Altlat  = ( -117.6, 34.12)
                xpt, ypt = map(Altlng, Altlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Alta Loma" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Altadena'):
                Altdlng, Altdlat  = (-118.13, 34.19)
                xpt, ypt = map(Altdlng, Altdlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Altadena" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Anaheim'):
                Analng, Analat  = ( -117.91, 33.83)
                xpt, ypt = map(Analng, Analat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Anaheim" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Anderson'):
                Andlng, Andlat  = ( -122.29, 40.44)
                xpt, ypt = map(Andlng, Andlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Anderson" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Antelope'):
                Antlng, Antlat  = ( -121.36, 38.71)
                xpt, ypt = map(Antlng, Antlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Antelope" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Antioch'):
                Antilng, Antilat  = ( -121.80, 38.00)
                xpt, ypt = map(Antilng, Antilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Antioch" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Apple Valley'):
                Applng, Applat  = ( -117.19, 34.50)
                xpt, ypt = map(Applng, Applat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Apple Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Aptos'):
                Aptlng, Aptlat  = ( -121.89, 36.97)
                xpt, ypt = map(Aptlng, Aptlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Aptos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Arbuckle'):
                Arlng, Arlat  = ( -122.05, 39.01)
                xpt, ypt = map(Arlng, Arlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Arbuckle" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Arcadia'):
                Arclng, Arclat  = ( -118.04, 34.13)
                xpt, ypt = map(Arclng, Arclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Arcadia" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Arcata'):
                Arcalng, Arcalat  = ( -124.08, 40.86)
                xpt, ypt = map(Arcalng, Arcalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Arcata" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Armona'):
                Armlng, Armlat  = ( -119.70, 36.31 )
                xpt, ypt = map(Armlng, Armlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Armona" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Arroyo Grande'):
                Arrlng, Arrlat  = ( -120.59, 35.12)
                xpt, ypt = map(Arrlng, Arrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Arroyo Grande" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Atascadero'):
                Atalng, Atalat  = ( -120.67, 35.49)
                xpt, ypt = map(Atalng, Atalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Atascadero" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Atwater'):
                Atwlng, Atwlat  = ( -120.61, 37.35)
                xpt, ypt = map(Atwlng, Atwlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Atwater" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Auburn'):
                Aublng, Aublat  = ( -121.08, 38.89)
                xpt, ypt = map(Aublng, Aublat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Auburn" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Avenal'):
                Avlng, Avlat  = ( -120.13, 36.00)
                xpt, ypt = map(Avlng, Avlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Avenal" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Avocado Heights'):
                Avolng, Avolat  = ( -117.99, 34.04)
                xpt, ypt = map(Avolng, Avolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Avocado Heights" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Azusa'):
                Azlng, Azlat  = ( -117.91, 34.13)
                xpt, ypt = map(Azlng, Azlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Azusa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Bakersfield'):
                Baklng, Baklat  = ( -119.02, 35.37)
                xpt, ypt = map(Baklng, Baklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Bakersfield" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Balboa Island'):
                Ballng, Ballat  = ( -117.89, 33.61)
                xpt, ypt = map(Ballng, Ballat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Balboa Island" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Baldwin Park'):
                Baldlng, Baldlat  = ( -117.96, 34.09)
                xpt, ypt = map(Baldlng, Baldlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Baldwin Park" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Banning'):
                Banlng, Banlat  = ( -116.87, 33.93)
                xpt, ypt = map(Banlng, Banlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Banning" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Barstow'):
                Barlng, Barlat  = ( -117.02, 34.89)
                xpt, ypt = map(Barlng, Barlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Barstow" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Bass Lake'):
                Baslng, Baslat  = ( -119.57, 37.32)
                xpt, ypt = map(Baslng, Baslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Bass Lake" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Bay Area'):
                Baylng, Baylat  = ( -122.29, 37.83)
                xpt, ypt = map(Baylng, Baylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Bay Area" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Beaumont'):
                Bealng, Bealat  = ( -116.97, 33.93)
                xpt, ypt = map(Bealng, Bealat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Beaumont" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Benicia'):
                Benlng, Benlat  = ( -122.16, 38.05)
                xpt, ypt = map(Benlng, Benlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Benicia" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Berkeley'):
                Berlng, Berlat  = ( -122.27, 37.87)
                xpt, ypt = map(Berlng, Berlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Berkeley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Berry Creek'):
                Berrlng, Berrlat  = ( -121.40, 39.65)
                xpt, ypt = map(Berrlng, Berrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Berry Creek" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Big Bear Lake'):
                Biglng, Biglat  = ( -116.91, 34.24)
                xpt, ypt = map(Biglng, Biglat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Big Bear Lake" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Big Pine'):
                Bplng, Bplat  = ( -118.29, 37.16)
                xpt, ypt = map(Bplng, Bplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Big Pine" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Big Sur'):
                Bslng, Bslat  = ( -121.86, 36.36)
                xpt, ypt = map(Bslng, Bslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Big Sur" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Blocksburg'):
                Bllng, Bllat  = ( -123.64, 40.28)
                xpt, ypt = map(Bllng, Bllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Blocksburg" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Blythe'):
                Blylng, Blylat  = ( -114.59, 33.62)
                xpt, ypt = map(Blylng, Blylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Blythe" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Bonny Doon'):
                Bolng, Bolat  = ( -122.15, 37.04)
                xpt, ypt = map(Bolng, Bolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Bonny Doon" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Bonsall'):
                Bonlng, Bonlat  = ( -117.23, 33.29)
                xpt, ypt = map(Bonlng, Bonlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Bonsall" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Borrego Springs'):
                Borrlng, Borrlat  = ( -116.87, 33.93)
                xpt, ypt = map(Borrlng, Borrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Borrego Springs" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Boulder Creek'):
                Boulng, Boulat  = ( -122.12, 37.13)
                xpt, ypt = map(Boulng, Boulat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Boulder Creek" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Boyle Heights'):
                Boylng, Boylat  = ( -118.21, 34.02)
                xpt, ypt = map(Boylng, Boylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Boyle Heights" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Banning'):
                Banlng, Banlat  = ( -116.87, 33.93)
                xpt, ypt = map(Banlng, Banlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Banning" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Brawley'):
                Brlng, Brlat  = ( -115.53, 32.98)
                xpt, ypt = map(Brlng, Brlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Brawley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Brentwood'):
                Brelng, Brelat  = ( -121.70, 37.93)
                xpt, ypt = map(Brelng, Brelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Brentwood" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Buellton'):
                Bulng, Bulat  = ( -120.19, 34.61)
                xpt, ypt = map(Bulng, Bulat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Buellton" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Buena Park'):
                Buelng, Buelat  = ( -117.99, 33.87)
                xpt, ypt = map(Buelng, Buelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Buena Park" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Burbank'):
                Burlng, Burlat  = ( -118.31, 34.18)
                xpt, ypt = map(Burlng, Burlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Burbank" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Calimesa'):
                Clng, Clat  = ( -117.06, 34.00)
                xpt, ypt = map(Clng, Clat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Calimesa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Calistoga'):
                Callng, Callat  = ( -122.58, 38.58)
                xpt, ypt = map(Callng, Callat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Calistoga" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Camarillo'):
                Camlng, Camlat  = ( -119.04, 34.22)
                xpt, ypt = map(Camlng, Camlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Camarillo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cambria'):
                Camblng, Camblat  = ( -121.08, 35.56)
                xpt, ypt = map(Camblng, Camblat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cambria" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Campbell'):
                Camplng, Camplat  = ( -121.95, 37.29)
                xpt, ypt = map(Camplng, Camplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Campbell" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Canoga Park'):
                Canlng, Canlat  = ( -118.61, 34.21)
                xpt, ypt = map(Canlng, Canlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Canoga Park" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Canyon Country'):
                Canylng, Canylat  = ( -118.47, 34.42)
                xpt, ypt = map(Canylng, Canylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Canyon Country" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Canyon Lake'):
                Canyolng, Canyolat  = ( -117.27, 33.69)
                xpt, ypt = map(Canyolng, Canyolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Canyon Lake" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Capitola'):
                Caplng, Caplat  = ( -121.95, 36.98)
                xpt, ypt = map(Caplng, Caplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Capitola" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cardiff by the Sea' or citywiththings[y] == 'Cardiff by The Sea'):
                Carlng, Carlat  = ( -117.28, 33.02)
                xpt, ypt = map(Carlng, Carlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cardiff By The Sea" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Caribou'):
                Carilng, Carilat  = ( -121.16, 40.08)
                xpt, ypt = map(Carilng, Carilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Caribou" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Carlsbad' or citywiththings[y] == 'Carlsbad/Oceanside'):
                Carllng, Carllat  = ( -117.35, 33.16)
                xpt, ypt = map(Carllng, Carllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Carlsbad" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Carmel Valley' ):
                Carmlng, Carmlat  = ( -121.73, 36.48)
                xpt, ypt = map(Carmlng, Carmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Carmel Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Carmichael' ):
                Carmilng, Carmilat  = ( -121.33, 38.62)
                xpt, ypt = map(Carmilng, Carmilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Carmichael" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Carpenteria' or citywiththings[y] == 'Carpinteria'):
                Carplng, Carplat  = ( -119.52, 34.40)
                xpt, ypt = map(Carplng, Carplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Carpinteria" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Carson' ):
                Carslng, Carslat  = ( -118.28, 33.83)
                xpt, ypt = map(Carslng, Carslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Carson" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Castaic' ):
                Castlng, Castlat  = ( -118.63, 34.49)
                xpt, ypt = map(Castlng, Castlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Castaic" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Castro Valley' ):
                Castrlng, Castrlat  = ( -122.08, 37.69)
                xpt, ypt = map(Castrlng, Castrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Castro Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Catalina Island' ):
                Catlng, Catlat  = ( -122.09, 37.69)
                xpt, ypt = map(Catlng, Catlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Catalina Island" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cathedral City' ):
                Cathlng, Cathlat  = ( -116.47, 33.78)
                xpt, ypt = map(Cathlng, Cathlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cathedral City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cayucos' ):
                Caylng, Caylat  = ( -120.89, 35.44)
                xpt, ypt = map(Caylng, Caylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cayucos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cerritos' ):
                Cerrlng, Cerrlat  = ( -118.06, 33.86)
                xpt, ypt = map(Cerrlng, Cerrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cerritos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Chatsworth' ):
                Chlng, Chlat  = ( -118.61, 34.25)
                xpt, ypt = map(Chlng, Chlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Chatsworth" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Chico' ):
                Chilng, Chilat  = ( -121.84, 39.73)
                xpt, ypt = map(Chilng, Chilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Chico" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Chino' ):
                Chinlng, Chinlat  = ( -117.69, 34.01)
                xpt, ypt = map(Chinlng, Chinlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Chino" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Chino Hills' ):
                Chhlng, Chhlat  = ( -117.73, 33.99)
                xpt, ypt = map(Chhlng, Chhlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Chino Hills" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Chula Vista' ):
                Cvlng, Cvlat  = ( -117.08, 32.64)
                xpt, ypt = map(Cvlng, Cvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Chula Vista" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Citrus Heights' ):
                Citlng, Citlat  = ( -121.28, 38.70)
                xpt, ypt = map(Citlng, Citlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Citrus Heights" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'City of Industry' ):
                CIlng, CIlat  = ( -117.96, 34.02)
                xpt, ypt = map(CIlng, CIlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Industry" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Clairemont' ):
                Clarlng, Clarlat  = ( -117.72, 34.10)
                xpt, ypt = map(Clarlng, Clarlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Claremont" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Clayton' ):
                Claylng, Claylat  = ( -121.94, 37.94)
                xpt, ypt = map(Claylng, Claylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Clayton" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Clearlake' ):
                Clelng, Clelat  = ( -122.63, 38.96)
                xpt, ypt = map(Clelng, Clelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Clearlake" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Clovis' ):
                Clolng, Clolat  = ( -119.70, 36.83)
                xpt, ypt = map(Clolng, Clolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Clovis" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Coalinga' ):
                Coalng, Coalat  = ( -120.36, 36.14)
                xpt, ypt = map(Coalng, Coalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Coalinga" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cobb' ):
                Cobblng, Cobblat  = ( -122.72, 38.83)
                xpt, ypt = map(Cobblng, Cobblat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cobb" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')


            if(citywiththings[y] == 'Caomptche' ):
                Coalng, Coalat  = ( -123.59, 39.26)
                xpt, ypt = map(Caolng, Caolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Caomptche" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Concord' ):
                Conlng, Conlat  = ( -122.03, 37.98)
                xpt, ypt = map(Conlng, Conlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Concord" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cool' ):
                Coolng, Coolat  = ( -121.02, 38.89)
                xpt, ypt = map(Coolng, Coolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cool" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Copperopolis' ):
                Coplng, Coplat  = ( -120.64, 37.98)
                xpt, ypt = map(Coplng, Coplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Copperopolis" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cornell' ):
                Cornlng, Cornlat  = ( -118.78, 34.11)
                xpt, ypt = map(Cornlng, Cornlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cornell" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Corona' ):
                Corlng, Corlat  = ( -117.57, 33.88)
                xpt, ypt = map(Corlng, Corlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Corona" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Corona del Mar' ):
                Cdmlng, Cdmlat  = ( -117.87, 33.60)
                xpt, ypt = map(Cdmlng, Cdmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Corona del Mar" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Corte Madera' ):
                Ctelng, Ctelat  = ( -122.53, 37.93)
                xpt, ypt = map(Ctelng, Ctelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Corte Madera" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Costa Mesa' ):
                Cmlng, Cmlat  = ( -117.92, 33.64)
                xpt, ypt = map(Cmlng, Cmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Costa Mesa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cotati' ):
                Cotlng, Cotlat  = ( -122.71, 38.33)
                xpt, ypt = map(Cotlng, Cotlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cotati" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Coto de Caza' ):
                Cclng, Cclat  = ( -117.59, 33.60)
                xpt, ypt = map(Cclng, Cclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Coto de Caza" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cottonwood' ):
                Cwlng, Cwlat  = ( -122.28, 40.39)
                xpt, ypt = map(Cwlng, Cwlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cottonwood" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Covina' or citywiththings[y] == 'West Covina' ):
                Covlng, Covlat  = ( -117.89, 34.09)
                xpt, ypt = map(Covlng, Covlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Covina" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Crescent City' ):
                Crelng, Crelat  = ( -124.20, 41.76)
                xpt, ypt = map(Crelng, Crelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cresent City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Crescent Mills' ):
                Creslng, Creslat  = ( -120.91, 40.10)
                xpt, ypt = map(Creslng, Creslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Crescent Mills" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Crestline' ):
                Crestlng, Crestlat  = ( -117.29, 34.24)
                xpt, ypt = map(Crestlng, Crestlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Crestline" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Culver City' ):
                Cullng, Cullat  = ( -118.40, 34.02)
                xpt, ypt = map(Cullng, Cullat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Culver City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Cypress' ):
                Cylng, Cylat  = ( -118.04, 33.82)
                xpt, ypt = map(Cylng, Cylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Cypress" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Daly City' ):
                Dlng, Dlat  = ( -122.27, 37.42)
                xpt, ypt = map(Dlng, Dlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Dale City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Dana Point' ):
                Dalng, Dalat  = ( -117.70, 33.47)
                xpt, ypt = map(Dalng, Dalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Dana Point" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Danville' ):
                Danlng, Danlat  = ( -122.00, 37.82)
                xpt, ypt = map(Danlng, Danlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Danville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Del Mar' ):
                Dellng, Dellat  = ( -117.27, 32.96)
                xpt, ypt = map(Dellng, Dellat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Del Mar" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Del Rosa' ):
                Delng, Delat  = ( -117.25, 34.16)
                xpt, ypt = map(Delng, Delat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Del Rosa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Desert Center' ):
                Deslng, Deslat  = ( -115.40, 33.71)
                xpt, ypt = map(Deslng, Deslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Desert Center" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Desert Hot Springs' ):
                Desslng, Desslat  = ( -116.50, 33.96)
                xpt, ypt = map(Desslng, Desslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Desert Hot Springs" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Diamond Bar' ):
                Dilng, Dilat  = ( -117.81, 34.03)
                xpt, ypt = map(Dilng, Dilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Diamond Bar" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Discovery Bay' ):
                Dislng, Dislat  = ( -121.60, 37.91)
                xpt, ypt = map(Dislng, Dislat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Discovery Bay" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Downey' ):
                Dolng, Dolat  = ( -118.13, 33.94)
                xpt, ypt = map(Dolng, Dolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Downey" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Duarte' ):
                Dulng, Dulat  = ( -117.98, 34.14)
                xpt, ypt = map(Dulng, Dulat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Duarte" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Dumont Dune National Park' ):
                Dumlng, Dumlat  = ( -116.21, 35.68)
                xpt, ypt = map(Dumlng, Dumlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Dumont Dunes" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'East Hemet' ):
                Elng, Elat  = ( -116.94, 33.74)
                xpt, ypt = map(Elng, Elat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "East Hemet" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'East Los Angeles' ):
                Ealng, Ealat  = ( -118.17, 34.02)
                xpt, ypt = map(Ealng, Ealat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "East Los Angeles" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'East Palo Alto' ):
                Easlng, Easlat  = ( -122.14, 37.47)
                xpt, ypt = map(Easlng, Easlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "East Palo Alto" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Eastvale' ):
                Eastlng, Eastlat  = ( -117.58, 33.95)
                xpt, ypt = map(Eastlng, Eastlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Eastvale" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Edwards' ):
                Edlng, Edlat  = ( -117.89, 34.92)
                xpt, ypt = map(Edlng, Edlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Edwards" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'El Cajon' or citywiththings[y] == 'EL Cajon'):
                Ejlng, Ejlat  = ( -116.96, 32.79)
                xpt, ypt = map(Ejlng, Ejlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "El Cajon" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'El Cerrito' ):
                Eclng, Eclat  = ( -122.31, 37.92)
                xpt, ypt = map(Eclng, Eclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "El Cerrito" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'El Dorato' ):
                Edlng, Edlat  = ( -120.44, 38.74)
                xpt, ypt = map(Edlng, Edlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "El Dorato" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'El Monte' or citywiththings[y] == 'South El Monte' ):
                Emlng, Emlat  = ( -118.03, 34.07)
                xpt, ypt = map(Emlng, Emlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "El Monte" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'El Segundo' ):
                Eslng, Eslat  = ( -118.42, 33.92)
                xpt, ypt = map(Eslng, Eslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "El Segundo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'El Soreno' ):
                Esslng, Esslat  = ( -118.18, 34.07)
                xpt, ypt = map(Esslng, Esslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "El Soreno" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Elk Grove' ):
                Elklng, Elklat  = ( -121.37, 38.41)
                xpt, ypt = map(Elklng, Elklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Elk Grove" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Elverta' ):
                Evlng, Evlat  = ( -121.46, 38.72)
                xpt, ypt = map(Evlng, Evlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Elverta" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Emeryville' ):
                Emylng, Emylat  = ( -122.29, 37.83)
                xpt, ypt = map(Emylng, Emylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Emeryville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Encinitas' or citywiththings[y] == 'Encinitas Carlsbad' or citywiththings[y] == 'Encintas' ):
                Enclng, Enclat  = ( -117.29,33.04)
                xpt, ypt = map(Enclng, Enclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Encinitas" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Encino' ):
                Enclng, Enclat  = ( -118.52, 34.15)
                xpt, ypt = map(Enclng, Enclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Encino" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Escalon' ):
                Esclng, Esclat  = ( -121.00, 37.80)
                xpt, ypt = map(Esclng, Esclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Escalon" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Escondido' ):
                Ecslng, Ecslat  = ( -117.09, 33.12)
                xpt, ypt = map(Ecslng, Ecslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Escondido" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Eureka' ):
                Eurlng, Eurlat  = ( -124.16, 40.80)
                xpt, ypt = map(Eurlng, Eurlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Eureka" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fair Oaks' ):
                Flng, Flat  = ( -121.27, 38.64)
                xpt, ypt = map(Flng, Flat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fair Oaks" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fairfield' ):
                Falng, Falat  = ( -122.04, 38.25)
                xpt, ypt = map(Falng, Falat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fairfield" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fall River Mills' ):
                Fallng, Fallat  = ( -121.44, 41.00)
                xpt, ypt = map(Fallng, Fallat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fall River Mills" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fallbrook' ):
                Fablng, Fablat  = ( -117.25, 33.38)
                xpt, ypt = map(Fablng, Fablat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fallbrook" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fillmore' or citywiththings[y] == 'Filmore'):
                Filng, Filat  = ( -118.92, 34.40)
                xpt, ypt = map(Filng, Filat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fillmore" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Firebaugh' ):
                Firlng, Firlat  = ( -120.46, 36.86)
                xpt, ypt = map(Firlng, Firlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Firebaugh" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Folsom' ):
                Folng, Folat  = ( -121.18, 38.68)
                xpt, ypt = map(Folng, Folat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Folsom" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fontana' ):
                Fonlng, Fonlat  = ( -117.44, 34.09)
                xpt, ypt = map(Fonlng, Fonlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fontana" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Foresthill' ):
                Forlng, Forlat  = ( -120.82, 39.02)
                xpt, ypt = map(Forlng, Forlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Foresthill" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'fort bragg' or citywiththings[y] == 'Fort Bragg' ):
                Ftlng, Ftlat  = ( -123.81, 39.45)
                xpt, ypt = map(Ftlng, Ftlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fort Bragg" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fortuna' ):
                Fnlng, Fnlat  = ( -124.16, 40.60)
                xpt, ypt = map(Fnlng, Fnlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fortuna" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fountain Valley' ):
                Fvlng, Fvlat  = ( -117.95, 33.71)
                xpt, ypt = map(Fvlng, Fvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fountain Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Frazier Park' ):
                Frlng, Frlat  = ( -118.94, 34.82)
                xpt, ypt = map(Frlng, Frlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Frazier Park" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fremont' ):
                Frelng, Frelat  = ( -121.99, 37.55)
                xpt, ypt = map(Frelng, Frelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fremont" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fresno' or citywiththings[y] == 'Fresno County' ):
                Fslng, Fslat  = ( -119.77, 36.75)
                xpt, ypt = map(Fslng, Fslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fresno" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Fullerton' ):
                Fullng, Fullat  = ( -117.92, 33.87)
                xpt, ypt = map(Fullng, Fullat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Fullerton" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Galt' ):
                Glng, Glat  = ( -121.30, 38.25)
                xpt, ypt = map(Glng, Glat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Galt" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Garden Grove' ):
                Galng, Galat  = ( -117.94, 33.77)
                xpt, ypt = map(Galng, Galat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Garden Grove" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Geyserville' ):
                Gylng, Gylat  = ( -122.90, 38.71)
                xpt, ypt = map(Gylng, Gylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Geyserville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Gilroy' ):
                Gilng, Gilat  = ( -121.57, 37.01)
                xpt, ypt = map(Gilng, Gilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Gilroy" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Glendale' ):
                Gllng, Gllat  = ( -118.26, 34.14)
                xpt, ypt = map(Gllng, Gllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Glendale" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Glendora' ):
                Glelng, Glelat  = ( -117.87, 34.14)
                xpt, ypt = map(Glelng, Glelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Glendora" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Goleta' ):
                Golng, Golat  = ( -119.83, 34.44 )
                xpt, ypt = map(Golng, Golat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Goleta" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Grand Terrace' ):
                Grlng, Grlat  = ( -117.31, 34.03)
                xpt, ypt = map(Grlng, Grlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Grand Terrace" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Granite Bay' ):
                Gralng, Gralat  = ( -121.16, 38.76)
                xpt, ypt = map(Gralng, Gralat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Granite Bay" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Grass Valley' ):
                Graslng, Graslat  = ( -121.06, 39.22)
                xpt, ypt = map(Graslng, Graslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Grass Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Grover Beach' ):
                Grolng, Grolat  = ( -120.62, 35.12)
                xpt, ypt = map(Grolng, Grolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Grover Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Gustine' ):
                Guslng, Guslat  = ( -121.00, 37.26)
                xpt, ypt = map(Guslng, Guslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Gustine" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Half Moon Bay' ):
                Hlng, Hlat  = ( -122.43, 37.46)
                xpt, ypt = map(Hlng, Hlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Half Moon Bay" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hanford' ):
                Halng, Halat  = ( -119.65, 36.33)
                xpt, ypt = map(Halng, Halat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hanford" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hawthorne' ):
                Hawlng, Hawlat  = ( -118.35, 33.92)
                xpt, ypt = map(Hawlng, Hawlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hawthorne" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hayward' ):
                Haylng, Haylat  = ( -122.08, 37.67)
                xpt, ypt = map(Haylng, Haylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hayward" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Healdsburg' ):
                Healng, Healat  = ( -122.87, 38.61)
                xpt, ypt = map(Healng, Healat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Healdsburg" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hemet' ):
                Helng, Helat  = ( -116.97, 33.75)
                xpt, ypt = map(Helng, Helat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hemet" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hermosa Beach' ):
                Herlng, Herlat  = ( -118.40, 33.86)
                xpt, ypt = map(Herlng, Herlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hermosa Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hesperia' ):
                Heslng, Heslat  = ( -117.30, 34.43)
                xpt, ypt = map(Heslng, Heslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hesperia" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hidden Valley' ):
                Hilng, Hilat  = ( -122.56, 38.81)
                xpt, ypt = map(Hilng, Hilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hidden Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Highland' or citywiththings[y] == 'Highland Park' ):
                Higlng, Higlat  = ( -117.21, 34.13)
                xpt, ypt = map(Higlng, Higlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Highland" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hinkley' ):
                Hylng, Hylat  = ( -117.20, 34.94)
                xpt, ypt = map(Hylng, Hylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hinkley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hollister' ):
                Holng, Holat  = ( -121.40, 36.85)
                xpt, ypt = map(Holng, Holat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hollister" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Hollywood' or citywiththings[y] == 'N. Hollywood' or citywiththings[y] == 'North Hollywood' or citywiththings[y] == 'West Hollywood'):
                Holllng, Holllat  = ( -118.33, 34.09)
                xpt, ypt = map(Holllng, Holllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Hollywood" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Huntington Beach' ):
                Hblng, Hblat  = ( -118.00, 33.66)
                xpt, ypt = map(Hblng, Hblat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Huntington Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Idyllwild' ):
                Ilng, Ilat  = ( -116.74, 33.74)
                xpt, ypt = map(Ilng, Ilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Idyllwild" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Imperial Beach' ):
                Iblng, Iblat  = ( -117.11, 32.58)
                xpt, ypt = map(Iblng, Iblat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Imperial Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Indio' ):
                Inlng, Inlat  = ( -116.21, 33.72)
                xpt, ypt = map(Inlng, Inlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Indio" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Irvine' ):
                Irlng, Irlat  = ( -117.79, 33.68)
                xpt, ypt = map(Irlng, Irlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Irvine" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Isla Vista' ):
                Islng, Islat  = ( -119.86, 34.41)
                xpt, ypt = map(Islng, Islat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Isla Vista" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Jackson' ):
                Jlng, Jlat  = ( -120.77, 38.35)
                xpt, ypt = map(Jlng, Jlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Jackson" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Jamul' ):
                Jalng, Jalat  = ( -116.88, 32.72)
                xpt, ypt = map(Jalng, Jalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Jamul" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Kelseyville' ):
                Klng, Klat  = ( -122.84, 38.99)
                xpt, ypt = map(Klng, Klat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Kelseyville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Kerman' ):
                Kelng, Kelat  = ( -120.06, 36.72)
                xpt, ypt = map(Kelng, Kelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Kerman" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Kings Beach' ):
                Kilng, Kilat  = ( -120.03, 39.24)
                xpt, ypt = map(Kilng, Kilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Kings Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Kingsburg' ):
                Kinlng, Kinlat  = ( -119.55, 36.51)
                xpt, ypt = map(Kinlng, Kinlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Kingsburg" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Knights Landing' ):
                Knlng, Knlat  = ( -121.72, 38.80)
                xpt, ypt = map(Knlng, Knlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Knights Landing" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'La Canada' or citywiththings[y] == 'La Canada Flintridge'):
                Llng, Llat  = ( -118.20, 34.21)
                xpt, ypt = map(Llng, Llat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "La Canada Flintridge" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'La Crescenta' ):
                Lalng, Lalat  = ( -118.24, 34.23)
                xpt, ypt = map(Lalng, Lalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "La Crescenta" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'La Habra' ):
                Lhlng, Lhlat  = ( -117.95, 33.93)
                xpt, ypt = map(Lhlng, Lhlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "La Habra" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'La Jolla' ):
                Ljlng, Ljlat  = ( -117.27, 32.83)
                xpt, ypt = map(Ljlng, Ljlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "La Jolla" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'La Mesa' ):
                Lmlng, Lmlat  = ( -117.02, 32.77)
                xpt, ypt = map(Lmlng, Lmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "La Mesa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'La Mirada' ):
                Lmilng, Lmilat  = ( -118.01, 33.92)
                xpt, ypt = map(Lmilng, Lmilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "La Mirada" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'La Puente' ):
                Lplng, Lplat  = ( -117.95, 34.02)
                xpt, ypt = map(Lplng, Lplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "La Puente" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'La Quinta' ):
                Lqlng, Lqlat  = ( -116.31, 33.66)
                xpt, ypt = map(Lqlng, Lqlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "La Quinta" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ladera Ranch' ):
                Ldlng, Ldlat  = ( -117.64, 33.55)
                xpt, ypt = map(Ldlng, Ldlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ladera Ranch" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lafayette' ):
                Lflng, Lflat  = ( -122.12, 37.89)
                xpt, ypt = map(Lflng, Lflat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lafayette" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Laguna Beach' or citywiththings[y] == 'Laguna beach'):
                Lablng, Lablat  = ( -117.78, 33.54)
                xpt, ypt = map(Lablng, Lablat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Laguna Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Laguna Niguel' ):
                Lanlng, Lanlat  = ( -117.71, 33.52)
                xpt, ypt = map(Lanlng, Lanlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Laguna Niguel" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Laguna Woods' ):
                Lwlng, Lwlat  = ( -117.73, 33.61)
                xpt, ypt = map(Lwlng, Lwlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Laguna Woods" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lake Alpine' ):
                Laalng, Laalat  = ( -120.00, 38.48)
                xpt, ypt = map(Laalng, Laalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lake Alpine" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lake Arrowhead' ):
                Laklng, Laklat  = ( -117.19, 34.25)
                xpt, ypt = map(Laklng, Laklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lake Arrowhead" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lake Elsinore' ):
                Leelng, Leelat  = ( -117.33, 33.67)
                xpt, ypt = map(Leelng, Leelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lake Elsinore" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lake Forest' ):
                Lflng, Lflat  = ( -117.69, 33.65)
                xpt, ypt = map(Lflng, Lflat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lake Forest" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lake Port' or citywiththings[y] == 'Lakeport'):
                Lplng, Lplat  = ( -122.92, 39.04)
                xpt, ypt = map(Lplng, Lplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lakeport" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lakeside' ):
                Lslng, Lslat  = ( -116.92, 32.86)
                xpt, ypt = map(Lslng, Lslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lakeside" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lakewood' ):
                Loolng, Loolat  = ( -118.13, 33.85)
                xpt, ypt = map(Loolng, Loolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lakewood" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lancaster' ):
                Lrrlng, Lrrlat  = ( -118.15, 34.69)
                xpt, ypt = map(Lrrlng, Lrrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lancaster" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lawndale' ):
                Lddlng, Lddlat  = ( -118.35, 33.89)
                xpt, ypt = map(Lddlng, Lddlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lawndale" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Laytonville' ):
                Lylng, Lylat  = ( -123.48, 39.69)
                xpt, ypt = map(Lylng, Lylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Laytonville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lemoore' ):
                Lmrlng, Lmrlat  = ( -119.78, 36.30)
                xpt, ypt = map(Lmrlng, Lmrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lemoore" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lennox' ):
                Lxlng, Lxlat  = ( -118.35, 33.94)
                xpt, ypt = map(Lxlng, Lxlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lennox" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lenwood' ):
                Lwrrlng, Lwrrlat  = ( -117.10, 34.88)
                xpt, ypt = map(Lwrrlng, Lwrrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lenwood" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lincoln' ):
                Lnlng, Lnlat  = ( -121.29, 38.89)
                xpt, ypt = map(Lnlng, Lnlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lincoln" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Litchfield' ):
                Litlng, Litlat  = ( -120.39, 40.38)
                xpt, ypt = map(Litlng, Litlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Litchfield" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Livermore' ):
                Lvrlng, Lvrlat  = ( -121.77, 37.68)
                xpt, ypt = map(Lvrlng, Lvrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Livermore" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Livingston' ):
                Lvglng, Lvglat  = ( -120.72, 37.39)
                xpt, ypt = map(Lvglng, Lvglat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Livingston" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Llano' ):
                Lllng, Lllat  = ( -117.82, 34.51)
                xpt, ypt = map(Lllng, Lllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Llano" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lodi' ):
                Lodlng, Lodlat  = ( -121.27, 38.13)
                xpt, ypt = map(Lodlng, Lodlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lodi" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Loleta' ):
                Lollng, Lollat  = ( -124.23, 40.64)
                xpt, ypt = map(Lollng, Lollat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Loleta" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Loma Linda' ):
                Lmllng, Lmllat  = ( -117.26, 34.05)
                xpt, ypt = map(Lmllng, Lmllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Loma Linda" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lomira' ):
                Lmrlng, Lmrlat  = ( -118.32, 33.79)
                xpt, ypt = map(Lmrlng, Lmrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lomita" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lompoc' ):
                Lpclng, Lpclat  = ( -120.46, 34.64)
                xpt, ypt = map(Lpclng, Lpclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lompoc" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Long Beach' or citywiththings[y] == 'Long Beach/Los Angles'):
                Lnglng, Lnglat  = ( -118.19, 33.77)
                xpt, ypt = map(Lnglng, Lnglat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Long Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Loomis' ):
                Loomlng, Loomlat  = ( -121.19, 38.82)
                xpt, ypt = map(Loomlng, Loomlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Loomis" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Los Alamitos' ):
                Llalng, Llalat  = ( -118.07, 33.80)
                xpt, ypt = map(Llalng, Llalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Los Alamitos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Los Alamos' ):
                Lsalng, Lsalat  = ( -120.28, 34.74)
                xpt, ypt = map(Lsalng, Lsalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Los Alamos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Los Angeles' or citywiththings[y] == 'Los Angeles/Burbank/Palmdale' or citywiththings[y] == 'West Los Angeles' or citywiththings[y] == 'Westchester'):
                Losalng, Losalat  = ( -118.24, 34.05)
                xpt, ypt = map(Losalng, Losalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Los Angeles" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Los Banos' ):
                Lbalng, Lbalat  = ( -120.85, 37.06)
                xpt, ypt = map(Lbalng, Lbalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Los Banos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Los Gatos' ):
                Lgatolng, Lgatolat  = ( -121.96, 37.24)
                xpt, ypt = map(Lgatolng, Lgatolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Los Gatos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Los Olivos' ):
                Llvlng, Llvlat  = ( -120.12, 34.67)
                xpt, ypt = map(Llvlng, Llvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Los Olivos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lucerne Valley' ):
                Luvlng, Luvlat  = ( -116.97, 34.44)
                xpt, ypt = map(Luvlng, Luvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lucerne Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Lynwood' ):
                Lynlng, Lynlat  = ( -118.21, 33.93)
                xpt, ypt = map(Lynlng, Lynlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Lynwood" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Madera' or citywiththings[y] == 'Madera Ranchos' ):
                Mlng, Mlat  = ( -120.06, 36.96)
                xpt, ypt = map(Mlng, Mlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Madera" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Magalia' ):
                Mglng, Mglat  = ( -121.588, 39.81)
                xpt, ypt = map(Mglng, Mglat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Magalia" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Malibu' ):
                Mallng, Mallat  = ( -118.78, 34.03)
                xpt, ypt = map(Mallng, Mallat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Malibu" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mammoth Lakes' ):
                Mamlng, Mamlat  = ( -118.97, 37.65)
                xpt, ypt = map(Mamlng, Mamlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mammoth Lakes" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Manhattan Beach' ):
                Mthlng, Mthlat  = ( -118.41, 33.88)
                xpt, ypt = map(Mthlng, Mthlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Manhattan Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Manteca' ):
                Mtelng, Mtelat  = ( -121.22, 37.80)
                xpt, ypt = map(Mtelng, Mtelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Manteca" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Marin County' ):
                Mrnlng, Mrnlat  = ( -122.76, 38.08)
                xpt, ypt = map(Mrnlng, Mrnlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Marin County" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Marina del Rey' or citywiththings[y] == 'Marina Del Rey' ):
                Mdrlng, Mdrlat  = ( -118.45, 33.98)
                xpt, ypt = map(Mdrlng, Mdrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Marina del Rey" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mariposa' ):
                Mpolng, Mpolat  = ( -119.97, 37.48)
                xpt, ypt = map(Mpolng, Mpolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mariposa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Martinez' ):
                Mzlng, Mzlat  = ( -122.13, 38.02)
                xpt, ypt = map(Mzlng, Mzlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Martinez" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Marysville' ):
                Mvlng, Mvlat  = ( -121.59, 39.15)
                xpt, ypt = map(Mvlng, Mvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Marysville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Maywood' ):
                Mdlng, Mdlat  = ( -118.19, 33.99)
                xpt, ypt = map(Mdlng, Mdlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Maywood" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mckittrick' ):
                Mcklng, Mcklat  = ( -119.62, 35.31)
                xpt, ypt = map(Mcklng, Mcklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mckittrick" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mecca' ):
                Mecclng, Mecclat  = ( -116.08, 33.57)
                xpt, ypt = map(Mecclng, Mecclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mecca" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Menifee' or citywiththings == 'Menifeeca' ):
                Mfeelng, Mfeelat  = ( -117.19, 33.70)
                xpt, ypt = map(Mfeelng, Mfeelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Menifee" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mentone' ):
                Mtnelng, Mtnelat  = ( -117.13, 34.07)
                xpt, ypt = map(Mtnelng, Mtnelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mentone" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Merced' ):
                Merclng, Merclat  = ( -120.48, 37.30)
                xpt, ypt = map(Merclng, Merclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Merced" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mercy Hot Springs' ):
                Mhslng, Mhslat  = ( -120.85, 36.70)
                xpt, ypt = map(Mhslng, Mhslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mercey Hot Springs" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Milpitas' ):
                Milplng, Milplat  = ( -121.90, 37.43)
                xpt, ypt = map(Milplng, Milplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Milpitas" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mira Loma' ):
                Miralng, Miralat  = ( -117.52, 33.98)
                xpt, ypt = map(Miralng, Miralat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mira Loma" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mission Viejo' ):
                Mvvlng, Mvvlat  = ( -117.667, 33.60)
                xpt, ypt = map(Mvvlng, Mvvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mission Viejo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Modesto' ):
                Mooolng, Mooolat  = ( -121.00, 37.64)
                xpt, ypt = map(Mooolng, Mooolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Modesto" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mojave' ):
                Mjvlng, Mjvlat  = ( -118.17, 35.05)
                xpt, ypt = map(Mjvlng, Mjvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mojave" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Monrovia' ):
                Mvilng, Mvilat  = ( -118.00, 34.14)
                xpt, ypt = map(Mvilng, Mvilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Monrovia" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Montague' ):
                Mtgelng, Mtgelat  = ( -122.53, 41.73)
                xpt, ypt = map(Mtgelng, Mtgelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Montague" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Montara' ):
                Mtatalng, Mtatalat  = ( -122.52, 37.54)
                xpt, ypt = map(Mtatalng, Mtatalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Montara" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Montclair' ):
                Mairlng, Mairlat  = ( -117.69, 34.08)
                xpt, ypt = map(Mairlng, Mairlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Montclair" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Montebello' ):
                Mllolng, Mllolat  = ( -118.11, 34.02)
                xpt, ypt = map(Mllolng, Mllolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Montebello" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Monterey' or citywiththings[y] == 'Monterey Bay' or citywiththings[y] == 'Monterey Park' ):
                Mterlng, Mterlat  = ( -121.89, 36.60)
                xpt, ypt = map(Mterlng, Mterlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Monterey Bay" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Moorpark' ):
                Mpklng, Mpklat  = ( -118.88, 34.29)
                xpt, ypt = map(Mpklng, Mpklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Moorpark" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Moreno Valley' ):
                Mvllng, Mvllat  = ( -117.23, 33.94)
                xpt, ypt = map(Mvllng, Mvllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Moreno Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Morgan Hill' ):
                Mghlng, Mghlat  = ( -121.65, 37.13)
                xpt, ypt = map(Mghlng, Mghlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Morgan Hill" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Moro Bay' or citywiththings[y] == 'Morro Bay'):
                Morrlng, Morrlat  = ( -120.85, 35.37)
                xpt, ypt = map(Morrlng, Morrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Morro Bay" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Morongo Valley' ):
                Mrvlllng, Mrvlllat  = ( -116.58, 34.05)
                xpt, ypt = map(Mrvlllng, Mrvlllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Morongo Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mount Shasta' or citywiththings == 'Mt. Shasta' ):
                Mshhlng, Mshhlat  = ( -122.31, 41.31)
                xpt, ypt = map(Mshhlng, Mshhlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mount Shasta" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mountain View' ):
                Mtnvlng, Mtnvlat  = ( -122.08, 37.39)
                xpt, ypt = map(Mtnvlng, Mtnvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mountain View" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Mt. Laguna' ):
                Mtnlllng, Mtnlllat  = ( -116.42, 32.87)
                xpt, ypt = map(Mtnlllng, Mtnlllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mount Laguna" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Murrieta' or citywiththings[y] == 'Murrietta' ):
                Murrrlng, Murrrlat  = ( -117.21, 33.55)
                xpt, ypt = map(Murrrlng, Murrrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Murrieta" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Napa' ):
                Nlng, Nlat  = ( -122.29, 38.30)
                xpt, ypt = map(Nlng, Nlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Napa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'National City' ):
                Nalng, Nalat  = ( -117.10, 32.68)
                xpt, ypt = map(Nalng, Nalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "National City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Near Woody' ):
                NWWlng, NWWlat  = ( -118.83, 35.70)
                xpt, ypt = map(NWWlng, NWWlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Woody" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Needles' ):
                Neelng, Neelat  = ( -114.61, 34.85)
                xpt, ypt = map(Neelng, Neelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Needles" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Newberry Springs' ):
                Newlng, Newlat  = ( -116.69, 34.83)
                xpt, ypt = map(Newlng, Newlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Newberry Springs" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Newbury Park' ):
                Newplng, Newplat  = ( -118.91, 34.18)
                xpt, ypt = map(Newplng, Newplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Newbury Park" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Newhall' ):
                Newhlng, Newhlat  = ( -118.53, 34.38)
                xpt, ypt = map(Newhlng, Newhlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Newhall" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Newman' ):
                Newmlng, Newmlat  = ( -121.02, 37.31)
                xpt, ypt = map(Newmlng, Newmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Newman" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Newport Beach' ):
                Nwblng, Nwblat  = ( -117.93, 33.62)
                xpt, ypt = map(Nwblng, Nwblat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Newport Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Nipomo' ):
                Noplng, Noplat  = ( -120.48, 35.04)
                xpt, ypt = map(Noplng, Noplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Nipomo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Norwalk' ):
                Norlng, Norlat  = ( -118.08, 33.90)
                xpt, ypt = map(Norlng, Norlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Norwalk" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Novato' ):
                Novlng, Novlat  = ( -122.57, 38.11)
                xpt, ypt = map(Novlng, Novlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Novato" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Nuevo' ):
                Nulng, Nulat  = ( -117.15, 33.80)
                xpt, ypt = map(Nulng, Nulat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Nuevo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Oakdale' ):
                Olng, Olat  = ( -120.85, 37.77)
                xpt, ypt = map(Olng, Olat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Oakdale" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Oakland' ):
                Oalng, Oalat  = ( -122.27, 37.80)
                xpt, ypt = map(Oalng, Oalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Oakland" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Oakley' ):
                Oklng, Oklat  = ( -121.71, 38.00)
                xpt, ypt = map(Oklng, Oklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Oakley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ocean Beach' ):
                OBlng, OBlat  = ( -117.25, 32.75)
                xpt, ypt = map(OBlng, OBlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ocean Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ocean Cove' ):
                OClng, OClat  = ( -123.30, 38.56)
                xpt, ypt = map(OClng, OClat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ocean Cove" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Oceano' ):
                Oolng, Oolat  = ( -120.61, 35.10)
                xpt, ypt = map(Oolng, Oolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Oceano" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Oceanside' ):
                Osslng, Osslat  = ( -117.38, 33.20)
                xpt, ypt = map(Osslng, Osslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Oceanside" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Oildale' ):
                Oilng, Oilat  = ( -119.02, 35.42)
                xpt, ypt = map(Oilng, Oilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Oildale" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ontario' ):
                Ontlng, Ontlat  = ( -117.65, 34.06)
                xpt, ypt = map(Ontlng, Ontlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ontario" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Orange' or citywiththings[y] == 'Orange County' or citywiththings[y] == 'Orange County area'):
                Orglng, Orglat  = ( -117.85, 33.79)
                xpt, ypt = map(Orglng, Orglat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Orange" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Orangevale' ):
                Oralng, Oralat  = ( -121.23, 38.68)
                xpt, ypt = map(Oralng, Oralat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Orangevale" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Organ House' ):
                OrHlng, OrHlat  = ( -121.27, 39.34)
                xpt, ypt = map(OrHlng, OrHlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Oregon House" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Orland' ):
                Orllng, Orllat  = ( -122.20, 39.75)
                xpt, ypt = map(Orllng, Orllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Orland" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Orville' ):
                Orvlng, Orvlat  = ( -121.56, 39.51)
                xpt, ypt = map(Orvlng, Orvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Orville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Otay Mesa' ):
                Otalng, Otalat  = ( -116.97, 32.56)
                xpt, ypt = map(Otalng, Otalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Otay" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Oxnard' ):
                Oxlng, Oxlat  = ( -119.18, 34.20)
                xpt, ypt = map(Oxlng, Oxlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Oxnard" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ozena' ):
                Ozlng, Ozlat  = ( -119.33, 34.69)
                xpt, ypt = map(Ozlng, Ozlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ozena Campground" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pacheco' ):
                Plng, Plat  = ( -122.08, 37.98)
                xpt, ypt = map(Plng, Plat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pacheco" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pacific Grove' ):
                Pclng, Pclat  = ( -121.92, 36.62)
                xpt, ypt = map(Pclng, Pclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pacific Grove" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pacifica' ):
                Pflng, Pflat  = ( -122.49, 37.61)
                xpt, ypt = map(Pflng, Pflat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pacifica" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pacoima' ):
                Paclng, Paclat  = ( -118.41, 34.78)
                xpt, ypt = map(Paclng, Paclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pacoima" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Palm Desert' ):
                Palmlng, Palmlat  = ( -116.37, 33.72)
                xpt, ypt = map(Palmlng, Palmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Palm Desert" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Palm Springs' ):
                PSlng, PSlat  = ( -116.55, 33.83)
                xpt, ypt = map(PSlng, PSlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Palm Springs" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Palmdale' ):
                Pdalng, Pdalat  = ( -118.12, 34.58)
                xpt, ypt = map(Pdalng, Pdalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Palmdale" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Palo Alto' ):
                PAllng, PAllat  = ( -122.14, 37.44)
                xpt, ypt = map(PAllng, PAllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Palo Alto" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Paradise' ):
                Pdilng, Pdilat  = ( -121.62, 39.76)
                xpt, ypt = map(Pdilng, Pdilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Paradise" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Paramount' ):
                Paralng, Paralat  = ( -118.16, 33.89)
                xpt, ypt = map(Paralng, Paralat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Paramount" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pasadena' ):
                Pnalng, Pnalat  = ( -118.14, 34.15)
                xpt, ypt = map(Pnalng, Pnalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pasadena" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Paso Robles' ):
                Psrlng, Psrlat  = ( -120.65, 35.64)
                xpt, ypt = map(Psrlng, Psrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Paso Robles" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Patterson' ):
                Pttlng, Pttlat  = ( -121.13, 37.47)
                xpt, ypt = map(Pttlng, Pttlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Patterson" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pearblossom' ):
                Psslng, Psslat  = ( -117.91, 34.51)
                xpt, ypt = map(Psslng, Psslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pearblossom" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Perris' ):
                Prrslng, Prrslat  = ( -117.23, 33.78)
                xpt, ypt = map(Prrslng, Prrslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Perris" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Petaluma' ):
                Petalng, Petalat  = ( -122.64, 38.23)
                xpt, ypt = map(Petalng, Petalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Petaluma" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Phelan' ):
                Phlng, Phlat  = ( -117.57, 34.43)
                xpt, ypt = map(Phlng, Phlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Phelan" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pico Rivera' ):
                Pcolng, Pcolat  = ( -118.10, 33.98)
                xpt, ypt = map(Pcolng, Pcolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pico Rivera" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pilot Hill' or citywiththings[y] == 'Pilot hill' ):
                PHilng, PHilat  = ( -121.01, 38.83)
                xpt, ypt = map(PHilng, PHilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pilot Hill" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pine Grove' ):
                PGlng, PGlat  = ( -120.66, 38.41)
                xpt, ypt = map(PGlng, PGlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pine Grove" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pine Mountain Club' ):
                PMClng, PMClat  = ( -119.16, 34.85)
                xpt, ypt = map(PMClng, PMClat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pine Mountain Club" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pinion Hills' or citywiththings[y] == 'Pinon Hills' ):
                Pinlng, Pinlat  = ( -117.65, 34.43)
                xpt, ypt = map(Pinlng, Pinlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pinon Hills" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pismo' ):
                Psmlng, Psmlat  = ( -120.64, 35.14)
                xpt, ypt = map(Psmlng, Psmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pismo Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Placentia' ):
                Pcelng, Pcelat  = ( -117.87, 33.87)
                xpt, ypt = map(Pcelng, Pcelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Placentia" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Placerville' ):
                Pvlllng, Pvlllat  = ( -120.80, 38.73)
                xpt, ypt = map(Pvlllng, Pvlllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Placerville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Play Vista' or citywiththings[y] == 'Playa Vista'):
                Playlng, Playlat  = ( -118.43, 33.97)
                xpt, ypt = map(Playlng, Playlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Playa Vista" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pleasanton' ):
                Ptonlng, Ptonlat  = ( -121.87, 37.66)
                xpt, ypt = map(Ptonlng, Ptonlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pleasanton" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Pollock Pines' ):
                Polllng, Polllat  = ( -120.59, 38.76)
                xpt, ypt = map(Polllng, Polllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Pollock Pines" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ponoma' ):
                Pnmlng, Pnmlat  = ( -117.75, 34.06)
                xpt, ypt = map(Pnmlng, Pnmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ponoma" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Port Hueneme' ):
                Phuelng, Phuelat  = ( -119.20, 34.15)
                xpt, ypt = map(Phuelng, Phuelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Port Hueneme" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Porterville' ):
                Porrlng, Porrlat  = ( -119.02, 36.07)
                xpt, ypt = map(Porrlng, Porrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Porterville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Potter Valley' ):
                Pottlng, Pottlat  = ( -123.11, 39.32)
                xpt, ypt = map(Pottlng, Pottlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Potter Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Poway' ):
                Powlng, Powlat  = ( -117.04, 32.96)
                xpt, ypt = map(Powlng, Powlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Poway" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Quincy' ):
                Qlng, Qlat  = ( -117.04, 32.96)
                xpt, ypt = map(Qlng, Qlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Quincy" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ramona' ):
                Rlng, Rlat  = ( -116.88, 33.04)
                xpt, ypt = map(Rlng, Rlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ramona" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rancho Bernardo' ):
                Rblng, Rblat  = ( -117.08, 33.03)
                xpt, ypt = map(Rblng, Rblat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rancho Bernardo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rancho Cordova' ):
                Rclng, Rclat  = ( -121.30, 38.59)
                xpt, ypt = map(Rclng, Rclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rancho Cordova" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rancho Cucamonga' ):
                Rcalng, Rcalat  = ( -117.59, 34.11)
                xpt, ypt = map(Rcalng, Rcalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rancho Cucamonga" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rancho Mirage' ):
                Rmlng, Rmlat  = ( -116.41, 33.74)
                xpt, ypt = map(Rmlng, Rmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rancho Mirage" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ranchos Palos Verdes' ):
                Rplng, Rplat  = ( -118.39, 33.74)
                xpt, ypt = map(Rplng, Rplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ranchos Palos Verdes" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rancho Santa Margarita' ):
                Rsmlng, Rsmlat  = ( -117.60, 33.64)
                xpt, ypt = map(Rsmlng, Rsmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rancho Santa Margarita" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Red Bluff' ):
                Redlng, Redlat  = ( -122.24, 40.18)
                xpt, ypt = map(Redlng, Redlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Red Bluff" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Redding' ):
                Reddlng, Reddlat  = ( -122.39, 40.59)
                xpt, ypt = map(Reddlng, Reddlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Redding" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Redlands' ):
                Redllng, Redllat  = ( -117.18, 34.06)
                xpt, ypt = map(Redllng, Redllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Redlands" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Redondo Beach' ):
                Rbblng, Rbblat  = ( -118.39, 33.85)
                xpt, ypt = map(Rbblng, Rbblat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Redondo Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Redwood City' or citywiththings[y] == 'Redwood Valley' ):
                Rclng, Rclat  = ( -122.24, 37.49)
                xpt, ypt = map(Rclng, Rclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Redwood City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Reedley' ):
                Reelng, Reelat  = ( -119.45, 36.60)
                xpt, ypt = map(Reelng, Reelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Reedley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Reseda' ):
                Reslng, Reslat  = ( -118.54, 34.20)
                xpt, ypt = map(Reslng, Reslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Reseda" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rialto' ):
                Rialng, Rialat  = ( -117.37, 34.11)
                xpt, ypt = map(Rialng, Rialat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rialto" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ridgecrest' ):
                Ridlng, Ridlat  = ( -117.67, 35.62)
                xpt, ypt = map(Ridlng, Ridlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ridgecrest" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rio Del Mar' ):
                Riolng, Riolat  = ( -121.88, 36.96)
                xpt, ypt = map(Riolng, Riolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rio Del Mar" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rio Dell' ):
                Rdellng, Rdellat  = ( -124.11, 40.50)
                xpt, ypt = map(Rdellng, Rdellat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rio Dell" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rio Linda' ):
                Rlinlng, Rlinlat  = ( -121.45, 38.69)
                xpt, ypt = map(Rlinlng, Rlinlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rio Linda" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rio Vista' ):
                Rvislng, Rvislat  = ( -121.69, 38.16)
                xpt, ypt = map(Rvislng, Rvislat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rio Vista" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ripon' ):
                Riplng, Riplat  = ( -121.14, 37.74)
                xpt, ypt = map(Riplng, Riplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ripon" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Riverbank' ):
                Rivlng, Rivlat  = ( -120.94, 37.74)
                xpt, ypt = map(Rivlng, Rivlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Riverbank" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Riverside' ):
                Rsdlng, Rsdlat  = ( -117.40, 33.95)
                xpt, ypt = map(Rsdlng, Rsdlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Riverside" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rocklin') :
                Rcklng, Rcklat  = ( -121.24, 38.71)
                xpt, ypt = map(Rcklng, Rcklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rocklin" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rohnert Park' or citywiththings[y] == 'Rohnert park' ):
                Rohnlng, Rohnlat  = ( -122.70, 38.34)
                xpt, ypt = map(Rohnlng, Rohnlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rohnert Park" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rosamond' ):
                Rsalng, Rsalat  = ( -118.16, 34.86)
                xpt, ypt = map(Rsalng, Rsalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rosamond" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rosemead' ):
                Roselng, Roselat  = ( -118.07, 34.08)
                xpt, ypt = map(Roselng, Roselat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rosemead" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Roseville' ):
                Rosvlng, Rosvlat  = ( -121.29, 38.75)
                xpt, ypt = map(Rosvlng, Rosvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Roseville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rough and Ready' ):
                RRlng, RRlat  = ( -121.14, 39.23)
                xpt, ypt = map(RRlng, RRlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rough and Ready" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Rubidoux' ):
                Rxxlng, Rxxlat  = ( -117.43, 34.00)
                xpt, ypt = map(Rxxlng, Rxxlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Rubidoux" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sacramento' or citywiththings[y] == 'North Highlands' or citywiththings[y] == 'North Sacramento' or citywiththings[y] == 'West Sacramento'):
                Slng, Slat  = ( -121.49, 38.58)
                xpt, ypt = map(Slng, Slat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sacramento" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Salinas' ):
                Salng, Salat  = ( -121.66, 36.68)
                xpt, ypt = map(Salng, Salat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Salinas" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Salton City' or citywiththings[y] == 'Salton Sea' or citywiththings[y] == 'Salton Sea Beach' ):
                SClng, SClat  = ( -115.96, 33.30)
                xpt, ypt = map(SClng, SClat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Salton City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Anselmo' ):
                SAlng, SAlat  = ( -122.56, 37.98)
                xpt, ypt = map(SAlng, SAlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Anselmo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Bernardino' ):
                SBlng, SBlat  = ( -117.29, 34.11)
                xpt, ypt = map(SBlng, SBlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Bernardino" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Carlos' ):
                SCClng, SCClat  = ( -122.26, 37.51)
                xpt, ypt = map(SCClng, SCClat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Carlos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Clemente' ):
                SCllng, SCllat  = ( -117.61, 33.43)
                xpt, ypt = map(SCllng, SCllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Clemente" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Diego' or citywiththings[y] == 'San diego'):
                SDlng, SDlat  = ( -117.16, 32.72)
                xpt, ypt = map(SDlng, SDlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Diego" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Dimas' ):
                SDilng, SDilat  = ( -117.81, 34.11)
                xpt, ypt = map(SDilng, SDilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Dimas" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Fernando' or citywiththings[y] == 'San Fernando Valley' ):
                SFelng, SFelat  = ( -118.44, 34.18)
                xpt, ypt = map(SFelng, SFelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Fernando" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Francisco' ):
                SFlng, SFlat  = ( -122.42, 37.77)
                xpt, ypt = map(SFlng, SFlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Francisco" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Gabriel' or citywiththings[y] == 'San Gabriel Valley' ):
                SGlng, SGlat  = ( -118.11, 34.10)
                xpt, ypt = map(SGlng, SGlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Gabriel" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Jacinto' ):
                SJalng, SJalat  = ( -116.96, 33.78)
                xpt, ypt = map(SJalng, SJalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Jacinto" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Jose' ):
                SJlng, SJlat  = ( -121.89, 37.34)
                xpt, ypt = map(SJlng, SJlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Jose" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Juan Capistrano' ):
                SJClng, SJClat  = ( -117.66, 33.50)
                xpt, ypt = map(SJClng, SJClat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Juan Capistrano" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Leandro' ):
                SLlng, SLlat  = ( -122.16, 37.72)
                xpt, ypt = map(SLlng, SLlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Leandro" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Luis Obispo' ):
                SLOlng, SLOlat  = ( -120.66, 35.28)
                xpt, ypt = map(SLOlng, SLOlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Luis Obispo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Marcos' or citywiththings[y] == 'San Marcos/Vista' ):
                SMMlng, SMMlat  = ( -117.17, 33.14)
                xpt, ypt = map(SMMlng, SMMlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Marcos" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Mateo' ):
                SMlng, SMlat  = ( -122.33, 37.56)
                xpt, ypt = map(SMlng, SMlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Mateo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Pablo' ):
                SPlng, SPlat  = ( -122.35, 37.96)
                xpt, ypt = map(SPlng, SPlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Pablo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Pedro' ):
                SPelng, SPelat  = ( -118.29, 33.74)
                xpt, ypt = map(SPelng, SPelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Pedro" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Rafael' ):
                SRlng, SRlat  = ( -122.53, 37.97)
                xpt, ypt = map(SRlng, SRlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Rafael" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Ramon' ):
                SRRlng, SRRlat  = ( -121.98, 37.78)
                xpt, ypt = map(SRRlng, SRRlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Ramon" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Ysidro' ):
                SYlng, SYlat  = ( -117.05, 32.56)
                xpt, ypt = map(SYlng, SYlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Ysidro" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Ana' ):
                SAnlng, SAnlat  = ( -117.87, 33.75)
                xpt, ypt = map(SAnlng, SAnlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Ana" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Barbara' or citywiththings[y] == 'Santa Barbara County'):
                SBalng, SBalat  = ( -119.70, 34.42)
                xpt, ypt = map(SBalng, SBalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Barbara" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Clara' ):
                SCllng, SCllat  = ( -121.96, 37.35)
                xpt, ypt = map(SCllng, SCllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Clara" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'San Clarita' ):
                SCrlng, SCrlat  = ( -118.54, 34.39)
                xpt, ypt = map(SCrlng, SCrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "San Clarita" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Cruz' ):
                SCClng, SCClat  = ( -118.54, 34.39)
                xpt, ypt = map(SCClng, SCClat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Cruz" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Fe' ):
                SaFlng, SaFlat  = ( -117.20, 33.02)
                xpt, ypt = map(SaFlng, SaFlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Fe" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Maria' ):
                SMalng, SMalat  = ( -120.44, 34.95)
                xpt, ypt = map(SMalng, SMalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Maria" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Monica' ):
                SMclng, SMclat  = ( -118.49, 34.02)
                xpt, ypt = map(SMclng, SMclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Monica" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Paula' ):
                SPPlng, SPPlat  = ( -119.06, 34.35)
                xpt, ypt = map(SPPlng, SPPlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Paula" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Rosa' ):
                SRalng, SRalat  = ( -122.71, 38.44)
                xpt, ypt = map(SRalng, SRalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Rosa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santa Ysabel' ):
                SYblng, SYblat  = ( -116.67, 33.11)
                xpt, ypt = map(SYblng, SYblat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santa Ysabel" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Santee' ):
                Steelng, Steelat  = ( -116.97, 32.84)
                xpt, ypt = map(Steelng, Steelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Santee" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Saratoga' ):
                Stogalng, Stogalat  = ( -122.02, 37.26)
                xpt, ypt = map(Stogalng, Stogalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Saratoga" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Saugus' ):
                Saulng, Saulat  = ( -118.54, 34.41)
                xpt, ypt = map(Saulng, Saulat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Saugus" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Seal Beach' ):
                SeaBlng, SeaBlat  = ( -118.10, 33.74)
                xpt, ypt = map(SeaBlng, SeaBlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Seal Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sears Point Raceway' ):
                SPRlng, SPRlat  = ( -122.45, 38.16)
                xpt, ypt = map(SPRlng, SPRlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sonoma Raceway" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sebastopol' ):
                Spollng, Spollat  = ( -122.82, 38.40)
                xpt, ypt = map(Spollng, Spollat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sebastopol" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Shafter' ):
                Saftlng, Saftlat  = ( -119.27, 35.50)
                xpt, ypt = map(Saftlng, Saftlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Shafter" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Shasta City' or citywiththings[y] == 'Shasta Lake'):
                SCLlng, SCLlat  = ( -122.31, 41.31)
                xpt, ypt = map(SCLlng, SCLlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Mount Shasta" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Shell Beach' ):
                Shhlng, Shhlat  = ( -120.67, 35.16)
                xpt, ypt = map(Shhlng, Shhlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Shell Beach" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sherman Oaks' ):
                ShOlng, ShOlat  = ( -118.45, 34.15)
                xpt, ypt = map(ShOlng, ShOlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sherman Oaks" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Signal Hill' ):
                SHlllng, SHlllat  = ( -118.17, 33.80)
                xpt, ypt = map(SHlllng, SHlllat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Signal Hill" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Simi Valley' ):
                Similng, Similat  = ( -118.78, 34.27)
                xpt, ypt = map(Similng, Similat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Simi Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sky Valley' ):
                Skylng, Skylat  = ( -116.35, 33.89)
                xpt, ypt = map(Skylng, Skylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sky Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Soledad' ):
                Sdadlng, Sdadlat  = ( -121.33, 36.42)
                xpt, ypt = map(Sdadlng, Sdadlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Soledad" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Solromar' ):
                Smarlng, Smarlat  = ( -118.95, 34.05)
                xpt, ypt = map(Smarlng, Smarlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Solromar" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Somis' ):
                Sislng, Sislat  = ( -119.00, 34.26)
                xpt, ypt = map(Sislng, Sislat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Somis" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sonoma' or citywiththings[y] == 'West Sonoma County' ):
                Smaalng, Smaalat  = ( -122.46, 38.29)
                xpt, ypt = map(Smaalng, Smaalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sonoma" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'South Gate' or citywiththings[y] == 'Southgate' ):
                SGalng, SGalat  = ( -118.21, 33.95)
                xpt, ypt = map(SGalng, SGalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "South Gate" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'South Lake Tahoe' ):
                SLTlng, SLTlat  = ( -119.98, 38.94)
                xpt, ypt = map(SLTlng, SLTlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "South Lake Tahoe" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'South Los Angeles' ):
                SLAalng, SLAalat  = ( -118.24, 34.05)
                xpt, ypt = map(SLAalng, SLAalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "South Los Angeles" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Spring Valley' ):
                SVlng, SVlat  = ( -117.00, 32.74)
                xpt, ypt = map(SVlng, SVlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Spring Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Stanford' ):
                Sfolng, Sfolat  = ( -122.17, 37.42)
                xpt, ypt = map(Sfolng, Sfolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Stanford" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Stockton' ):
                Stonlng, Stonlat  = ( -121.29, 37.96)
                xpt, ypt = map(Stonlng, Stonlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Stockton" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sultana' ):
                Stanalng, Stanalat  = ( -119.34, 36.55)
                xpt, ypt = map(Stanalng, Stanalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sultana" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Summerland' ):
                Smmlng, Smmlat  = ( -119.59, 34.42)
                xpt, ypt = map(Smmlng, Smmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Summerland" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sun Valley' ):
                SVunlng, SVunlat  = ( -118.38, 34.23)
                xpt, ypt = map(SVunlng, SVunlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sun Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sunnyvale' ):
                Sunnlng, Sunnlat  = ( -122.04, 37.67)
                xpt, ypt = map(Sunnlng, Sunnlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sunnyvale" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Susanville' ):
                Suslng, Suslat  = ( -120.65, 40.42)
                xpt, ypt = map(Suslng, Suslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Susanville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Sylmar' ):
                Sylmlng, Sylmlat  = ( -118.46, 34.31)
                xpt, ypt = map(Sylmlng, Sylmlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Sylmar" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Tarzana' ):
                Tlng, Tlat  = ( -118.55, 34.15)
                xpt, ypt = map(Tlng, Tlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Tarzana" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Tahachapi' ):
                Tilng, Tilat  = ( -118.45, 35.13)
                xpt, ypt = map(Tilng, Tilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Tahachapi" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Tehama' ):
                Talng, Talat  = ( -122.12, 40.03)
                xpt, ypt = map(Talng, Talat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Tehama" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Temecula' ):
                Tmalng, Tmalat  = ( -117.15, 33.49)
                xpt, ypt = map(Tmalng, Tmalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Temecula" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Temple City' or citywiththings[y] == 'Temple City/Arcadia' ):
                TClng, TClat  = ( -118.06, 34.11)
                xpt, ypt = map(TClng, TClat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Temple City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Templeton' ):
                Ttonlng, Ttonlat  = ( -120.71, 35.55)
                xpt, ypt = map(Ttonlng, Ttonlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Templeton" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Thousand Oaks' ):
                TOlng, TOlat  = ( -118.84, 34.17)
                xpt, ypt = map(TOlng, TOlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Thousand Oaks" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Three Rivers' ):
                TRlng, TRlat  = ( -118.90, 36.44)
                xpt, ypt = map(TRlng, TRlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Three Rivers" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Toluca Lake' ):
                Tcalng, Tcalat  = ( -118.35, 34.15)
                xpt, ypt = map(Tcalng, Tcalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Toluca Lake" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Topaga' or citywiththings[y] == 'Topanga Beach' ):
                Tngalng, Tngalat  = ( -118.60, 34.09)
                xpt, ypt = map(Tngalng, Tngalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Topanga" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Torrance' ):
                Trrlng, Trrlat  = ( -118.34, 33.84)
                xpt, ypt = map(Trrlng, Trrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Torrance" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Tracy' ):
                Traclng, Traclat  = ( -121.43, 37.74)
                xpt, ypt = map(Traclng, Traclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Tracy" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Trinidad' ):
                Tdadlng, Tdadlat  = ( -124.14, 41.06)
                xpt, ypt = map(Tdadlng, Tdadlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Trinidad" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Truckee' ):
                Trulng, Trulat  = ( -120.18, 39.33)
                xpt, ypt = map(Trulng, Trulat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Truckee" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Tujunga' ):
                Tjalng, Tjalat  = ( -118.31, 34.26)
                xpt, ypt = map(Tjalng, Tjalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Tujunga" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Turlock' ):
                Tlocklng, Tlocklat  = ( -120.85, 37.49)
                xpt, ypt = map(Tlocklng, Tlocklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Turlock" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Tustin' ):
                Ttinlng, Ttinlat  = ( -117.83, 33.75)
                xpt, ypt = map(Ttinlng, Ttinlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Tustin" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ukiah' ):
                Ulng, Ulat  = ( -123.21, 39.15)
                xpt, ypt = map(Ulng, Ulat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ukiah" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'University City' ):
                Unlng, Unlat  = ( -117.21, 32.86)
                xpt, ypt = map(Unlng, Unlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "University City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Upland' ):
                Uplng, Uplat  = ( -117.65, 34.10)
                xpt, ypt = map(Uplng, Uplat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Upland" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Vacaville' ):
                Vlng, Vlat  = ( -121.99, 38.36)
                xpt, ypt = map(Vlng, Vlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Vacaville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Vallejo' ):
                Valng, Valat  = ( -122.26, 38.10)
                xpt, ypt = map(Valng, Valat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Vallejo" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Valley Springs' ):
                VSlng, VSlat  = ( -120.83, 38.19)
                xpt, ypt = map(VSlng, VSlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Valley Springs" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Valley Village' ):
                VVlng, VVlat  = ( -118.38, 34.16)
                xpt, ypt = map(VVlng, VVlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Valley Village" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Van Nuys' or citywiththings[y] == 'Vannuys'):
                VNlng, VNlat  = ( -118.45, 34.19)
                xpt, ypt = map(VNlng, VNlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Van Nuys" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Vandenberg Village' ):
                VVVlng, VVVlat  = ( -120.47, 34.71)
                xpt, ypt = map(VVVlng, VVVlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Vandenberg Village" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Venice' or citywiththings[y] == 'Venice beach'):
                Velng, Velat  = ( -118.47, 33.99)
                xpt, ypt = map(Velng, Velat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Venice" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Ventura' ):
                Vrrlng, Vrrlat  = ( -119.23, 34.27)
                xpt, ypt = map(Vrrlng, Vrrlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Ventura" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Victorville' ):
                Viclng, Viclat  = ( -117.29, 34.54)
                xpt, ypt = map(Viclng, Viclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Victorville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Visalia' ):
                Vlilng, Vlilat  = ( -119.29, 36.33)
                xpt, ypt = map(Vlilng, Vlilat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Visalia" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Vista' ):
                Vislng, Vislat  = ( -117.24, 33.20)
                xpt, ypt = map(Vislng, Vislat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Vista" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Walnut' ):
                Wlng, Wlat  = ( -117.87, 34.02)
                xpt, ypt = map(Wlng, Wlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Walnut" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Walnut Creek' ):
                WClng, WClat  = ( -122.07, 37.91)
                xpt, ypt = map(WClng, WClat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Walnut Creek" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Warner Springs' ):
                WSlng, WSlat  = ( -116.65, 33.28)
                xpt, ypt = map(WSlng, WSlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Warner Springs" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Watsonville' ):
                Wvlng, Wvlat  = ( -121.76, 36.91)
                xpt, ypt = map(Wvlng, Wvlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Watsonville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Weed' ):
                Weelng, Weelat  = ( -122.39, 41.42)
                xpt, ypt = map(Weelng, Weelat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Weed" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'West Hills' ):
                Welng, Welat  = ( -118.64, 34.20)
                xpt, ypt = map(Welng, Welat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "West Hills" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Westminster' ):
                Wterlng, Wterlat  = ( -118.00, 33.75)
                xpt, ypt = map(Wterlng, Wterlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Westminster" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Westport' ):
                Wportlng, Wportlat  = ( -123.78, 39.64)
                xpt, ypt = map(Wportlng, Wportlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Westport" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Westwood' ):
                Woolng, Woolat  = ( -121.01, 40.31)
                xpt, ypt = map(Woolng, Woolat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Westwood" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Whittier' ):
                Wtttlng, Wtttlat  = ( -118.03, 33.98)
                xpt, ypt = map(Wtttlng, Wtttlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Whittier" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Wildomar' ):
                Wildlng, Wildlat  = ( -117.28, 33.60)
                xpt, ypt = map(Wildlng, Wildlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Wildomar" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Williams' ):
                Wmslng, Wmslat  = ( -122.15, 39.15)
                xpt, ypt = map(Wmslng, Wmslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Williams" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Willits' ):
                Wlltlng, Wlltlat  = ( -123.36, 39.41)
                xpt, ypt = map(Wlltlng, Wlltlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Willits" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Willows' or citywiththings[y] == 'Wilows'):
                Wwslng, Wwslat  = ( -122.19, 39.52)
                xpt, ypt = map(Wwslng, Wwslat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Willows" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Wilmington' ):
                Wmylng, Wmylat  = ( -118.26, 33.79)
                xpt, ypt = map(Wmylng, Wmylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Wilmington" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Winchester' ):
                Wchlng, Wchlat  = ( -117.08, 33.71)
                xpt, ypt = map(Wchlng, Wchlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Winchester" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Windsor' ):
                Wsorlng, Wsorlat  = ( -122.82, 38.55)
                xpt, ypt = map(Wsorlng, Wsorlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Windsor" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Woodlake' ):
                Wlaklng, Wlaklat  = ( -119.10, 36.41)
                xpt, ypt = map(Wlaklng, Wlaklat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt , "Woodlake" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Woodland' or citywiththings[y] == 'Woodland Hills'):
                WHIlng, WHIlat  = ( -121.77, 38.68)
                xpt, ypt = map(WHIlng, WHIlat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt + 10000, "Woodland" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Yountville' ):
                Ylng, Ylat  = ( -122.36, 38.40)
                xpt, ypt = map(Ylng, Ylat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt + 10000, "Yountville" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Yuba City' ):
                Ybalng, Ybalat  = ( -121.62, 39.14)
                xpt, ypt = map(Ybalng, Ybalat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt + 10000, "Yuba City" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Yucaipa' ):
                Yclng, Yclat  = ( -117.04, 34.03)
                xpt, ypt = map(Yclng, Yclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt + 10000, "Yucaipa" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')

            if(citywiththings[y] == 'Yucca Valley' ):
                Ycclng, Ycclat  = ( -116.43, 34.11)
                xpt, ypt = map(Ycclng, Ycclat, inverse = False)
                map.plot(xpt,ypt, 'D', markersize = 5, color = 'r')
                plt.text(xpt,ypt + 10000, "Yucca Valley" , fontsize = 7, fontweight = 'bold', color = '#FFFFFF')
    #----------------------------------------------------------------------------------------------------------------------------------------------------#

        plt.title('UFO SIGHTINGS IN CALIFORNIA')
        plt.show() #Learn how to plot multiple points I think plt.show() comes after all the points

    if(searcher == 0):
        print("") #So it does nothing if it is not found. Mostly for the date
