import tkinter as tk
from tkinter import messagebox
from CalculateBMI import *


def closeapp():
    window.destroy()


def reset():
    height_inch_entry.delete(0, 12)
    weight_lb_entry.delete(0, 12)
    height_meter_entry.delete(0, 12)
    weight_kg_entry.delete(0, 12)
    text.set("")
    bmi.set("")
    interpretation.set("")


def calculate_bmi():
    text.set("Your BMI is")
    if (height_inch_entry.get() != '') and (weight_lb_entry.get() != '') and (height_meter_entry.get() != '') and (
            weight_kg_entry.get() != ''):
        messagebox.showerror("Error", "Please enter weight and height once only")
    elif (height_inch_entry.get() != '') and (weight_lb_entry.get() != ''):
        if float(height_inch_entry.get()) <= 0 or float(weight_lb_entry.get()) <= 0:
            messagebox.showerror("Error", "Values cannot be 0 or less than 0")
        else:
            h = (height_inch_entry.get())
            w = (weight_lb_entry.get())
            bmi.set(calculate_bmi2(w, h))
    elif (height_meter_entry.get() != '') and (weight_kg_entry.get() != ''):
        if float(height_meter_entry.get()) <= 0 or float(weight_kg_entry.get()) <= 0:
            messagebox.showerror("Error", "Values cannot be 0 or less than 0")
        else:
            h = (height_meter_entry.get())
            w = (weight_kg_entry.get())
            bmi.set(calculate_bmi1(w, h))
    elif (height_inch_entry.get() != '') and (weight_kg_entry.get() != ''):
        if float(height_inch_entry.get()) <= 0 or float(weight_kg_entry.get()) <= 0:
            messagebox.showerror("Error", "Values cannot be 0 or less than 0")
        else:
            w = convert_kg2lb(weight_kg_entry.get())
            h = (height_inch_entry.get())
            bmi.set(calculate_bmi2(w, h))
    elif (height_meter_entry.get() != '') and (weight_lb_entry.get() != ''):
        if float(height_meter_entry.get()) <= 0 or float(weight_lb_entry.get()) <= 0:
            messagebox.showerror("Error", "Values cannot be 0 or less than 0")
        else:
            w = convert_lb2kg(weight_lb_entry.get())
            h = (height_meter_entry.get())
            bmi.set(calculate_bmi1(w, h))
    interpretation.set(interpret_bmi(bmi))

window = tk.Tk()
window.resizable(height="true", width="true")
window.title("Calculate BMI")
window.minsize(height=250, width=500)

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=closeapp)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", )
menubar.add_cascade(label="Help", menu=helpmenu)

# Title Calculate your BMI
top_Frame = tk.Frame(window)
top_Frame.grid(row=0, column=0, pady=10, sticky="")
header = tk.Label(top_Frame, text="Calculate your BMI", font=("calibri", "12"), fg="red")

# Enter Your input Values
mid_Frame = tk.Frame(window, borderwidth=2, highlightbackground="black", highlightthickness=1)
mid_Frame.grid(row=1, column=0, rowspan=2, columnspan=2, padx=20, pady=10)

mid_Frame1 = tk.Frame(mid_Frame)
mid_Frame1.grid(row=0, column=0)
height_inch = tk.Label(mid_Frame1, text="height (inch)", font=("calibri", "12"), width=12)
height_inch_entry = tk.Entry(mid_Frame1)

mid_Frame3 = tk.Frame(mid_Frame)
mid_Frame3.grid(row=1, column=0)
weight_lb = tk.Label(mid_Frame3, text="weight (lbs)", font=("calibri", "12"), width=12)
weight_lb_entry = tk.Entry(mid_Frame3)

mid_Frame2 = tk.Frame(mid_Frame)
mid_Frame2.grid(row=0, column=1)
height_meter = tk.Label(mid_Frame2, text="height (mtrs)", font=("calibri", "12"), width=12)
height_meter_entry = tk.Entry(mid_Frame2)

mid_Frame4 = tk.Frame(mid_Frame)
mid_Frame4.grid(row=1, column=1)
weight_kg = tk.Label(mid_Frame4, text="weight (kgs)", font=("calibri", "12"), width=12)
weight_kg_entry = tk.Entry(mid_Frame4)

mid_Frame5 = tk.Frame(mid_Frame)
mid_Frame5.grid(row=2, column=0, sticky="e")
bmi = tk.DoubleVar()
text = tk.StringVar()
interpretation = tk.StringVar()
text.set("Your BMI is")
info = tk.Label(mid_Frame5, textvariable=text, font=("calibri", "12"))
resultDisplay = tk.Label(mid_Frame5, textvariable=bmi, font=("calibri", "12"))
result = tk.Label(mid_Frame5, textvariable=interpretation, font=("calibri", "12"))

# Click on buttons to calculate or reset or close
bottom_Frame = tk.Frame(window, highlightbackground="black", highlightthickness=1)
bottom_Frame.grid(row=4, column=0, pady=10, sticky="e")
calculate = tk.Button(bottom_Frame, text="Calculate", command=calculate_bmi, font=("calibri", "12"), bg="#fff",
                      fg="#4b4f56",
                      width=12)
calculate.grid(pady=5, padx=10, row=0, column=0)
close = tk.Button(bottom_Frame, text="Close", font=("calibri", "12"), bg="#fff", fg="#4b4f56", command=closeapp,
                  width=12)
close.grid(pady=5, padx=10, row=0, column=1)
reset = tk.Button(bottom_Frame, text="Reset", font=("calibri", "12"), bg="#fff", fg="#4b4f56", command=reset, width=12)
reset.grid(pady=5, padx=10, row=0, column=2)

# pack it all together
header.pack(side="left")
height_inch.pack(side="left", padx=2)
height_inch_entry.pack(side="left", padx=2)
weight_lb.pack(side="left", padx=2)
weight_lb_entry.pack(side="left", padx=2)
height_meter.pack(side="left", padx=2)
height_meter_entry.pack(side="left", padx=2)
weight_kg.pack(side="left", padx=2)
weight_kg_entry.pack(side="left", padx=2)
info.pack(side="left")
resultDisplay.pack(side="left")
result.pack(side="left")

height_inch_entry.focus()

window.config(menu=menubar)
window.mainloop()