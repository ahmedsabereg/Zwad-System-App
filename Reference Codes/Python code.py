#_____________________________________________________________________________________________________________________________________________________
#Importation
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "UI" / "tkdesigner" / "project" / "build" / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("875x680")
window.configure(bg = "#FFFFFF")
window.title("Zwad Information App")
#_____________________________________________________________________________________________________________________________________________________


#_____________________________________________________________________________________________________________________________________________________
#Interface design:
#______________________________________________________
#1. Design
#1.1 Window
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 680,
    width = 875,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

#1.2 Window's upper rectangle
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    875.0,
    120.0,
    fill="#EF9D37",
    outline="")
#______________________________________________________

#______________________________________________________
#2. Titles
#2.1 Main title
canvas.create_text(
    228.0,
    18.0,
    anchor="nw",
    text="Zwad Information App",
    fill="#000000",
    font=("Inter Black", 35 * -1)
)

#2.2 Welcoming the user
canvas.create_text(
    161.0,
    70.0,
    anchor="nw",
    text="Welcome to Zwad program for customers’ data recording",
    fill="#000000",
    font=("Inter Medium", 20 * -1)
)
#______________________________________________________

#______________________________________________________
#3. Logos
#3.1 Zwad logo
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    825.0,
    60.0,
    image=image_image_1
)

#3.2 QR code
image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    73.0,
    60.0,
    image=image_image_20
)

#1.3 Window's lower rectangle (moved here to be above logos)
canvas.create_rectangle(
    0.0,
    126.0,
    875.0,
    688.0,
    fill="#FFF7DC",
    outline="")
#______________________________________________________

#______________________________________________________
#4. Excel sheet button
import os

def open_excel():
    from pathlib import Path
    excel_path = Path(__file__).parent / "Donations.xlsx"

    if os.path.exists(excel_path):
        os.startfile(excel_path)
    else:
        messagebox.showerror("File Error", "Excel file not found.")


button_image_excel = PhotoImage(
    file=relative_to_assets("Image_22.png"))
button_excel = Button(
    image=button_image_excel,
    borderwidth=0,
    highlightthickness=0,
    command=open_excel,
    relief="flat"
)

button_excel.place(
    x=615.0,
    y=425.0,
    width=244.0,
    height=243.0
)
#______________________________________________________

#______________________________________________________
#5. Boxes
#5.1 Shop name box
image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    179.0,
    176.0,
    image=image_image_11
)

#5.2 Seller's name box
image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    488.0,
    175.0,
    image=image_image_10
)

#5.3 Owner's name box
image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    741.0,
    175.0,
    image=image_image_9
)

#5.4 Shop address box
image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    431.0,
    273.0,
    image=image_image_8
)

#5.5 Phone number box
image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    431.0,
    367.0,
    image=image_image_7
)

#5.6 Cartoon weight box
image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    90.0,
    485.0,
    image=image_image_6
)

#5.7 Plastic weight box
image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    300.0,
    486.0,
    image=image_image_5
)

#5.8 Books weight box
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    509.0,
    485.0,
    image=image_image_4
)
#______________________________________________________

#______________________________________________________
#6. Texts
#6.1 Shop name text
canvas.create_text(
    52.0,
    144.0,
    anchor="nw",
    text="Shop name:",
    fill="#000000",
    font=("Inter Medium", 20 * -1)
)

#6.2 Seller's name text
canvas.create_text(
    410.0,
    144.0,
    anchor="nw",
    text="Seller’s name:",
    fill="#000000",
    font=("Inter Medium", 20 * -1)
)

#6.3 Owner's name text
canvas.create_text(
    670.0,
    144.0,
    anchor="nw",
    text="Owner’s name:",
    fill="#000000",
    font=("Inter Medium", 20 * -1)
)

#6.4 Shop address text
canvas.create_text(
    48.0,
    241.0,
    anchor="nw",
    text="Shop address:",
    fill="#000000",
    font=("Inter Medium", 20 * -1)
)

#6.5 Phone number text
canvas.create_text(
    57.0,
    339.0,
    anchor="nw",
    text="Phone number:",
    fill="#000000",
    font=("Inter Medium", 20 * -1)
)

#6.6 Cartoon weight text
canvas.create_text(
    44.0,
    447.0,
    anchor="nw",
    text="Cartoon weight:",
    fill="#000000",
    font=("Inter Medium", 17 * -1)
)

#6.7 Plastic weight text
canvas.create_text(
    244.0,
    447.0,
    anchor="nw",
    text="Plastic weight:",
    fill="#000000",
    font=("Inter Medium", 19 * -1)
)

#6.8 Books weight text
canvas.create_text(
    456.0,
    447.0,
    anchor="nw",
    text="Books weight:",
    fill="#000000",
    font=("Inter Medium", 19 * -1)
)
#______________________________________________________

#______________________________________________________
#7. Entries
#7.1 Shop name entry
entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    179.0,
    190.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_8.place(
    x=35.0,
    y=172.0,
    width=288.0,
    height=34.0
)

#7.2 Seller's name entry
entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    489.5,
    189.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_7.place(
    x=403.0,
    y=171.0,
    width=173.0,
    height=34.0
)

#7.3 Owner's name entry
entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    740.0,
    189.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_6.place(
    x=653.0,
    y=171.0,
    width=174.0,
    height=34.0
)

#7.4 Shop address entry
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    425.5,
    288.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_5.place(
    x=36.0,
    y=271.0,
    width=779.0,
    height=32.0
)

#7.5 Phone number entry
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    432.0,
    381.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_4.place(
    x=37.5,
    y=365.0,
    width=789.0,
    height=31.0
)

#7.6 Cartoon weight entry
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    91.0,
    499.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_3.place(
    x=38.5,
    y=478.0,
    width=105.0,
    height=41.0
)

#7.7 Plastic weight entry
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    300.5,
    500.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_2.place(
    x=246.0,
    y=478.0,
    width=109.0,
    height=42.0
)

#7.8 Books weight entry
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    507.5,
    499.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Inter", 16)
)
entry_1.place(
    x=452.5,
    y=478.0,
    width=110.0,
    height=41.0
)
#______________________________________________________

#______________________________________________________
#8. Icons
#8.1 Shop icon
image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    30.0,
    155.0,
    image=image_image_19
)

#8.2 Seller icon
image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    391.0,
    153.0,
    image=image_image_18
)

#8.3 Owner icon
image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    652.0,
    155.0,
    image=image_image_17
)

#8.4 Address icon
image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    28.0,
    251.0,
    image=image_image_16
)

#8.5 Phone icon
image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    33.0,
    349.0,
    image=image_image_15
)

#8.6 Cartoon icon
image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    26.0,
    458.0,
    image=image_image_14
)

#8.7 Plastic icon
image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    231.0,
    458.0,
    image=image_image_13
)

#8.8 Books icon
image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    441.0,
    461.0,
    image=image_image_12
)
#______________________________________________________
#_____________________________________________________________________________________________________________________________________________________


#_____________________________________________________________________________________________________________________________________________________
#Functionalities:
#______________________________________________________
#1. Tab-button adjustment
entries = [entry_8, entry_7, entry_6, entry_5, entry_4, entry_3, entry_2, entry_1]

for i, entry in enumerate(entries):
    def focus_next(event, idx=i):
        next_idx = (idx + 1) % len(entries)
        entries[next_idx].focus_set()
        return "break"
    entry.bind("<Tab>", focus_next)


from pathlib import Path
csv_path = Path(__file__).parent / "C#_table.csv"

import pandas as pd
def update_excel():
    try:
        df = pd.read_csv(csv_path)
        excel_path = Path(__file__).parent / "Donations.xlsx"
        df.to_excel(excel_path, index=False)
    except Exception as e:
        print(f"Excel update failed: {e}")
#______________________________________________________

#______________________________________________________
#2. Success window after data submission
def show_success_window():
    success_win = Tk()
    success_win.title("Success")
    success_win.geometry("300x150")
    success_win.configure(bg="#FFF7DC")

    label = Button(success_win, text="Excel sheet updated successfully!", bg="#FFF7DC", fg="#000000", borderwidth=0)
    label.pack(pady=30)

    def on_ok():
        success_win.destroy()

    ok_button = Button(success_win, text="OK", command=on_ok, width=10)
    ok_button.pack(pady=10)

    success_win.mainloop()
#______________________________________________________

#______________________________________________________
#3. Data retrieval and processing
def get_data():
    shop = entry_8.get().title()
    name = entry_7.get().title()
    owner = entry_6.get().title()
    address = entry_5.get()
    phone = entry_4.get().strip()

    ##3.1 Empty field checking process
    if not shop:
        messagebox.showerror("Input Error", "Shop name must be inserted.")
        return
    if not name:
        messagebox.showerror("Input Error", "Seller name must be inserted.")
        return
    if not owner:
        messagebox.showerror("Input Error", "Owner name must be inserted.")
        return
    if not address:
        messagebox.showerror("Input Error", "Shop address must be written.")
        return
    if not phone:
        messagebox.showerror("Input Error", "Phone number must be written.")
        return

    #3.2 Invalid inputs checking process
    if not all(char.isalpha() or char.isspace() or char.isdigit() for char in shop):
        messagebox.showerror("Invalid shop name", "It should contain only letters.")
        return
    if not all(char.isalpha() or char.isspace() for char in name):
        messagebox.showerror("Invalid seller name", "It should contain only letters.")
        return
    if not all(char.isalpha() or char.isspace() for char in owner):
        messagebox.showerror("Invalid owner name", "It should contain only letters.")
        return
    if not (phone.isdigit() and len(phone) == 11):
        messagebox.showerror("Invalid phone number", "It should contain only numbers.")
        return

    try:
       weightc = float(entry_3.get())
       weightp = float(entry_2.get())
       weightb = float(entry_1.get())
    except ValueError:
       messagebox.showerror("Invalid weight", "It should contain only numbers.")
       return

    if weightc < 0 or weightp < 0 or weightb < 0:
       messagebox.showerror("Input Error", "Weight must be positive.")
       return

    #3.3 Date and time importation
    from datetime import datetime
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #3.4 Total weight, price, and points calculations
    weight = weightc + weightp + weightb
    price = (weightc * 15) + (weightp * 10) + (weightb * 5)
    points = price / 10

    #3.5 Outputs
    print(f"\nDonation accepted!\n")
    print(f"Shop name: {shop}")
    print(f"Seller's name: {name}")
    print(f"Owner's name: {owner}")
    print(f"Shop's address: {address}")
    print(f"Phone number: {phone}")
    print(f"Date & time: {time}")
    print(f"Cartoon weight: {weightc} kg")
    print(f"Plastic weight: {weightp} kg")
    print(f"Books weight: {weightb} kg")
    print(f"Total weight: {round(weight, 2)} kg")
    print(f"Total price: {round(price, 2)}L.E.")
    print(f"Points: {round(points, 0)} points")

    #3.6 Save outputs to CSV
    import os
    import csv   

    file_exists = os.path.isfile(csv_path)
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Shop", "Seller", "Owner", "Address", "Phone", "Timestamp", "Cartoon", "Plastic", "Books", "Price", "Points"])
        writer.writerow([shop, name, owner, address, phone, time, weightc, weightp, weightb, round(price, 2), round(points, 0)])

    #3.7 Call the C# export EXE after saving the CSV if it exists
    import subprocess
    from pathlib import Path
    exe_path = Path(__file__).parent / "ExportApp" / "bin" / "Release" / "net9.0" / "ExportApp.exe"
    if os.path.exists(exe_path):
        subprocess.run([exe_path])
        button_1.config(image=button_image_success)
        window.after(2000, lambda: button_1.config(image=button_image_1))
        button_1.config(image=button_image_success, state="disabled")
        window.after(2000, lambda: button_1.config(image=button_image_1, state="normal"))

    else:
        update_excel()  
        button_1.config(image=button_image_success)
        window.after(2000, lambda: button_1.config(image=button_image_1))
        button_1.config(image=button_image_success, state="disabled")
        window.after(2000, lambda: button_1.config(image=button_image_1, state="normal"))

    #3.8 Clear entries after submission
    for entry in entries:
        entry.delete(0, 'end')
    entry_8.focus_set()
#_____________________________________________________________________________________________________________________________________________________

#_____________________________________________________________________________________________________________________________________________________
#______________________________________________________
#Finalization:
#1. Submit button
button_image_success = PhotoImage(file=relative_to_assets("button_image_success.png"))

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=get_data,
    relief="flat"
)
button_1.place(
    x=6.0,
    y=574.0,
    width=588.0,
    height=78.11346435546875
)


#2. Enter key binding to submit data
window.bind("<Return>", lambda event: get_data())
window.resizable(False, False)
window.mainloop()
#______________________________________________________
#_____________________________________________________________________________________________________________________________________________________