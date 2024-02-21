import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from main_video import main_video



def capture():
    # Add your capture functionality here
    pass

def settings():
    # Add your settings functionality here
    pass

window = tk.Tk()
window.title("NextGen cctv")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')

frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="NextGen cctv Camera")
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=1, columnspan=2)

icon = Image.open('icons/spy.png')
icon = icon.resize((150, 150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5, 10), column=1, columnspan=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50, 50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50, 50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50, 50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50, 50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/security-camera.png')
btn7_image = btn7_image.resize((50, 50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)

btn_font = font.Font(size=25)
button_config = {
    'height': 90,
    'width': 180,
    'compound': 'left',
    'font': btn_font,
    'bd': 4,
    'highlightthickness': 0,
    'bg': '#f0f0f0',  # Button background color
    'fg': 'green',  # Button text color
    'activebackground': '#dddddd',  # Button background color when clicked
    'activeforeground': 'black',  # Button text color when clicked
}

btn1 = tk.Button(frame1, text='Monitor', command=find_motion, image=btn1_image, **button_config)
btn1.grid(row=2, pady=(20, 10), column=1)

btn4 = tk.Button(frame1, text='Record', command=record, image=btn4_image, **button_config)
btn4.grid(row=2, pady=(20, 10), column=2)

btn6 = tk.Button(frame1, text='In Out', command=in_out, image=btn6_image, **button_config)
btn6.grid(row=3, pady=(20, 10), column=1)

btn7 = tk.Button(frame1, text='Identify', command=main_video, image=btn7_image, **button_config)
btn7.grid(row=3, pady=(20, 10), column=2)

btn5 = tk.Button(frame1, command=window.quit, image=btn5_image, **button_config)
btn5.grid(row=4, pady=(20, 10), column=1, columnspan=2)

frame1.pack()
window.mainloop()
