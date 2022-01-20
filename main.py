from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk

# ALL STUFF SHOULD GO TO /dev/null HAHAHAHAHAHA


def add_info():
    lbl_end = Label(window, text="This software is a joke.", font=("Arial Bold", 12))
    lbl_end.place(x=285, y=220)
    prog.destroy()
    lbl_end2 = Label(window, text="Never input this data to any software!", font=("Arial Bold", 12))
    lbl_end2.place(x=285, y=240)


def clicked():
    lbl_thx = Label(window, text="ありがと！", font=("Arial Bold", 12))
    lbl_thx.place(x=399, y=195)
    prog.place(x=340, y=220)
    prog.start()
    prog.after(5000, add_info)


window = Tk()
window.title("Totally Not Malware")
window.geometry('600x281')
window.resizable(width=False, height=False)
img_load = Image.open("tsukasa-hiiragi.png")
img_rend = ImageTk.PhotoImage(img_load)
img = Label(window, image=img_rend)
img.image = img_rend
img.grid(column=0, row=0)
lbl = Label(window, text="H-hi there...", font=("Arial Bold", 12))
lbl.place(x=400, y=0)
lbl1 = Label(window, text="Do you th-think I could have your", font=("Arial Bold", 12))
lbl1.place(x=325, y=20)
lbl2 = Label(window, text="credit card information, p-please?", font=("Arial Bold", 12))
lbl2.place(x=323, y=40)
lbl3 = Label(window, text="Card number:", font=("Arial Bold", 12))
lbl3.place(x=285, y=65)
txt = Text(window, height=1, width=23)
txt.place(x=400, y=68)
lbl4 = Label(window, text="Expiry date:", font=("Arial Bold", 12))
lbl4.place(x=290, y=95)
txt1 = Text(window, height=1, width=23)
txt1.place(x=400, y=98)
lbl5 = Label(window, text="Security code:", font=("Arial Bold", 12))
lbl5.place(x=280, y=125)
txt2 = Text(window, height=1, width=23)
txt2.place(x=400, y=128)
prog = Progressbar(window, orient=HORIZONTAL, length=200, mode="indeterminate")
btn = Button(window, text="Th-thanks", command=clicked, font=("Arial Bold", 12))
btn.place(x=395, y=160)
window.mainloop()
