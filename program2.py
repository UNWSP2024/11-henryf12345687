#Henry Forst
#11/14/2025
#Week 11
import tkinter 
import tkinter.messagebox
class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window, text='Show Info',
                                        command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text='Quit',
                                          command=self.main_window.destroy)
        self.my_button.pack()
        self.quit_button.pack()
    def do_something(self):
        tkinter.messagebox.showinfo('Henry Forst','62104 376 st. Gibbon, MN')
if __name__ == '__main__':
    my_gui = myGUI()
    tkinter.mainloop()
