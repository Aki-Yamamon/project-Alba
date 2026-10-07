import tkinter as tk


class Shell:
    """全画面ウィンドウを持ち、Page を載せて切り替える土台。"""

    def __init__(self, fullscreen=True, interval_ms=200):
        self.root = tk.Tk()
        self.root.configure(bg="#111")
        if fullscreen:
            self.root.attributes("-fullscreen", True)
            self.root.config(cursor="none")
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("q", lambda e: self.root.destroy())

        self._interval = interval_ms
        self._pages = {}    # 名前 -> Page
        self._frames = {}   # 名前 -> build() で作った Frame
        self._current = None

    def add_page(self, name, page):
        self._frames[name] = page.build(self.root)
        self._pages[name] = page

    def show(self, name):
        if self._current:
            self._frames[self._current].pack_forget()
        self._frames[name].pack(fill="both", expand=True)
        self._current = name

    def _tick(self):
        if self._current:
            self._pages[self._current].update()
        self.root.after(self._interval, self._tick)

    def run(self):
        self._tick()
        self.root.focus_force()
        self.root.mainloop()