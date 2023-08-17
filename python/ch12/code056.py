# Copyright © https://steam.oxxostudio.tw

import tkinter as tk

root = tk.Tk()          # 產生 tkinter 視窗
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width, height)
root.destroy()          # 關閉視窗

