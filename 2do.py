import tkinter as tk, win32gui, win32con, os

def add():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save()

def remove():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save()
    except IndexError:
        pass

def save():
    tasks = listbox.get(0, tk.END)
    folder = os.path.expanduser("~")
    taskfile = os.path.join(folder, "tasks.txt")
    with open(taskfile, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def dresizing(window):
    window.resizable(False, False)

def close():
    save(), root.destroy()

def length(new_value):
    return len(new_value) <= 75

root = tk.Tk()
win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="#343434")
listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="#343434", fg="white")
listbox.pack(pady=10, fill=tk.BOTH, expand=True)
input_label = tk.Label(root, text="Input:", bg="#343434", fg="white")
input_label.pack(pady=5)
length_func = root.register(length)
entry = tk.Entry(root, validate="key", validatecommand=(length_func, "%P"), bg="#343434", fg="white")
entry.pack(pady=5, padx=20, fill=tk.X)
button_frame = tk.Frame(root, bg="#343434")
button_frame.pack(pady=5)
add_button = tk.Button(button_frame, text="Add Task", command=add, bg="#343434", fg="white", activebackground="#343434")
add_button.pack(side=tk.LEFT)
remove_button = tk.Button(button_frame, text="Delete Task", command=remove, bg="#343434", fg="white", activebackground="#343434")
remove_button.pack(side=tk.RIGHT)

try:
    folder = os.path.expanduser("~")
    taskfile = os.path.join(folder, "tasks.txt")
    if os.path.exists(taskfile):
        with open(taskfile, "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())
except FileNotFoundError:
    pass

root.protocol("WM_DELETE_WINDOW", close)
dresizing(root)
root.mainloop()
