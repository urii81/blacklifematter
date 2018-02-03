from tkinter import *

class MainW(Tk):
    def __init__(self, master):
        Tk.__init__(self, master)
        self.master = master

       # self.mainWidgets()

#    def mainWidgets(self):
#        self.label1 = Label(self, text="Main window label", bg="green")
#        self.label1.grid(row=0, column=0)

 
'''
class SimConfig:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

class PlayerPlan:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")
'''
def main():
    
    app = MainW(None)
    app.title("A.I. BlackJack Sim v1.0")
    app.geometry('{}x{}'.format(1000, 700))
    #app.iconbitmap()
    app.mainloop()

if __name__ == '__main__':
    main()
