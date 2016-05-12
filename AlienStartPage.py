#https://pythonprogramming.net/change-show-new-frame-tkinter/
#https://www.youtube.com/watch?v=jBUpjijYtCk
#http://effbot.org/tkinterbook/listbox.htm

import tkinter as tk


LARGE_FONT= ("Georgia", 44)


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

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #button to city search
        button = tk.Button(self, text="City Search",
                            command=lambda: controller.show_frame(CityPage))
        button.pack()

        #button to shape search
        button2 = tk.Button(self, text="Shape Search",
                            command=lambda: controller.show_frame(ShapePage))
        button2.pack()

        #button to date search
        button3 = tk.Button(self, text="Date Search",
                            command=lambda: controller.show_frame(DatePage))
        button3.pack()


class CityPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="City Search", font=LARGE_FONT)
        label.pack()

        #creating city search widget
        cityEntry = tk.Entry(self) #search bar is appearing everywhere
        cityEntry.config(width = 15,font = "Helvetica 28")
        cityEntry.pack()

        #cityEntered is string of entered string in entry field
        cityEntered = cityEntry.get()
        searchButton = tk.Button(self, text = "Search")
        searchButton.pack()


class ShapePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Shape Search", font=LARGE_FONT)
        label.pack()

        #creating shape search widget
        #Using listbox for shape search for only 18
        shapeList = tk.Listbox(self, font = "Helvetica 16")
        shapeList.insert(1, "Chevron")
        shapeList.insert(2, "Cigar")
        shapeList.insert(3, "Circle")
        shapeList.insert(4, "Cone")
        shapeList.insert(5, "Cross")
        shapeList.insert(6, "Cylinder")
        shapeList.insert(7, "Diamond")
        shapeList.insert(8, "Disk")
        shapeList.insert(9, "Unknown")
        shapeList.insert(10, "Egg")
        shapeList.insert(11, "Fireball")
        shapeList.insert(12, "Formation")
        shapeList.insert(13, "Light")
        shapeList.insert(14, "Other")
        shapeList.insert(15, "Oval")
        shapeList.insert(16, "Rectangle")
        shapeList.insert(17, "Sphere")
        shapeList.insert(18, "Triangle")
        shapeList.pack()

        
        searchButton = tk.Button(self, text = "Search")
        searchButton.pack()
        
class DatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Date Search", font=LARGE_FONT)
        label.pack()

        blankSpace = tk.Label(self, text = "")
        blankSpace.pack()

        #creating spinbox for date
        #creating spinbox to select date by first month, then day
        monthLabel = tk.Label(self, text = "Month", font = "Helvetica 12").pack()
        month = tk.Spinbox(self, from_=1, to=12, font = "Helvetica 16").pack()
        dayLabel = tk.Label(self, text = "Day", font = "Helvetica 12").pack()
        day = tk.Spinbox(self, from_=1, to=31, font = "Helvetica 16").pack()

        searchButton = tk.Button(self, text = "Search")
        searchButton.pack()
        
app = UFO()
app.mainloop()
