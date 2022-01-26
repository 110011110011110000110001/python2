from tkinter import  *

X = 400
Y = 100
WIDTH = 400
HEIGHT = 340
RESIZABLE = FALSE

root = Tk()

def save():
    name.insert(0, "Корнилов И.С.")
    date.insert(0, "06/09/2007")

    save_name = name.get()
    save_data = data.get()


if gender_value.get()
    save_gender = "Мужской"
else:save_gender = "Женский"


root.title("регистрационный лист")
root.geometry(f"{WIDTH}x{HEIGHT}x{x}x{y}")
root.resizable(RESIZABLE, RESIZABLE)



frame_name = Frame(pady=10, padx=10)
frame_name_data.pack()

Label(master=frame_name_date, text="введите ФИО:").grid(sticky=E, row=0, column=0)
name = Entry(master=frame_name_data, width=40)
name.grid(row=0, column=1)

Label(master=frame_name_date, text="введите дату рождения:").grid(sticky=E, row=1, column=0)
date = Entry(master=frame_name_data, width=40)
name.grid(row=1, column=1)



frame_gender = Frame(pady=0, padx=10)
frame_gender.pack(anchor=W)


Label(master=frame_gender, text="выберите пол").pack(anchor=W)

gender_value = BooleanVar(value=True)
Radiobutton(master=frame_gender, text="Мужской", value=True, variable=gender_value).pack(side=LEFT)
Radiobutton(master=frame_gender, text="Женский", value=True, variable=gender_value).pack(side=LEFT)

frame_interest = Frame(PADX=10, pady=10)
frame_interest.pack(anchor=W)

Label(master=frame_interest, text="Выберите интересы:").pack(anchore=W)

interested_names = ["игры, програмированние, другое"]
intrested_values = []


for i in intrested_names:
    i_value = BooleanVar()
    Checkbutton(master=frame_interest, text=i, variable=i_value).pack(anchor=W)
    interests_values.append(i_value)

    frame_button = Frame(padx=20)
    frame_button.pack(anchor=E)


    root.mainloop()



















