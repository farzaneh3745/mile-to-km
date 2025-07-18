from tkinter import Tk,Label,Entry,Button

window=Tk()
window.title("Mile To KM")

mile_label=Label(window,text="Mile : ")
mile_label.grid(row=0,column=0,padx=10,pady=10,sticky="e")

mile_entry=Entry(window,width=30)
mile_entry.grid(row=0,column=1,padx=(0,10),pady=5,sticky="w")

text_label=Label(window)
text_label.grid(row=1,column=1,padx=10,pady=5)

def calculate_amount():
    try:
        mile=float(mile_entry.get())
    except ValueError:
        text_label.config(text="Invalid Value",fg="red")
    else:
        km=round(mile * 1.6,2)
        text_label.config(text=f" is equal to : {km} km",fg="black")

calculate_button=Button(window,text="Calculate",command=calculate_amount)
calculate_button.grid(row=2,column=1,padx=10,pady=10)

window.mainloop()

