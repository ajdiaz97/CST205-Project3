#https://pythonprogramming.net/change-show-new-frame-tkinter/
#https://www.youtube.com/watch?v=jBUpjijYtCk
#http://effbot.org/tkinterbook/listbox.htm
#http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

import tkinter as tk
import FinalUFOSightingMapper

LARGE_FONT= ("Georgia", 44)
global searchforcity




#makes a window with the start page
class UFO(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, CityPage, ShapePage, DatePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#this allows the user to choose which search he wants to commit
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #button to city search
        button = tk.Button(self, text="City Search",
                            command=lambda: controller.show_frame(CityPage), width = 55, height = 10)
        button.pack()

        #button to shape search
        button2 = tk.Button(self, text="Shape Search",
                            command=lambda: controller.show_frame(ShapePage), width = 55, height = 10)
        button2.pack()

        #button to date search
        button3 = tk.Button(self, text="Date Search",
                            command=lambda: controller.show_frame(DatePage), width = 55, height = 10)
        button3.pack()



#For city search
class CityPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="City Search", font=LARGE_FONT)
        label.pack()
        #creating city search widget
        self.cityEntry = tk.Entry(self) #search bar is appearing everywhere
        self.cityEntry.config(width = 15,font = "Helvetica 28")
        self.cityEntry.pack()
        #cityEntered is string of entered string in entry field
        searchButton = tk.Button(self, text = "Search", command = self.callback)
        searchButton.pack()

    def callback(self):
        global searchforcity
        #puts the variable on whatever city you write into the search box into the program
        searchforcity = self.cityEntry.get()
        FinalUFOSightingMapper.searchforcity = searchforcity
        FinalUFOSightingMapper.citysearch()




        #searchforcity



class ShapePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Shape Search", font=LARGE_FONT)
        label.pack()
        #creating shape search widget
        #Using listbox for shape search for only 18
        self.shapeList = tk.Listbox(self, font = "Helvetica 16")
        self.shapeList.insert(1, "Chevron")
        self.shapeList.config(selectbackground ="springgreen4")
        self.shapeList.insert(2, "Cigar")
        self.shapeList.insert(3, "Circle")
        self.shapeList.insert(4, "Cone")
        self.shapeList.insert(5, "Cross")
        self.shapeList.insert(6, "Cylinder")
        self.shapeList.insert(7, "Diamond")
        self.shapeList.insert(8, "Disk")
        self.shapeList.insert(9, "Unknown")
        self.shapeList.insert(10, "Egg")
        self.shapeList.insert(11, "Fireball")
        self.shapeList.insert(12, "Formation")
        self.shapeList.insert(13, "Light")
        self.shapeList.insert(14, "Other")
        self.shapeList.insert(15, "Oval")
        self.shapeList.insert(16, "Rectangle")
        self.shapeList.insert(17, "Sphere")
        self.shapeList.insert(18, "Triangle")
        self.shapeList.pack()


        searchButton = tk.Button(self, text = "Search", command = self.listcall)
        searchButton.pack()

    def listcall(self):
        #searchforshape
        #whatever shape is chosen is put into the program
        index = self.shapeList.curselection()[0]
        seltext = self.shapeList.get(index)
        FinalUFOSightingMapper.question = "Shape"
        FinalUFOSightingMapper.searchforshape = seltext
        FinalUFOSightingMapper.advancedsearch()


class DatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Date Search", font=LARGE_FONT)
        label.pack()

        blankSpace = tk.Label(self, text = "")
        blankSpace.pack()

        #creating spinbox for date
        #creating spinbox to select date by first month, then day
        self.monthLabel = tk.Label(self, text = "Month", font = "Helvetica 12")
        self.monthLabel.pack()
        self.month = tk.Spinbox(self, from_=1, to=12, font = "Helvetica 16")
        self.month.pack()
        self.dayLabel = tk.Label(self, text = "Day", font = "Helvetica 12")
        self.dayLabel.pack()
        self.day = tk.Spinbox(self, from_=1, to=31, font = "Helvetica 16")
        self.day.pack()
        searchButton = tk.Button(self, text = "Search", command = self.datecall )
        searchButton.pack()

    def datecall(self):
        #searchformonth
        #searchforday
        #whatever date is chosen will be put into the program
        monther = self.month.get()
        dayer = self.day.get()
        FinalUFOSightingMapper.question = "Date"
        FinalUFOSightingMapper.searchformonth = monther
        FinalUFOSightingMapper.searchforday = dayer
        FinalUFOSightingMapper.advancedsearch()

app = UFO()
app.mainloop()
