from tkinter import Label, Tk 
import time
import datetime
import pytz

app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x200")  # Increased the height to accommodate the date
app_window.resizable(0, 0)

text_font = ("Arial", 40, 'bold')  # from this line we can change the fonts
background = "black"
foreground = "red"
border_width = 45

time_label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
time_label.grid(row=0, column=1)

date_font = ("Arial", 20, 'bold')
date_label = Label(app_window, font=date_font, bg=background, fg=foreground)
date_label.grid(row=1, column=1)

def digital_clock():
    tz = pytz.timezone('Asia/Kolkata')  # Setting the time zone for India
    current_time = datetime.datetime.now(tz)

    # Format the time with AM/PM
    time_live = current_time.strftime("%I:%M:%S %p") 
    time_label.config(text=time_live)

    # Format the date
    date_live = current_time.strftime("%A, %B %d, %Y")
    date_label.config(text=date_live)

    app_window.after(200, digital_clock)

digital_clock()
app_window.mainloop()
