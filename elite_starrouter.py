from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk

class UI:
    def __init__(self, root):
        self._root = root
        
        # BooleanVar muuttujat
        self._system            = tk.BooleanVar()
        self._notes             = tk.BooleanVar()
        self._distance          = tk.BooleanVar()
        self._star_class        = tk.BooleanVar()
        self._dist_waypoint     = tk.BooleanVar()
        self._deviation         = tk.BooleanVar()
        self._system_address    = tk.BooleanVar()

        self.entry_box = None
        self.filepath = None

    def start(self):
        left_frame = tk.Frame(self._root, bg="lightgrey")
        left_frame.grid(row=1, column=0, sticky="nsew")

        right_frame = tk.Frame(self._root, bg="lightgrey")
        right_frame.grid(row=1, column=1, sticky="n")

        self.text_box = tk.Text(left_frame, state="normal", width=80, height=40)
        self.text_box.pack(fill="both", expand=True)

        # file open button
        file_opener = tk.Button(master=self._root, command=self.main, bg="lightgrey", text="Open StarRoute")
        file_opener.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # checkbuttons linkitetty BooleanVar:iin
        tk.Checkbutton(right_frame, text="System",            bg="lightgrey", variable=0).pack(anchor="w")
        tk.Checkbutton(right_frame, text="Notes",             bg="lightgrey", variable=self._notes).pack(anchor="w")
        tk.Checkbutton(right_frame, text="Distance",          bg="lightgrey", variable=self._distance).pack(anchor="w")
        tk.Checkbutton(right_frame, text="Star Class",        bg="lightgrey", variable=self._star_class).pack(anchor="w")
        tk.Checkbutton(right_frame, text="Distance Waypoint", bg="lightgrey", variable=self._dist_waypoint).pack(anchor="w")
        tk.Checkbutton(right_frame, text="Deviation",         bg="lightgrey", variable=self._deviation).pack(anchor="w")
        tk.Checkbutton(right_frame, text="System Address",    bg="lightgrey", variable=self._system_address).pack(anchor="w")

    def button_checker():
        pass
    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if not filepath:
            return None
        self.filepath = filepath
        return filepath    

    def main(self):
        x = " "
        filepath = self.open_file()
        if not filepath:
            return

        self.text_box.delete("1.0", tk.END)

        with open(filepath, "r", encoding="utf-8") as file:
            next(file)  # skip the first row
            for row in file:
                parts = row.strip().split(";")
                _system = parts[0]
                _notes = parts[1]
                _distance = parts[2]
                _star_class = parts[6]
                _dist_wayp = parts[7]
                _deviation = parts[8]
                _sys_adress = parts[9]

                self.text_box.insert(tk.END, parts[0] + x*5, parts[2] + x*5, parts[6] + x*5, parts[7], "\n")

root = Tk()
root.title("Elite Dangerous starRoute Reader")
root.geometry("1000x700")
root.config(bg="lightgrey")

ui = UI(root)
ui.start()

root.mainloop()
