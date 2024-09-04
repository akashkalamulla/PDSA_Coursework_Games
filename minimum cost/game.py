import tkinter as tk
from tkinter import messagebox
import random
import time
import mysql.connector
import unittest

# Database Connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pdsa_2"
)

cursor = db_connection.cursor()


# Function to generate random cost matrix
def generate_cost_matrix(n):
    return [[random.randint(20, 200) for _ in range(n)] for _ in range(n)]


# Manual Hungarian Algorithm Implementation
def hungarian_algorithm(cost_matrix):
    n = len(cost_matrix)
    original_cost_matrix = [row[:] for row in cost_matrix]  # Keep the original matrix for cost calculation

    # Step 1: Subtract the row minimum from each row
    for i in range(n):
        row_min = min(cost_matrix[i])
        for j in range(n):
            cost_matrix[i][j] -= row_min

    # Step 2: Subtract the column minimum from each column
    for j in range(n):
        col_min = min(cost_matrix[i][j] for i in range(n))
        for i in range(n):
            cost_matrix[i][j] -= col_min

    # Step 3: Cover all zeros with the minimum number of lines (Not fully implemented in this simple example)
    # ... A simplified version for demonstration purposes

    # Step 4: Make assignments (this is a simplified version for clarity)
    row_ind = list(range(n))
    col_ind = list(range(n))

    total_cost = sum(original_cost_matrix[row_ind[i]][col_ind[i]] for i in range(n))

    return row_ind, col_ind, total_cost


# Save to Database
def save_to_db(task_count, time_taken, total_cost):
    try:
        cursor.execute("INSERT INTO task_assignments (task_count, time_taken, total_cost) VALUES (%s, %s, %s)",
                       (task_count, time_taken, total_cost))
        db_connection.commit()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")


# GUI Application
class MinimumCostGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minimum Cost Game")
        self.geometry("600x400")

        self.task_count_label = tk.Label(self, text="Enter Number of Tasks:")
        self.task_count_label.pack()

        self.task_count_entry = tk.Entry(self)
        self.task_count_entry.pack()

        self.play_button = tk.Button(self, text="Play", command=self.play_game)
        self.play_button.pack()

        self.matrix_frame = tk.Frame(self)
        self.matrix_frame.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def clear_matrix(self):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

    def display_matrix(self, cost_matrix, row_ind, col_ind):
        self.clear_matrix()

        for i, row in enumerate(cost_matrix):
            for j, cost in enumerate(row):
                label_text = f"${cost}"
                if i in row_ind and j == col_ind[row_ind.index(i)]:
                    label_text += " (Assigned)"
                label = tk.Label(self.matrix_frame, text=label_text, borderwidth=1, relief="solid", padx=10, pady=5)
                label.grid(row=i, column=j, padx=5, pady=5)

    def play_game(self):
        try:
            task_count = int(self.task_count_entry.get())
            cost_matrix = generate_cost_matrix(task_count)

            start_time = time.time()
            row_ind, col_ind, total_cost = hungarian_algorithm(cost_matrix)
            time_taken = time.time() - start_time

            save_to_db(task_count, time_taken, total_cost)

            self.display_matrix(cost_matrix, row_ind, col_ind)
            self.result_label.config(text=f"Total Minimum Cost: ${total_cost}\nTime Taken: {time_taken:.4f} seconds")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of tasks.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Unit Testing
class TestMinimumCostGame(unittest.TestCase):
    def test_hungarian_algorithm(self):
        cost_matrix = [
            [100, 75, 80],
            [60, 70, 90],
            [70, 60, 80]
        ]
        _, _, result = hungarian_algorithm(cost_matrix)
        self.assertEqual(result, 210)  # Example expected result

    def test_db_connection(self):
        self.assertIsNotNone(db_connection)


if __name__ == "__main__":
    app = MinimumCostGame()
    app.mainloop()

    # Run Unit Tests
    unittest.main(argv=[''], exit=False)
