from tkinter import *

window = Tk()
window.title("Joey has no brain")
window.minsize(300, 150)
window.config(padx=20,pady=20)


entry = Entry(width=7)
entry.insert(END, string="0")
print(entry.get())
entry.grid(column=1,row=0)

label = Label(text="Kilometer")
label.grid(column=2,row=0)

labeleq = Label(text="is equal to")
labeleq.grid(column=0,row=1)

labelkm = Label(text="Miles")
labelkm.grid(column=3,row=1)

def cal(): #get is km
    newtext = float(entry.get())
    get = newtext * 0.62137
    label0.config(text=f"{get}")

label0 = Label(text="0")
label0.grid(column=1,row=1)

button = Button(text="Calculate", command=cal)
button.grid(column=1, row=2)

window.mainloop()