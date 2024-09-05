import os
import subprocess
import sys
from pathlib import Path
from tkinter import Tk, Entry, PhotoImage, Button, Canvas

import mysql
import mysql.connector

from algo.Bellman_Ford_algo import get_path
from algo import random_no_generator, Bellman_Ford_algo, Dijkstra_algorithm

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Game/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#path
code_dir = Path(r"C:\Users\kusal\PycharmProjects\pdsa\algo")
sys.path.append(str(code_dir))

# Generated numbers and letters
genrandom_numbers = random_no_generator.random_numbers
genrandom_letter = random_no_generator.random_letter

shortest_paths = Bellman_Ford_algo.shortest_paths
cities = Bellman_Ford_algo.cities
predecessors = Bellman_Ford_algo.predecessors
start_city_idx = Bellman_Ford_algo.start_city_idx

bellman_time = Bellman_Ford_algo.bellman_time
dijkstra_time = Dijkstra_algorithm.dijkstra_time

window = Tk()
window.geometry("1440x1059")
window.configure(bg="#002D44")

distance_A = [0] * 20


def submit_handler():
    try:
        distance_A[0] = int(entry_1.get())
        distance_A[1] = int(entry_2.get())
        distance_A[2] = int(entry_3.get())
        distance_A[3] = int(entry_4.get())
        distance_A[4] = int(entry_5.get())
        distance_A[5] = int(entry_6.get())
        distance_A[6] = int(entry_7.get())
        distance_A[7] = int(entry_8.get())
        distance_A[8] = int(entry_9.get())
        distance_A[9] = int(entry_10.get())
        distance_A[10] = entry_11.get()
        distance_A[11] = entry_12.get()
        distance_A[12] = entry_13.get()
        distance_A[13] = entry_14.get()
        distance_A[14] = entry_15.get()
        distance_A[15] = entry_16.get()
        distance_A[16] = entry_17.get()
        distance_A[17] = entry_18.get()
        distance_A[18] = entry_19.get()
        distance_A[19] = entry_20.get()

    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def display():
    print("Values in the distance_A array:")
    for i in range(len(distance_A)):
        print(f"Element at index {i}: {distance_A[i]}")


def validate_user_input():
    is_valid = True
    for i in range(10):
        user_distance = distance_A[i]
        correct_distance = shortest_paths[i]
        if user_distance is not None and user_distance != correct_distance:
            print(f"Incorrect distance for City {cities[i]}: Expected {correct_distance}, got {user_distance}")
            is_valid = False

        elif user_distance is None:
            is_valid = False

    for i in range(10, 20):
        user_path = distance_A[i]
        correct_path = ''.join(get_path(predecessors, start_city_idx, i - 10))
        if user_path is not None and user_path != correct_path:
            print(f"Incorrect path for City {cities[i - 10]}: Expected {correct_path}, got {user_path}")
            is_valid = False

        elif user_path is None:
            is_valid = False

    if is_valid:
        print("All inputs are correct!")
        save_data_to_database(
            name="Player Name",
            time_bellman_ford=bellman_time,
            time_dijkstra=dijkstra_time,
            distance_A=distance_A,
        )

        # Open the new GUI script after saving data
        new_page_path = r"C:\Users\kusal\PycharmProjects\pdsa\gui_entername\build\gui.py"
        try:
            subprocess.run(['python', new_page_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while opening new page: {e}")

    else:
        print("Some inputs are incorrect.")
        new_page_path = r"C:\Users\kusal\PycharmProjects\pdsa\youlose\build\gui.py"
        try:
            subprocess.run(['python', new_page_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while opening new page: {e}")




def save_data_to_database(name, time_bellman_ford, time_dijkstra, distance_A):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pdsa_2'
        )

        cursor = connection.cursor()
        cursor.execute("SELECT MAX(game_round) FROM shortest_path")
        last_round = cursor.fetchone()[0]  # Fetch the last round number

        game_round = (last_round + 1) if last_round is not None else 1

        insert_query = """
        INSERT INTO shortest_path (
            game_round, name, Time_Bellman_Ford, Time_Dijkstra, distance_A, distance_B, distance_C, distance_D, distance_E, distance_F, distance_G, distance_H, distance_I, distance_J, path_A, path_B, path_C, path_D, path_E, path_F, path_G, path_H, path_I, path_J
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            game_round, name, time_bellman_ford, time_dijkstra, distance_A[0], distance_A[1], distance_A[2],
            distance_A[3], distance_A[4], distance_A[5], distance_A[6], distance_A[7], distance_A[8], distance_A[9],
            distance_A[10], distance_A[11], distance_A[12], distance_A[13], distance_A[14], distance_A[15],
            distance_A[16], distance_A[17], distance_A[18], distance_A[19]
        )

        cursor.execute(insert_query, data)
        connection.commit()

        print("Data saved successfully.")



    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


canvas = Canvas(
    window,
    bg = "#002D44",
    height = 1059,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    1153.1429061889648,
    565.0,
    1255.0,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    1175.0,
    584.0,
    anchor="nw",
    text="City J",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    1041.6824569702148,
    565.0,
    1143.53955078125,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    1064.021484375,
    584.2286987304688,
    anchor="nw",
    text="City I",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    930.2222518920898,
    565.0,
    1032.079345703125,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    950.6690063476562,
    584.2286987304688,
    anchor="nw",
    text="City H",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    818.7619857788086,
    565.0,
    920.6190795898438,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    841.0000610351562,
    584.0,
    anchor="nw",
    text="City G",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    707.3016586303711,
    565.0,
    809.1587524414062,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    729.5664672851562,
    584.2286987304688,
    anchor="nw",
    text="City F",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    595.8413314819336,
    565.0,
    697.6984252929688,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    617.8145751953125,
    584.2286987304688,
    anchor="nw",
    text="City E",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    484.3810043334961,
    565.0,
    586.2380981445312,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    507.0000305175781,
    584.0,
    anchor="nw",
    text="City D",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    372.9209213256836,
    565.0,
    474.77801513671875,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    395.0,
    584.0,
    anchor="nw",
    text="City C",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    261.4606246948242,
    565.0,
    363.3177185058594,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    283.35943603515625,
    584.2286987304688,
    anchor="nw",
    text="City B",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    149.99999237060547,
    565.0,
    251.85708618164062,
    626.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    172.0,
    584.0,
    anchor="nw",
    text="City A",
    fill="#000000",
    font=("Inter", 20 * -1)
)


canvas.create_text(
    311.0000305175781,
    522.0,
    anchor="nw",
    text="Taking ",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    405.0000305175781,
    522.0,
    anchor="nw",
    text="as starting city find the shortest path and distance for other cities ",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    383.0000305175781,
    521.0,
    anchor="nw",
    text=f"{genrandom_letter}    ",
    fill="#FFD800",
    font=("Inter ExtraBold", 20 * -1)
)

canvas.create_rectangle(
    330.0,
    425.0,
    399.0,
    457.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    433.0,
    anchor="nw",
    text="City J",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    458.0,
    469.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    417.0,
    466.0,
    anchor="nw",
    text="City A",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    458.0,
    539.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    487.0,
    466.0,
    anchor="nw",
    text="City B",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    458.0,
    609.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    557.0,
    466.0,
    anchor="nw",
    text="City C",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    458.0,
    679.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    627.0,
    466.0,
    anchor="nw",
    text="City D",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    458.0,
    749.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    697.0,
    466.0,
    anchor="nw",
    text="City E",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    750.0,
    458.0,
    819.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    767.0,
    466.0,
    anchor="nw",
    text="City F",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    820.0,
    458.0,
    889.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    837.0,
    466.0,
    anchor="nw",
    text="City G",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    890.0,
    458.0,
    959.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    907.0,
    466.0,
    anchor="nw",
    text="City H",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    425.0,
    469.0,
    457.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[0],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    425.0,
    539.0,
    457.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    496.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[1],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    425.0,
    609.0,
    457.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    566.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[2],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    425.0,
    679.0,
    457.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    636.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[3],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    425.0,
    749.0,
    457.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    706.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[4],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    750.0,
    425.0,
    819.0,
    457.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    776.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[5],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    820.0,
    425.0,
    889.0,
    457.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    846.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[6],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    890.0,
    425.0,
    959.0,
    457.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    916.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[7],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    960.0,
    458.0,
    1029.0,
    490.0,
    fill="#F6FA81",
    outline="")

canvas.create_text(
    977.0,
    466.0,
    anchor="nw",
    text="City I",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    960.0,
    425.0,
    1029.0,
    457.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    986.0,
    433.0,
    anchor="nw",
    text=genrandom_numbers[8],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    330.0,
    392.0,
    399.0,
    424.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    400.0,
    anchor="nw",
    text="City I",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    392.0,
    469.0,
    424.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    400.0,
    anchor="nw",
    text=genrandom_numbers[9],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    392.0,
    539.0,
    424.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    496.0,
    401.0,
    anchor="nw",
    text=genrandom_numbers[10],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    392.0,
    609.0,
    424.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    566.0,
    400.0,
    anchor="nw",
    text=genrandom_numbers[11],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    392.0,
    679.0,
    424.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    636.0,
    400.0,
    anchor="nw",
    text=genrandom_numbers[12],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    392.0,
    749.0,
    424.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    706.0,
    400.0,
    anchor="nw",
    text=genrandom_numbers[13],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    750.0,
    392.0,
    819.0,
    424.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    776.0,
    400.0,
    anchor="nw",
    text=genrandom_numbers[14],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    820.0,
    392.0,
    889.0,
    424.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    846.0,
    400.0,
    anchor="nw",
    text=genrandom_numbers[15],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    890.0,
    392.0,
    959.0,
    424.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    916.0,
    400.0,
    anchor="nw",
    text=genrandom_numbers[16],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    960.0,
    392.0,
    1029.0,
    424.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    986.0,
    401.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    330.0,
    359.0,
    399.0,
    391.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    367.0,
    anchor="nw",
    text="City H",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    359.0,
    469.0,
    391.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    367.0,
    anchor="nw",
    text=genrandom_numbers[17],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    359.0,
    539.0,
    391.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    496.0,
    367.0,
    anchor="nw",
    text=genrandom_numbers[18],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    359.0,
    609.0,
    391.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    566.0,
    367.0,
    anchor="nw",
    text=genrandom_numbers[19],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    359.0,
    679.0,
    391.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    636.0,
    367.0,
    anchor="nw",
    text=genrandom_numbers[20],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    359.0,
    749.0,
    391.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    706.0,
    367.0,
    anchor="nw",
    text=genrandom_numbers[21],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    750.0,
    359.0,
    819.0,
    391.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    776.0,
    367.0,
    anchor="nw",
    text=genrandom_numbers[22],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    820.0,
    359.0,
    889.0,
    391.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    846.0,
    367.0,
    anchor="nw",
    text=genrandom_numbers[23],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    890.0,
    359.0,
    959.0,
    391.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    916.0,
    368.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    960.0,
    359.0,
    1029.0,
    391.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    326.0,
    399.0,
    358.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    334.0,
    anchor="nw",
    text="City G",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    326.0,
    469.0,
    358.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    334.0,
    anchor="nw",
    text=genrandom_numbers[24],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    326.0,
    539.0,
    358.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    496.0,
    334.0,
    anchor="nw",
    text=genrandom_numbers[25],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    326.0,
    609.0,
    358.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    566.0,
    334.0,
    anchor="nw",
    text=genrandom_numbers[26],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    326.0,
    679.0,
    358.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    636.0,
    334.0,
    anchor="nw",
    text=genrandom_numbers[27],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    326.0,
    749.0,
    358.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    706.0,
    334.0,
    anchor="nw",
    text=genrandom_numbers[28],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    750.0,
    326.0,
    819.0,
    358.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    776.0,
    334.0,
    anchor="nw",
    text=genrandom_numbers[29],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    820.0,
    326.0,
    889.0,
    358.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    846.0,
    335.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    890.0,
    326.0,
    959.0,
    358.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    326.0,
    1029.0,
    358.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    293.0,
    399.0,
    325.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    301.0,
    anchor="nw",
    text="City F",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    293.0,
    469.0,
    325.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    301.0,
    anchor="nw",
    text=genrandom_numbers[30],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    293.0,
    539.0,
    325.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    496.0,
    301.0,
    anchor="nw",
    text=genrandom_numbers[31],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    293.0,
    609.0,
    325.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    566.0,
    301.0,
    anchor="nw",
    text=genrandom_numbers[32],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    293.0,
    679.0,
    325.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    636.0,
    301.0,
    anchor="nw",
    text=genrandom_numbers[33],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    293.0,
    749.0,
    325.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    706.0,
    301.0,
    anchor="nw",
    text=genrandom_numbers[34],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    750.0,
    293.0,
    819.0,
    325.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    776.0,
    302.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    820.0,
    293.0,
    889.0,
    325.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    293.0,
    959.0,
    325.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    293.0,
    1029.0,
    325.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    260.0,
    399.0,
    292.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    268.0,
    anchor="nw",
    text="City E",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    260.0,
    469.0,
    292.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    268.0,
    anchor="nw",
    text=genrandom_numbers[35],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    260.0,
    539.0,
    292.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    496.0,
    268.0,
    anchor="nw",
    text=genrandom_numbers[36],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    260.0,
    609.0,
    292.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    566.0,
    268.0,
    anchor="nw",
    text=genrandom_numbers[37],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    260.0,
    679.0,
    292.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    636.0,
    268.0,
    anchor="nw",
    text=genrandom_numbers[38],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    260.0,
    749.0,
    292.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    706.0,
    269.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    750.0,
    260.0,
    819.0,
    292.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    260.0,
    889.0,
    292.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    260.0,
    959.0,
    292.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    260.0,
    1029.0,
    292.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    227.0,
    399.0,
    259.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    235.0,
    anchor="nw",
    text="City D",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    227.0,
    469.0,
    259.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    235.0,
    anchor="nw",
    text=genrandom_numbers[39],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    227.0,
    539.0,
    259.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    496.0,
    235.0,
    anchor="nw",
    text=genrandom_numbers[40],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    227.0,
    609.0,
    259.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    566.0,
    235.0,
    anchor="nw",
    text=genrandom_numbers[41],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    227.0,
    679.0,
    259.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    636.0,
    236.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    227.0,
    749.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    750.0,
    227.0,
    819.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    227.0,
    889.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    227.0,
    959.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    227.0,
    1029.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    194.0,
    399.0,
    226.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    202.0,
    anchor="nw",
    text="City C",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    194.0,
    469.0,
    226.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    202.0,
    anchor="nw",
    text=genrandom_numbers[42],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    194.0,
    539.0,
    226.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    496.0,
    202.0,
    anchor="nw",
    text=genrandom_numbers[43],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    194.0,
    609.0,
    226.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    566.0,
    203.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    194.0,
    679.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    680.0,
    194.0,
    749.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    750.0,
    194.0,
    819.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    194.0,
    889.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    194.0,
    959.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    194.0,
    1029.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    161.0,
    399.0,
    193.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    169.0,
    anchor="nw",
    text="City B",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    161.0,
    469.0,
    193.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    426.0,
    169.0,
    anchor="nw",
    text=genrandom_numbers[44],
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    161.0,
    539.0,
    193.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    496.0,
    170.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    161.0,
    609.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    610.0,
    161.0,
    679.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    680.0,
    161.0,
    749.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    750.0,
    161.0,
    819.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    161.0,
    889.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    161.0,
    959.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    161.0,
    1029.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    128.0,
    399.0,
    160.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    136.0,
    anchor="nw",
    text="City A",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    128.0,
    469.0,
    160.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    426.0,
    136.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    128.0,
    539.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    540.0,
    128.0,
    609.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    610.0,
    128.0,
    679.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    680.0,
    128.0,
    749.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    750.0,
    128.0,
    819.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    128.0,
    889.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    128.0,
    959.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    128.0,
    1029.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_text(
    856.0,
    91.0,
    anchor="nw",
    text="Distance Between cities in KM",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    200.92853927612305,
    662.8013877868652,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=164.99999237060547,
    y=632.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    312.24128341674805,
    663.0319175720215,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=276.31273651123047,
    y=632.5,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    423.8494682312012,
    662.8013877868652,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=387.9209213256836,
    y=632.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    535.3095512390137,
    662.8013877868652,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=499.3810043334961,
    y=632.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    646.7698783874512,
    662.8013877868652,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=610.8413314819336,
    y=632.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    758.2302055358887,
    662.8013877868652,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=722.3016586303711,
    y=632.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    869.6905326843262,
    662.8013877868652,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=833.7619857788086,
    y=632.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    981.1507987976074,
    662.8013877868652,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=945.2222518920898,
    y=632.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    1092.6110038757324,
    662.8013877868652,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=1056.6824569702148,
    y=632.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    1204.0714530944824,
    662.7985191345215,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=1168.1429061889648,
    y=632.2666015625,
    width=71.85709381103516,
    height=59.06383514404297
)
canvas.create_rectangle(
    540.0,
    227.0,
    609.0,
    259.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    566.0,
    235.0,
    anchor="nw",
    text="41",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    227.0,
    679.0,
    259.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    636.0,
    236.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    680.0,
    227.0,
    749.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    750.0,
    227.0,
    819.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    227.0,
    889.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    227.0,
    959.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    227.0,
    1029.0,
    259.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    194.0,
    399.0,
    226.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    202.0,
    anchor="nw",
    text="City C",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    194.0,
    469.0,
    226.0,
    fill="#F6E208",
    outline="")

canvas.create_text(
    426.0,
    202.0,
    anchor="nw",
    text="42",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    194.0,
    539.0,
    226.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    496.0,
    202.0,
    anchor="nw",
    text="43",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    194.0,
    609.0,
    226.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    566.0,
    203.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    610.0,
    194.0,
    679.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    680.0,
    194.0,
    749.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    750.0,
    194.0,
    819.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    194.0,
    889.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    194.0,
    959.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    194.0,
    1029.0,
    226.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    161.0,
    399.0,
    193.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    169.0,
    anchor="nw",
    text="City B",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    161.0,
    469.0,
    193.0,
    fill="#F6E308",
    outline="")

canvas.create_text(
    426.0,
    169.0,
    anchor="nw",
    text="44",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    161.0,
    539.0,
    193.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    496.0,
    170.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    540.0,
    161.0,
    609.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    610.0,
    161.0,
    679.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    680.0,
    161.0,
    749.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    750.0,
    161.0,
    819.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    161.0,
    889.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    161.0,
    959.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    161.0,
    1029.0,
    193.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    330.0,
    128.0,
    399.0,
    160.0,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    348.0,
    136.0,
    anchor="nw",
    text="City A",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    400.0,
    128.0,
    469.0,
    160.0,
    fill="#4D6ADE",
    outline="")

canvas.create_text(
    426.0,
    136.0,
    anchor="nw",
    text="---",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_rectangle(
    470.0,
    128.0,
    539.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    540.0,
    128.0,
    609.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    610.0,
    128.0,
    679.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    680.0,
    128.0,
    749.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    750.0,
    128.0,
    819.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    820.0,
    128.0,
    889.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    890.0,
    128.0,
    959.0,
    160.0,
    fill="#4732BA",
    outline="")

canvas.create_rectangle(
    960.0,
    128.0,
    1029.0,
    160.0,
    fill="#4732BA",
    outline="")


canvas.create_rectangle(
    1153.1429061889648,
    755.0,
    1255.0,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    1175.0,
    774.0,
    anchor="nw",
    text="City J",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    1041.6824569702148,
    755.0,
    1143.53955078125,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    1064.021484375,
    774.2286987304688,
    anchor="nw",
    text="City I",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    930.2222518920898,
    755.0,
    1032.079345703125,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    950.6690063476562,
    774.2286987304688,
    anchor="nw",
    text="City H",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    818.7619857788086,
    755.0,
    920.6190795898438,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    841.0000610351562,
    774.0,
    anchor="nw",
    text="City G",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    707.3016586303711,
    755.0,
    809.1587524414062,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    729.5664672851562,
    774.2286987304688,
    anchor="nw",
    text="City F",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    595.8413314819336,
    755.0,
    697.6984252929688,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    617.8145751953125,
    774.2286987304688,
    anchor="nw",
    text="City E",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    484.3810043334961,
    755.0,
    586.2380981445312,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    507.0000305175781,
    774.0,
    anchor="nw",
    text="City D",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    372.9209213256836,
    755.0,
    474.77801513671875,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    395.0,
    774.0,
    anchor="nw",
    text="City C",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    261.4606246948242,
    755.0,
    363.3177185058594,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    283.35943603515625,
    774.2286987304688,
    anchor="nw",
    text="City B",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    149.99999237060547,
    755.0,
    251.85708618164062,
    816.063835144043,
    fill="#F7FB82",
    outline="")

canvas.create_text(
    172.0,
    774.0,
    anchor="nw",
    text="City A",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    311.0000305175781,
    712.0,
    anchor="nw",
    text="Taking ",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    405.0000305175781,
    712.0,
    anchor="nw",
    text="as starting city find the shortest path for other cities ",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    383.0000305175781,
    711.0,
    anchor="nw",
    text="x ",
    fill="#FFD800",
    font=("Inter ExtraBold", 20 * -1)
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    200.92853927612305,
    852.8013877868652,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=164.99999237060547,
    y=822.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    312.24128341674805,
    853.0319175720215,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=276.31273651123047,
    y=822.5,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    423.8494682312012,
    852.8013877868652,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=387.9209213256836,
    y=822.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    535.3095512390137,
    852.8013877868652,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=499.3810043334961,
    y=822.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    646.7698783874512,
    852.8013877868652,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=610.8413314819336,
    y=822.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    758.2302055358887,
    852.8013877868652,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=722.3016586303711,
    y=822.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    869.6905326843262,
    852.8013877868652,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=833.7619857788086,
    y=822.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    981.1507987976074,
    852.8013877868652,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=945.2222518920898,
    y=822.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    1092.6110038757324,
    852.8013877868652,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=1056.6824569702148,
    y=822.2694702148438,
    width=71.85709381103516,
    height=59.06383514404297
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    1204.0714530944824,
    852.7985191345215,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_20.place(
    x=1168.1429061889648,
    y=822.2666015625,
    width=71.85709381103516,
    height=59.06383514404297
)
"""
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

def combined_function():
    submit_handler()  # First method
    validate_user_input()  # Second method




button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=combined_function,
    relief="flat"
)
button_1.place(
    x=605.0,
    y=928.0,
    width=229.0,
    height=52.0
)
"""
def combined_function():
    submit_handler()  # First method
    validate_user_input()  # Second method


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=combined_function,
    relief="flat"
)
button_1.place(
    x=605.0,
    y=928.0,
    width=229.0,
    height=52.0
)


def Close():

    # Close the existing window
    window.destroy()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Close,
    relief="flat"
)
button_2.place(
    x=951.0,
    y=928.0,
    width=229.0,
    height=52.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=160.0,
    y=928.0,
    width=229.0,
    height=52.0
)



window.resizable(False, False)
window.mainloop()
