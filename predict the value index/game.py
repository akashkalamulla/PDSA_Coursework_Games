import os
import tkinter as tk
from tkinter import messagebox
import random
import time
import mysql.connector
from mysql.connector import Error

# MySQL setup
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'pdsa_2'
}

# Establishing connection to MySQL
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
except Error as err:
    messagebox.showerror("Database Error", f"Error connecting to the database: {err}")
    exit(1)

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Predict the Value Index Game')
        self.root.geometry('600x500')
        self.root.configure(bg='#4682b4')
        self.root.minsize(600, 500)

        self.player_name = tk.StringVar()
        self.target = None
        self.correct_index = None
        self.chosen_index = None
        self.results = {}
        self.previous_index = None

        # Initialize the start screen
        self.show_start_screen()

    def show_start_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text='Welcome to Predict the Value Index Game!', bg='#4682b4', fg='white', font=('Arial', 18, 'bold')).pack(pady=20)
        tk.Label(self.root, text='Enter your name to start:', bg='#4682b4', fg='white', font=('Arial', 16)).pack(pady=20)

        name_entry = tk.Entry(self.root, textvariable=self.player_name, font=('Arial', 14))
        name_entry.pack(pady=10)

        tk.Button(self.root, text='Start Game', command=self.play_game, bg='#ff4500', fg='white', font=('Arial', 14)).pack(pady=20)

    def play_game(self):
        name = self.player_name.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        if len(name) > 50:
            messagebox.showwarning("Input Error", "Name is too long. Please enter a shorter name.")
            return

        self.start_game()

    def start_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Ensure that a different index is selected each time the game is played
        while True:
            numbers = sorted(random.sample(range(1, 1000001), 5000))
            self.target = random.randint(1, 1000000)

            self.results = {
                "Binary Search": {"index": None, "time": None},
                "Jump Search": {"index": None, "time": None},
                "Exponential Search": {"index": None, "time": None},
                "Fibonacci Search": {"index": None, "time": None},
                "Interpolation Search": {"index": None, "time": None},
            }

            # Calculate the index for the current target
            self.results["Binary Search"]["index"], self.results["Binary Search"]["time"] = self.binary_search(numbers, self.target)

            # Ensure the new index is different from the previous index
            if self.results["Binary Search"]["index"] != self.previous_index:
                self.previous_index = self.results["Binary Search"]["index"]
                break

        self.results["Jump Search"]["index"], self.results["Jump Search"]["time"] = self.jump_search(numbers, self.target)
        self.results["Exponential Search"]["index"], self.results["Exponential Search"]["time"] = self.exponential_search(numbers, self.target)
        self.results["Fibonacci Search"]["index"], self.results["Fibonacci Search"]["time"] = self.fibonacci_search(numbers, self.target)
        self.results["Interpolation Search"]["index"], self.results["Interpolation Search"]["time"] = self.interpolation_search(numbers, self.target)

        random_choices = random.sample(range(5000), 3) + [self.results["Binary Search"]["index"]]
        random.shuffle(random_choices)

        self.chosen_index = tk.IntVar()

        tk.Label(self.root, text=f"Target Number: {self.target}", bg='#4682b4', fg='white', font=('Arial', 16)).pack(pady=20)
        tk.Label(self.root, text="Guess the index of the target number:", bg='#4682b4', fg='white', font=('Arial', 14)).pack(pady=10)

        for choice in random_choices:
            tk.Radiobutton(self.root, text=f'Index {choice}', variable=self.chosen_index, value=choice, bg='#f0f8ff',
                           font=('Arial', 14)).pack(anchor='w', padx=20, pady=5)

        tk.Button(self.root, text='Submit Guess', command=self.submit_guess, bg='#32cd32', fg='white', font=('Arial', 14)).pack(pady=20)

    def binary_search(self, arr, x):
        try:
            low, high = 0, len(arr) - 1
            start_time = time.time()
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    return mid, "{:.8f}".format(time.time() - start_time)
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1, "{:.8f}".format(time.time() - start_time)
        except Exception as e:
            print(f"Binary Search Error: {e}")
            return -1, "0.00000000"

    def jump_search(self, arr, x):
        try:
            length = len(arr)
            step = int(length ** 0.5)
            prev, curr = 0, 0
            start_time = time.time()
            while curr < length and arr[curr] < x:
                prev = curr
                curr += step
            for i in range(prev, min(curr, length)):
                if arr[i] == x:
                    return i, "{:.8f}".format(time.time() - start_time)
            return -1, "{:.8f}".format(time.time() - start_time)
        except Exception as e:
            print(f"Jump Search Error: {e}")
            return -1, "0.00000000"

    def exponential_search(self, arr, x):
        try:
            if arr[0] == x:
                return 0, "0.00000000"
            length = len(arr)
            i = 1
            start_time = time.time()
            while i < length and arr[i] <= x:
                i = i * 2
            return self.binary_search(arr[:min(i, length)], x)
        except Exception as e:
            print(f"Exponential Search Error: {e}")
            return -1, "0.00000000"

    def fibonacci_search(self, arr, x):
        try:
            length = len(arr)
            fib2 = 0
            fib1 = 1
            fibM = fib2 + fib1
            while fibM < length:
                fib2 = fib1
                fib1 = fibM
                fibM = fib2 + fib1
            offset = -1
            start_time = time.time()
            while fibM > 1:
                i = min(offset + fib2, length - 1)
                if arr[i] < x:
                    fibM = fib1
                    fib1 = fib2
                    fib2 = fibM - fib1
                    offset = i
                elif arr[i] > x:
                    fibM = fib2
                    fib1 -= fib2
                    fib2 = fibM - fib1
                else:
                    return i, "{:.8f}".format(time.time() - start_time)
            if fib1 and arr[offset + 1] == x:
                return offset + 1, "{:.8f}".format(time.time() - start_time)
            return -1, "{:.8f}".format(time.time() - start_time)
        except Exception as e:
            print(f"Fibonacci Search Error: {e}")
            return -1, "0.00000000"

    def interpolation_search(self, arr, x):
        try:
            low, high = 0, len(arr) - 1
            start_time = time.time()
            while low <= high and arr[low] <= x <= arr[high]:
                pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
                if arr[pos] == x:
                    return pos, "{:.8f}".format(time.time() - start_time)
                if arr[pos] < x:
                    low = pos + 1
                else:
                    high = pos - 1
            return -1, "{:.8f}".format(time.time() - start_time)
        except Exception as e:
            print(f"Interpolation Search Error: {e}")
            return -1, "0.00000000"

    def submit_guess(self):
        self.correct_index = self.results["Binary Search"]["index"]
        guess = self.chosen_index.get()

        if guess == self.correct_index:
            messagebox.showinfo("Result", f"Correct! The target number {self.target} is at index {guess}.")
        else:
            messagebox.showinfo("Result", f"Wrong! The correct index is {self.correct_index}. You chose {guess}.")

        self.save_result()

    def save_result(self):
        try:
            name = self.player_name.get()
            for method, result in self.results.items():
                index = result["index"]
                time_taken = result["time"]
                cursor.execute("INSERT INTO searches (user_name, search_method, time_taken, index_value, target_value) "
                               "VALUES (%s, %s, %s, %s, %s)",
                               (name, method, time_taken, index, self.target))
            conn.commit()
        except Error as e:
            messagebox.showerror("Database Error", f"Error saving to the database: {e}")
        finally:
            self.show_start_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
