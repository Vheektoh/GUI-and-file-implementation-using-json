from tkinter import *
import random
from tkinter import messagebox
import json

# =================GENERATE RANDOM CLASS===========
def generate_class():
    all_game_classes = ["Defender", "Airborne", "Refitter", "Ninja", "Smoke Bomber", "Poltergeist", "Trickster",
                        "Trap Master", "Spotter", "Medic", "Mechanic", "Desperado", "Rewind"]
    new_class = random.choice(all_game_classes)
    Class_entry.insert(0, new_class)


# ================SAVE FILE=======================
def save():

    InGameName = InGameName_entry.get()
    UserID = UserID_entry.get()
    Class = Class_entry.get()
    Country = Country_entry.get()
    new_dict = {
        InGameName: {
            "UserID": UserID,
            "Class": Class,

    }}

    if len(InGameName)==0 or len(UserID)==0:
        messagebox.showinfo(title="OOPs", message="Please make sure you have not left any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=InGameName,
                                       message=f"Please make sure your details were entered correctly:"
                                               f"\nInGameName:{InGameName}\n UserID:{UserID}\n Class: "
                                               f"{Class}\n Country:{Country}\nIs it okay to save? ")
        if is_ok:
            with open("data.json", "r") as data_file:
                # Reading old data
                data_n = json.load(data_file)

            #Updating old data with new data
            json.update(data_n)

            with open("data.json","W") as data_file:
                #Saving updated data
                json.dump(data_n, data_file, indent=4)


            InGameName_entry.delete(0, END)
            UserID_entry.delete(0, END)
            Class_entry.delete(0, END)
            Country_entry.delete(0, END)



# ==================USER INTERFACE===================
# WINDOW
screen = Tk()
screen.title("CALL OF DUTY REGISTER")
screen.minsize(width=500,height=500)
screen.config(padx=50, pady=50)

# LABELS
InGameName = Label(text="InGameName:")
InGameName.grid(row=1, column=0)
UserID = Label(text="UserID:")
UserID.grid(row=2, column=0)
Class = Label(text="Class:")
Class.grid(row=3,column=0)
Country = Label(text="Country:")
Country.grid(row=4,column=0)

# ENTRIES
InGameName_entry = Entry(width=30)
InGameName_entry.grid(row=1, column=1)
InGameName_entry.focus()
UserID_entry = Entry(width=30)
UserID_entry.grid(row=2, column=1)
Class_entry = Entry(width=30)
Class_entry.grid(row=3, column=1)
Country_entry = Entry(width=30)
Country_entry.grid(row=4, column=1)


#BUTTONS
GenerateClass = Button(text="Generate Class", command=generate_class)
GenerateClass.grid(row=3, column=3)
Add = Button(text="Add",command=save)
Add.grid(row=1, column=3)
Search = Button(text="Search")
Search.grid(row=2, column=3)


canvas = Canvas(width=300,height=300)
image_logo = PhotoImage(file="call of duty picsssss.png")
canvas.create_image(150,150,image=image_logo)
canvas.grid(row=0, column=1,columnspan=2)



screen.mainloop()