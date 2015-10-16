''' Tk UI module.
'''

import tkinter

class UI():
    '''
    Implementation of the UI interface using Tk.
    '''
    def __init__(self, client):
        self.window = tkinter.Tk()
        self.window.title('Many Worlds')
        self.window.geometry('400x300')
        
        self.button = tkinter.Button(self.window, text='Click', command=client.button_callback)
        self.button.pack()
        
        self.label = tkinter.Label(self.window, text='0')
        self.label.pack()
        
        self.client = client
        
    def startEventLoop(self):
        self.window.after(1000, self.tick)
        self.window.mainloop()
    
    def tick(self):
        self.client.tick()
        self.window.after(1000, self.tick)

    def updateClickCount(self, count):
        self.label.configure(text=str(count))