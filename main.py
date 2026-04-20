import tkinter as tk
from tkinter import messagebox
from register import register_student
from train import train_model
from attendance import take_attendance

def register():
    name = name_entry.get()
    student_id = id_entry.get()

    if not name or not student_id:
        messagebox.showerror("Error", "Enter Name and ID")
        return

    register_student(name, student_id)
    messagebox.showinfo("Success", "Student Registered!")

def train():
    train_model()
    messagebox.showinfo("Success", "Model Trained!")

def attendance():
    take_attendance()

root = tk.Tk()
root.title("Face Attendance System")
root.geometry("400x300")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Button(root, text="Register Student", command=register).pack(pady=10)
tk.Button(root, text="Train Model", command=train).pack(pady=10)
tk.Button(root, text="Take Attendance", command=attendance).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()