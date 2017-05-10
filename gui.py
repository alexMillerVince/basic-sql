from tkinter import *
import tkinter.ttk as ttk


# Init
root = Tk()
root.configure(background='white')
root.style = ttk.Style()
root.style.theme_use('alt')
root.title('CodeCool - HRManager')
root.minsize(width=1024, height=800)

# Init left frame
left_frame = Frame(root, width=100, height=200)
left_frame.grid(rowspan=10, column=1, padx=10, pady=20)
left_frame.configure(background='white')


def create_button(button_name, row=0, column=0, padx=0, pady=0, width=None, function_name=None, window=left_frame):
    button = Button(window, text=button_name, command=function_name, width=width)
    button.grid(row=row, column=column, padx=padx, pady=pady)