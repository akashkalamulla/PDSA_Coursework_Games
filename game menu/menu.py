import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def run_program(file_path):
    try:
        if os.path.isfile(file_path):
            subprocess.run(['python', file_path], check=True)
        else:
            messagebox.showerror("Error", f"File not found: {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def tower_of_hanoi():
    new_page_path = r"C:\Users\AKASH\Documents\NIbm Digree\PDSA module\CW\PDSA_Coursework_Games\game menu\menu.py"
    try:
        subprocess.run(['python', new_page_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while opening new page: {e}")

def sixteen_queens_puzzle():
    new_page_path = r"C:\Users\AKASH\Documents\NIbm Digree\PDSA module\CW\PDSA_Coursework_Games\game menu\sixteen queens’ puzzle\game.py"
    try:
        subprocess.run(['python', new_page_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while opening new page: {e}")

def minimum_cost():
    new_page_path = r"C:\Users\AKASH\Documents\NIbm Digree\PDSA module\CW\PDSA_Coursework_Games\game menu\minimum cost\game.py"
    try:
        subprocess.run(['python', new_page_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while opening new page: {e}")

def identify_shortest_path():
    new_page_path = r"C:\Users\AKASH\Documents\NIbm Digree\PDSA module\CW\PDSA_Coursework_Games\game menu\identify shortest path\pdsa\gui-game\build\gui.py"
    try:
        subprocess.run(['python', new_page_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while opening new page: {e}")

def predict_value_index():
    new_page_path = r"C:\Users\AKASH\Documents\NIbm Digree\PDSA module\CW\PDSA_Coursework_Games\game menu\predict the value index\game.py"
    try:
        subprocess.run(['python', new_page_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while opening new page: {e}")


root = tk.Tk()
root.title("Game Menu")
root.geometry("400x400")
root.config(bg="#2C3E50")

# Styling options
button_bg = "#3498DB"
button_fg = "#FFFFFF"
button_font = ("Helvetica", 12, "bold")
button_active_bg = "#2980B9"
button_hover_bg = "#1ABC9C"

def on_enter(e):
    e.widget['background'] = button_hover_bg

def on_leave(e):
    e.widget['background'] = button_bg

# Create buttons
button1 = tk.Button(root, text="Tower of Hanoi", font=button_font, bg=button_bg, fg=button_fg,
                    activebackground=button_active_bg, command=tower_of_hanoi)
button2 = tk.Button(root, text="Sixteen Queens' Puzzle", font=button_font, bg=button_bg, fg=button_fg,
                    activebackground=button_active_bg, command=sixteen_queens_puzzle)
button3 = tk.Button(root, text="Minimum Cost", font=button_font, bg=button_bg, fg=button_fg,
                    activebackground=button_active_bg, command=minimum_cost)
button4 = tk.Button(root, text="Identify Shortest Path", font=button_font, bg=button_bg, fg=button_fg,
                    activebackground=button_active_bg, command=identify_shortest_path)
button5 = tk.Button(root, text="Predict the Value Index", font=button_font, bg=button_bg, fg=button_fg,
                    activebackground=button_active_bg, command=predict_value_index)

for button in [button1, button2, button3, button4, button5]:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

button1.pack(pady=20, ipadx=10, ipady=10, fill=tk.X)
button2.pack(pady=10, ipadx=10, ipady=10, fill=tk.X)
button3.pack(pady=10, ipadx=10, ipady=10, fill=tk.X)
button4.pack(pady=10, ipadx=10, ipady=10, fill=tk.X)
button5.pack(pady=10, ipadx=10, ipady=10, fill=tk.X)

root.mainloop()
