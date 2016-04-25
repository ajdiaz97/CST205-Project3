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
global citylocation
#Reads the CSV file and seperates the data into lists
def filereader():
    with open('Sightings.csv') as data:
        reader = csv.reader(data)
        for row in reader:
            date = row[0]
            time = row[1]
            city = row[2]
            state = row[3]
            shape = row[4]
            duration = row[5]
            description = row[6]
            #an example I want to figure out how to make it a list so it shows all the info we want
            if(city == 'Modesto'):
                global citylocation
                citylocation = geocoder.google(city)


def map():
    global citylocation
    #Makes a map of specifically California
    #llcrnrlat = lower leftcorner latitude, urcrnrlat = upper right corner latitude, llcrnerlon = lower leftcorner longitude, upper right corner longitude
    map = Basemap(projection = 'mill', llcrnrlat = 31, urcrnrlat = 43, llcrnrlon = -130, urcrnrlon = -109, resolution = 'h')
    map.drawcoastlines()
    map.fillcontinents(color = '#90EE90')
    map.drawstates(linewidth = 1)
    map.drawcountries(linewidth = 1)
    xpt, ypt = map(citylocation.lng, citylocation.lat)
    map.plot(xpt,ypt, 'c*', markersize = 15)
    plt.show()

filereader()
map()
