import tkinter as tk
from tkinter import messagebox

WORK_TIME = 25
BREAK_TIME = 5


def update_timer():
    if not paused.get():
        minutes, seconds = divmod(current_time.get(), 60)
        timer_text.set(f"{minutes:02d}:{seconds:02d}")
        current_time.set(current_time.get() - 1)
        if current_time.get() >= 0:
            window.after(1000, update_timer)
        else:
            if timer_type.get() == "Work":
                timer_finished()
                start_btn.config(state="normal")
                break_timer()
            else:
                timer_finished()
                start_btn.config(state="normal")
                main_timer()


def main_timer():
    current_time.set(WORK_TIME)
    timer_type.set("Work")
    paused.set(False)
    start_btn.config(state="normal")
    update_timer()


def break_timer():
    current_time.set(BREAK_TIME)
    timer_type.set("Break")
    paused.set(False)
    update_timer()


def timer_finished():
    messagebox.showinfo("Timer Done", "Time's up!")


def pause_timer():
    paused.set(not paused.get())

    if paused.get():
        pause_btn.config(text="Resume")
    else:
        pause_btn.config(text="Pause")
        start_btn.config(state='disabled')  # disable start button
        update_timer()


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Pomodoro timer")
    window.geometry("400x300")
    window.rowconfigure(1, weight=1)
    window.columnconfigure(1, weight=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)

    timer_text = tk.StringVar()
    timer_label = tk.Label(frame, textvariable=timer_text, font=("Helvetica", 24))

    start_btn = tk.Button(frame, text="Start", command=lambda: main_timer())
    pause_btn = tk.Button(frame, text="Pause", command=lambda: pause_timer())

    timer_label.grid(row=0, column=0)
    start_btn.grid(row=1, column=0)
    pause_btn.grid(row=2, column=0)

    current_time = tk.IntVar()
    timer_type = tk.StringVar()
    paused = tk.BooleanVar()

    frame.grid(row=2, column=1)

    window.mainloop()
