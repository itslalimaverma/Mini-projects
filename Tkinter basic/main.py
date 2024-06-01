#Miles to Km program using Tkinter
from tkinter import *
def miles_to_km():
    mil=float(miles.get())
    km=round(mil*1.609)
    result.config(text=f"{km}")


window=Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

miles=Entry(width=7)
miles.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)


is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)


result=Label(text="0")
result.grid(column=1,row=1)


kilometer=Label(text="Km")
kilometer.grid(column=2,row=1)


button=Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)


window.mainloop()