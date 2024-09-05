import subprocess
from pathlib import Path
from tkinter import Tk, Entry, PhotoImage, Button, Canvas

import mysql
import mysql.connector


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/game_ui/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def getname():
    name=entry_1.get()
    save_name_to_database(name)

def save_name_to_database(name):
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

        if last_round is not None:
            # If there is an existing game_round, update the name
            update_query = """
            UPDATE shortest_path SET name = %s WHERE game_round = %s
            """
            data = (name, last_round)
            cursor.execute(update_query, data)
        else:
            # If no previous rounds exist, insert the new record
            game_round = 1
            insert_query = """
            INSERT INTO shortest_path (game_round, name) VALUES (%s, %s)
            """
            data = (game_round, name)
            cursor.execute(insert_query, data)

        connection.commit()
        print("Name saved successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def on_enter_pressed(event):
    name = entry_1.get()
    if name:
        save_name_to_database(name)
    else:
        print("Name field cannot be empty!")


window = Tk()
window.geometry("1440x679")
window.configure(bg="#002D44")

canvas = Canvas(
    window,
    bg="#002D44",
    height=679,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)


canvas.create_text(
    471.0,
    156.0,
    anchor="nw",
    text="You are the Winner!!!!!",
    fill="#FFFFFF",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    595.0,
    240.0,
    anchor="nw",
    text="Enter Your name",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)
"""
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=getname,
    relief="flat"
)
button_1.place(
    x=616.0,
    y=489.0,
    width=229.0,
    height=52.0
)
"""

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=getname,
    relief="flat"
)
button_1.place(
    x=388.0,
    y=489.0,
    width=229.0,
    height=52.0
)


def restart():
    new_page_path = r"C:\Users\kusal\PycharmProjects\pdsa\gui-game\build\gui.py"
    try:
        subprocess.run(['python', new_page_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while opening new page: {e}")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=restart,
    relief="flat"
)
button_2.place(
    x=648.0,
    y=489.0,
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
    x=901.0,
    y=489.0,
    width=229.0,
    height=52.0
)


entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    719.5,
    351.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#4D6ADE",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=315.0,
    y=321.0,
    width=809.0,
    height=59.0
)

entry_1.bind("<Return>", on_enter_pressed)  # Bind Enter key to the handler

window.resizable(False, False)
window.mainloop()
