from tkinter import Tk, Label, Button, Frame

class Welcome:
    def __init__(self, master):
        self._master = master
        self._master.title("A.I. BlackJack Sim v1.0")
        self._master.geometry('{}x{}'.format(460, 350))
        

#        self._top_frame = Frame(self._master, bg='cyan', width=450, height=50, pady=3)

        
#        self._master.grid_rowconfigure(1, weight=1)
#        self._master.grid_columnconfigure(0, weight=1)


#        self._top_frame.grid(row=0, sticky="ew")


        self._label = Label(self._master, text="Welcome to Artificial Intelligence BJ Simulator")
        self._label.pack()
        self._close_button = Button(self._master, text="Close", command=self._master.quit)
        self._close_button.pack()
        self._next_button = Button(self._master, text="Next", command=self.next)
        self._next_button.pack()


    def next(self):
        pass

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
    root = Tk()
    my_gui = Welcome(root)
    root.mainloop()

if __name__ == '__main__':
    main()
