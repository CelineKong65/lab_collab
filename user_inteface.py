import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Covid-19 Diagnose Expert System")
window.geometry("300x200+500+300")

def on_button_click():
    #messagebox.showinfo("Message",entry.get())
    messagebox.showinfo("Message","Send her to karaoke!")
    
label = tk.Label(window, text="Please enter your roommate's mood")
label.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.insert(0,"Roommate is in bad mood")
entry.pack(pady=12)

button = tk.Button(window, text="Ok", command=on_button_click)
button.pack(pady=12)

window.mainloop()