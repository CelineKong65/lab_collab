import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("COVID-19 Diagnosis Expert System")
window.geometry("350x260+500+300")

def diagnose():
    fever = var_fever.get()
    cough = var_cough.get()
    taste = var_taste.get()
    breath = var_breath.get()

    # Simple rule-based expert system
    if fever and cough and taste:
        result = "High chance of COVID-19.\nPlease get tested immediately."
    elif (fever and cough) or (cough and taste):
        result = "Possible COVID-19 infection.\nPlease monitor your symptoms."
    elif breath:
        result = "Warning: Difficulty breathing!\nSeek medical help IMMEDIATELY."
    else:
        result = "Low COVID-19 risk.\nContinue to monitor your health."

    messagebox.showinfo("Diagnosis Result", result)

# Labels
label = tk.Label(window, text="Select your symptoms:")
label.pack(pady=10)

# Checkbox variables
var_fever = tk.BooleanVar()
var_cough = tk.BooleanVar()
var_taste = tk.BooleanVar()
var_breath = tk.BooleanVar()

# Checkboxes
tk.Checkbutton(window, text="Fever", variable=var_fever).pack(anchor='w')
tk.Checkbutton(window, text="Cough", variable=var_cough).pack(anchor='w')
tk.Checkbutton(window, text="Loss of taste/smell", variable=var_taste).pack(anchor='w')
tk.Checkbutton(window, text="Difficulty breathing", variable=var_breath).pack(anchor='w')

# Button
button = tk.Button(window, text="Diagnose", command=diagnose)
button.pack(pady=15)

window.mainloop()
