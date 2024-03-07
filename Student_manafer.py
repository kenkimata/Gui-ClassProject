from tkinter import *

class Student():

    def __init__(self, name):
        self.name =  "John"

    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade

def show_grade(event):
    current_cursor = students_listbox.cursorselection()
    current_student = current_cursor[0]
    grade_label.config(text=csc_2[0].get_grade())


csc_2 = []

csc_2.append(Student("Bob"))
csc_2[0].set_grade("Achived")
csc_2.append(Student("John"))
csc_2[1].set_grade("Merit")
csc_2.append(Student("Jacob"))
csc_2[2].set_grade("Excellence")
csc_2.append(Student("Boaz"))
csc_2[3].set_grade("Not Achived")

window = Tk()
window.geometry("300x300")

students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0, "Bob")
students_listbox.insert(1, "John")
students_listbox.insert(2, "Jacob")
students_listbox.insert(3, "Boaz")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()


window.mainloop()