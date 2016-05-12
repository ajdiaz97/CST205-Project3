#https://pythonprogramming.net/change-show-new-frame-tkinter/
#https://www.youtube.com/watch?v=jBUpjijYtCk
#http://effbot.org/tkinterbook/listbox.htm

import tkinter as tk

class UFO(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, CityPage, ShapePage, DatePage):
            
            frame = F(container,self)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,controller)
        label = tk.Label(self, text = "UFO SIGHTINGS IN CALIFORNIA", font = "Helvetica 44")
        label.pack(pady = 10, padx = 10)

        button = tk.Button(self, text = "City Search", command = lambda: controller.show_frame(CityPage))
        button.pack()

        button2 = tk.Button(self, text = "Shape Search", command = lambda: controller.show_frame(ShapePage))
        button2.pack()

        button3 = tk.Button(self, text = "Date Search", command=lambda:controller.show_frame(DatePage))
        button3.pack()
        
class CityPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "City Search", font = "Helvetica 44")
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "DO NOTHING")
        button1.pack()

class ShapePage(tk.Frame):
    tk.Frame.__init__(self, parent, controller)
    label = tk.Label(self,text= "Shape Search", font = "Helvetica 44")
    label.pack(pady=10, padx=10)

    button = tk.Button(self, text="DO NOTHING")
    button.pack()

class DatePage(tk.Frame):
    tk.Frame.__init__(self, parent, controller)
    label = tk.Label(self,text="Date Search", font = "Helvetica 44")
    label.pack(pady=10,padx=10)

    button = tk.Button(self, text="DO NOTHING")
    button.pack()

root = UFO()
root.mainloop()
