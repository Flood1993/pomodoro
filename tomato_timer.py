from tkinter import Tk
from tkinter import Label
from tkinter import Button


class TomatoTimer:
    def __init__(self, master):
        self.working_minutes = 4  #25
        self.timer = 4  #25*60
        self.running_time = False
        self.completed_tomatoes = 0

        self.master = master
        master.title("Pomodoro Timer")

        self.label_text = Label(master, text='Timer:')
        self.label_text.pack()
        self.label = Label(master, text=str(self.timer))
        self.label.pack()

        self.tomato_count_text = Label(master, text='Completed tomatoes:')
        self.tomato_count_text.pack()
        self.tomato_count = Label(master, text=str(self.completed_tomatoes))
        self.tomato_count.pack()

        self.start_button = Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.pause_button = Button(master, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.reset_button = Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.resume_button = Button(master, text="Resume", command=self.resume)
        self.resume_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def start(self):
        if self.timer <= 0:
            self.timer = self.working_minutes
        self.running_time = True
        self.master.iconify()

    def pause(self):
        self.running_time = False

    def reset(self):
        self.timer = self.working_minutes
        self.running_time = False

    def resume(self):
        self.running_time = True
        self.master.iconify()

    def update_timer(self):
        if self.running_time:
            self.timer -= 1

        # Time is up
        if self.timer <= 0:
            # Stop timer and reset it to the original value
            self.running_time = False
            self.timer = self.working_minutes

            # Update the tomato count
            self.completed_tomatoes += 1
            self.tomato_count['text'] = str(self.completed_tomatoes)

            # Bring back the window so user can easily start next tomato
            self.master.deiconify()

        # Update the timer label and call itself after one second
        self.label['text'] = str(self.timer)
        self.label.after(1000, self.update_timer)


if __name__ == '__main__':
    root = Tk()
    tomato = TomatoTimer(root)
    tomato.update_timer()
    root.mainloop()
