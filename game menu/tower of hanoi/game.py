import time
import tkinter as tk
from tkinter import font, messagebox
import mysql.connector

def create_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Use 'localhost' if the MySQL server is running on your local machine
        user="root",       # 'root' should be your MySQL username
        password="",       # Provide your MySQL password here
        database="pdsa_2"  # Ensure that the database 'pdsa_2' exists
    )



class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class TowerOfHanoiGUI:
    def __init__(self, root, num_disks, player_name):
        self.root = root
        self.num_disks = num_disks
        self.player_name = player_name
        self.root.title("Tower of Hanoi")

        canvas_height = max(400, 20 * num_disks + 200)
        self.canvas = tk.Canvas(self.root, width=600, height=canvas_height)
        self.canvas.pack()

        self.setup_ui()

        self.rods = {
            'A': Stack(),
            'B': Stack(),
            'C': Stack()
        }

        self.rod_coords = {
            'A': (150, 300),
            'B': (300, 300),
            'C': (450, 300)
        }

        for coord in self.rod_coords.values():
            self.canvas.create_line(coord[0], 100, coord[0], 300, width=5)
        self.canvas.create_rectangle(50, 300, 550, 320, fill="gray")

        rod_labels = {
            'A': "A",
            'B': "B",
            'C': "C"
        }

        for rod, (rx, ry) in self.rod_coords.items():
            label = tk.Label(self.root, text=rod_labels[rod], font=font.Font(size=12))
            label.place(x=rx - 5, y=325)

        self.disks = []
        disk_height = min(20, 200 // num_disks)
        for i in range(num_disks, 0, -1):
            disk_width = max(10, i * 10)
            disk = self.canvas.create_rectangle(
                150 - disk_width,
                300 - disk_height * (num_disks - i + 1),
                150 + disk_width,
                320 - disk_height * (num_disks - i + 1),
                fill="blue"
            )
            self.disks.append(disk)
            self.rods['A'].push(disk)

        self.selected_disk = None
        self.moves = []

        self.canvas.bind("<Button-1>", self.on_click)

        self.start_time = time.time()

    def setup_ui(self):
        back_button = tk.Button(self.root, text="Back", command=self.back_to_menu, font=font.Font(size=10))
        back_button.pack(side=tk.LEFT, padx=10, pady=10)

        player_label = tk.Label(self.root, text=f"Player: {self.player_name}", font=font.Font(size=12))
        player_label.pack(side=tk.LEFT, padx=10)

        self.hint_label = tk.Label(self.root, text="Hint: Move the disks from Rod A to Rod C.", font=font.Font(size=12))
        self.hint_label.pack(side=tk.TOP, pady=10)

    def on_click(self, event):
        x, y = event.x, event.y
        selected_rod = self.get_rod_from_coords(x)

        if selected_rod:
            if self.selected_disk is None:  # Select a disk
                if not self.rods[selected_rod].is_empty():
                    self.selected_disk = self.rods[selected_rod].pop()
                    self.canvas.itemconfig(self.selected_disk, fill="red")
                    self.selected_rod = selected_rod
            else:  # Move the disk
                if self.can_move_disk(self.selected_disk, selected_rod):
                    self.move_disk(self.selected_disk, self.selected_rod, selected_rod)
                    self.moves.append((self.selected_rod, selected_rod))
                    self.selected_disk = None
                    self.check_win()
                else:
                    self.rods[self.selected_rod].push(self.selected_disk)
                    self.canvas.itemconfig(self.selected_disk, fill="blue")
                    self.selected_disk = None
                    messagebox.showerror("Invalid Move", "A smaller disk cannot be placed on a larger disk.")

    def get_rod_from_coords(self, x):
        for rod, (rx, _) in self.rod_coords.items():
            if abs(x - rx) < 50:
                return rod
        return None

    def can_move_disk(self, disk, target_rod):
        if self.rods[target_rod].is_empty():
            return True
        top_disk = self.rods[target_rod].peek()
        return self.canvas.coords(disk)[2] - self.canvas.coords(disk)[0] < \
            self.canvas.coords(top_disk)[2] - self.canvas.coords(top_disk)[0]

    def move_disk(self, disk, from_rod, to_rod):
        self.canvas.itemconfig(disk, fill="blue")
        self.rods[to_rod].push(disk)

        # Calculate new position
        disk_width = (self.canvas.coords(disk)[2] - self.canvas.coords(disk)[0]) / 2
        new_x_center = self.rod_coords[to_rod][0]
        new_y = 300 - min(20, 200 // self.num_disks) * self.rods[to_rod].size()

        # Update disk position
        self.canvas.coords(
            disk,
            new_x_center - disk_width,
            new_y,
            new_x_center + disk_width,
            new_y + min(20, 200 // self.num_disks)
        )

    def check_win(self):
        if self.rods['C'].size() == self.num_disks:
            end_time = time.time()
            time_taken = end_time - self.start_time

            save_game_result(self.player_name, self.num_disks, len(self.moves), self.moves, time_taken)

            messagebox.showinfo("Congratulations!", f"You've solved the Tower of Hanoi in {time_taken:.2f} seconds!")

            if messagebox.askyesno("Play Again?", "Do you want to play again?"):
                self.ask_for_disks()
            else:
                self.back_to_menu()

    def ask_for_disks(self):
        self.root.destroy()
        disk_input_screen(self.player_name)

    def back_to_menu(self):
        self.root.destroy()
        main_menu()


def save_game_result(player_name, num_disks, num_moves, move_sequence, time_taken):
    try:
        connection = create_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO game_results (player_name, num_disks, num_moves, move_sequence, time_taken)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (player_name, num_disks, num_moves, str(move_sequence), time_taken)

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"An error occurred: {err}")


def main_menu():
    root = tk.Tk()
    root.title("Tower of Hanoi")
    root.geometry("300x200")

    label = tk.Label(root, text="Tower of Hanoi", font=("Arial", 16))
    label.pack(pady=20)

    start_button = tk.Button(root, text="Start Game", font=font.Font(size=12), command=lambda: start_game(root))
    start_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", font=font.Font(size=12), command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()


def start_game(root):
    root.destroy()
    name_input_screen()


def name_input_screen():
    root = tk.Tk()
    root.title("Player Name")
    root.geometry("300x150")

    tk.Label(root, text="Enter your name:", font=font.Font(size=12)).pack(pady=10)
    name_entry = tk.Entry(root, font=font.Font(size=12))
    name_entry.pack(pady=10)

    def submit_name():
        player_name = name_entry.get()
        if player_name:
            root.destroy()
            disk_input_screen(player_name)
        else:
            messagebox.showerror("Error", "Please enter your name.")

    submit_button = tk.Button(root, text="Submit", font=font.Font(size=12), command=submit_name)
    submit_button.pack(pady=10)

    root.mainloop()


def disk_input_screen(player_name):
    root = tk.Tk()
    root.title("Number of Disks")
    root.geometry("300x150")

    tk.Label(root, text="Enter the number of disks (1-15):", font=font.Font(size=12)).pack(pady=10)
    disk_entry = tk.Entry(root, font=font.Font(size=12))
    disk_entry.pack(pady=10)

    def submit_disks():
        try:
            num_disks = int(disk_entry.get())
            if 1 <= num_disks <= 15:  # Restricting the number of disks to a maximum of 15
                root.destroy()
                TowerOfHanoiGUI(tk.Tk(), num_disks, player_name)
            else:
                messagebox.showerror("Error", "Please enter a number between 1 and 15.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    submit_button = tk.Button(root, text="Submit", font=font.Font(size=12), command=submit_disks)
    submit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main_menu()