import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
USER_INP = simpledialog.askstring(title="Test",
prompt="какое у вас имя?:")

print("Привет", USER_INP)
