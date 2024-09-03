import tkinter as tk
import pygame
import time
from threading import Thread

pygame.mixer.init()

class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.is_running = False

        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes

        self.timer = self.work_time

        self.min = tk.StringVar()
        self.sec = tk.StringVar()
        self.update_display(self.timer)

        self.create_widgets()

    def create_widgets(self):
        self.min_label = tk.Label(self.root, textvariable=self.min, font=("arial", 22, "bold"), bg="red", fg='black')
        self.min_label.pack()

        self.sec_label = tk.Label(self.root, textvariable=self.sec, font=("arial", 22, "bold"), bg="black", fg='white')
        self.sec_label.pack()

        self.start_button = tk.Button(self.root, text="Start", bd=5, command=self.start_timer, bg="red", font=("arial", 15, "bold"))
        self.start_button.place(x=50, y=120)

    def update_display(self, timer):
        minutes, seconds = divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()

    def countdown(self):
        while self.timer > 0 and self.is_running:
            time.sleep(1)
            self.timer -= 1
            self.update_display(self.timer)

        if self.timer == 0 and self.is_running:
            self.play_sound()
            if self.timer == 0:
                if self.timer == self.work_time:
                    self.start_break()
                else:
                    self.start_timer()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.timer = self.work_time
            self.update_display(self.timer)
            thread = Thread(target=self.countdown)
            thread.start()

    def start_break(self):
        self.timer = self.break_time
        self.update_display(self.timer)
        thread = Thread(target=self.countdown)
        thread.start()

    def play_sound(self):
        pygame.mixer.music.load("Alarm.wav")
        pygame.mixer.music.play(loops=0)

    def stop(self):
        self.is_running = False

if __name__ == "__main__":
    root = tk.Tk()
    pomodoro = Pomodoro(root)
    root.mainloop()
