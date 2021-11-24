# we are going to create covid-19 track record for a clinic

from tkinter import *

from datetime import *

root = Tk()
root.title("Covid-19 Test Records")
root.geometry("300x300")
root.resizable(width=None, height=None)


class Storage:
    title_label = Label(root, text="Fill this record form").grid(row=0, column=0)
    clinic_label = Label(root, text="Clinic name: ").grid(row=1, column=0)
    fname_label = Label(root, text="First name: ").grid(row=2, column=0)
    lname_label = Label(root, text="Last name: ").grid(row=3, column=0)
    gender_label = Label(root, text="Gender: ").grid(row=4, column=0)
    ID_label = Label(root, text="ID number: ").grid(row=5, column=0)
    nationality_label = Label(root, text="Nationality: ").grid(row=6, column=0)
    age_label = Label(root, text= "age: ").grid(row=10, column=0)
    location_label = Label(root, text="Location: ").grid(row=11, column=0)
    test_cite_label = Label(root, text="Test cite: ").grid(row=12, column=0)

    record_storage = {
        "clinic": [],
        "first name": [],
        "last name": [],
        "gender": [],
        "ID": [],
        "nationality": [],
        "age": [],
        "location": [],
        "test cite": []
    }

    def __init__(self):
        self.clinic = Entry(root)
        self.clinic.grid(row=1, column=1)
        self.fname = Entry(root)
        self.fname.grid(row=2, column=1)
        self.lname = Entry(root)
        self.lname.grid(row=3, column=1)
        self.gender = Entry(root)
        self.gender.grid(row=4, column=1)
        self.id = Entry(root)
        self.id.grid(row=5, column=1)
        self.nationality = Entry(root)
        self.nationality.grid(row=6, column=1)
        self.age = Entry(root)
        self.age.grid(row=10, column=1)
        self.location = Entry(root)
        self.location.grid(row=11, column=1)
        self.cite = Entry(root)
        self.cite.grid(row=12, column=1)
        self.count_1 = 0
        self.count_2 = 0
        self.count_3 = 0
        self.count_4 = 0
        self.count_5 = 0
        self.count_6 = 0
        self.count_7 = 0
        self.count_8 = 0
        self.count_9 = 0

    def storing(self):
        self.record_storage["clinic"].append(self.clinic.get())
        self.record_storage["first name"].append(self.fname.get())
        self.record_storage["last name"].append(self.lname.get())
        self.record_storage["gender"].append(self.gender.get())
        self.record_storage["ID"].append(self.id.get())
        self.record_storage["nationality"].append(self.nationality.get())
        self.record_storage["age"].append(self.age.get())
        self.record_storage["location"].append(self.location.get())
        self.record_storage["test cite"].append(self.cite.get())

        print(self.record_storage)
        self.count_1 = len(self.record_storage["clinic"])
        self.count_2 = len(self.record_storage["first name"])
        self.count_3 = len(self.record_storage["last name"])
        self.count_4 = len(self.record_storage["gender"])
        self.count_5 = len(self.record_storage["ID"])
        self.count_6 = len(self.record_storage["nationality"])
        self.count_7 = len(self.record_storage["age"])
        self.count_8 = len(self.record_storage["location"])
        self.count_9 = len(self.record_storage["test cite"])

        self.clinic.delete(0, END)
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.gender.delete(0, END)
        self.id.delete(0, END)
        self.nationality.delete(0, END)
        self.age.delete(0, END)
        self.location.delete(0, END)
        self.cite.delete(0, END)

    # def log(self):
        file = open("Storage.txt", "a")

        file.write(f"""
{self.count_1}                {self.record_storage["clinic"][self.count_1 -1]}              {self.record_storage["first name"][self.count_2 -1]}              {self.record_storage["last name"][self.count_3 -1]}               {self.record_storage["gender"][self.count_4 -1]}              {self.record_storage["ID"][self.count_5 -1]}              {self.record_storage["nationality"][self.count_6 -1]}             {self.record_storage["age"][self.count_7 -1]}             {self.record_storage["location"][self.count_8 -1]}                {self.record_storage["test cite"][self.count_9 -1]}""")


store = Storage()
button_add = Button(root, text="Submit", command=store.storing).grid(row=13, column=0)
# store.log()
root.mainloop()

