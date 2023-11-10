from tkinter import Label, Tk 
import time
import datetime
import pytz

app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(0, 0)

text_font = ("Arial", 45, 'bold')  # form this line we can change the fonts
background = "black"
foreground = "red"
border_width = 40

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock():
    tz = pytz.timezone('Asia/Kolkata')  # Seting the time zone for India
    current_time = datetime.datetime.now(tz)

    # Format the time with AM/PM
    time_live = current_time.strftime("%I:%M:%S %p") 
    label.config(text=time_live) 
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
