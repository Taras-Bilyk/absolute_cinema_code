from tkinter import *
from kivy.app import App
class A(App):
    def build(self):
        tk = Tk()
        canvas = Canvas(tk, height=400, width=200)
        canvas.pack()
        tk.title('test')
        btn = Button(text='button').pack()


A().run()

