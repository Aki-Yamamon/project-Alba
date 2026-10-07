import tkinter as tk

from shell.page import Page

FONT = "DejaVu Sans Mono"


class ClockPage(Page):
    def __init__(self, clock):
        self.clock = clock

    def build(self, parent):
        self.frame = tk.Frame(parent, bg="#111")
        box = tk.Frame(self.frame, bg="#111")
        box.place(relx=0.5, rely=0.5, anchor="center")

        self.date_lbl = tk.Label(box, fg="#9ecbff", bg="#111")
        self.time_lbl = tk.Label(box, fg="#7CFC98", bg="#111")
        self.tz_lbl = tk.Label(box, fg="#888", bg="#111")
        for lbl in (self.date_lbl, self.time_lbl, self.tz_lbl):
            lbl.pack()

        self.frame.bind("<Configure>", self._resize)
        return self.frame

    def _resize(self, event):
        px = int(min(event.width * 0.9 / (8 * 0.602), event.height * 0.9 / 1.8))
        px = max(px, 10)
        self.time_lbl.config(font=(FONT, -px, "bold"))
        self.date_lbl.config(font=(FONT, -int(px * 0.3)))
        self.tz_lbl.config(font=(FONT, -int(px * 0.15)))

    def update(self):
        t = self.clock.now()
        self.date_lbl.config(text=t.strftime("%Y-%m-%d (%a)"))
        self.time_lbl.config(text=t.strftime("%H:%M:%S"))
        self.tz_lbl.config(text=f"{self.clock.tz_name}  UTC{t.strftime('%z')}")