from tkinter import *
from tkinter import ttk
from winsound import *
root = Tk()


screen_size = ("480","x","380")
root.geometry("".join(screen_size))
root.minsize(screen_size[0],screen_size[2])
root.maxsize(screen_size[0],screen_size[2])
root.title("Pomidoro by sonju")
root.configure(bg='lightcoral')

label_main  = ttk.Label(text="Pomidoro 0",foreground="#FFFFFF", background="lightcoral",font=("Arial",28))
label_main.place(x=120,y=30) 


label_time = ttk.Label(text="25:00",foreground="#FFFFFF", background="lightcoral",font=("Arial",46))
label_time.place(x=150,y=120)

label_status = ttk.Label(text="work",foreground="#FFFFFF", background="lightcoral",font=("Arial",28))
label_status.place(x=180,y=230)

status = "work"
pomidoro = 0
clock = 25*60
clock_run = False

start_text = """||   ||
||   ||
||   ||"""

stop_text = """|  \   
|    }
|  /"""

def play():
    return MessageBeep()
def time():
    global clock
    global clock_run
    global status
    global pomidoro
    if clock_run == False:
        return 0;
    minutes = str(clock // 60) if clock // 60 >= 10 else str("0" + str(clock // 60))
    second = str(clock % 60) if clock % 60 >= 10 else str("0" + str(clock % 60))
    label_time.config(text= f"{minutes}:{second}")
    clock -= 1
    if clock < 30:
        play()
    if clock == -1:
        run_clock()
        if status == "work":
            if pomidoro == 3:
                status = "happy"
                label_status.config(text=status)
                clock = 30*60
                return 0
            status = "relax"
            label_status.config(text=status)
            clock = 5*60
        elif status == "happy":
            status = "end"
            label_status.config(text=status)
            pomidoro += 1
            label_main.config(text=str("Pomidoro " + str(pomidoro)))    
            label_status.config(text=status)
        elif status == "relax":
            status = "work"
            clock = 25*60
            pomidoro += 1
            label_main.config(text=str("Pomidoro " + str(pomidoro)))
                
    root.after(1000,time)


def run_clock():
    global Button
    global clock_run
    if status == "end":
        return 0;
    if clock_run == False:
        clock_run = True
        Button.config(text=start_text)
        return time()
    clock_run = False
    Button.config(text=stop_text)


Button = ttk.Button(text=stop_text,command=run_clock,width=25)
Button.place(x=150,y=300)
root.mainloop()