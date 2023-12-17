import tkinter as tk
from tkinter import messagebox


def validate_entry_content(entry_text):
    return bool(entry_text)


def on_login():
    username = entry_username.get()
    password = entry_password.get()
# validate username and password
    if username == 'admin' and password == '123':
        messagebox.showinfo('Login Successfull', 'Wellcome: ' + username+"!")
    else:
        messagebox.showerror("login failed", "invalid username or password")


root = tk.Tk()
root.geometry("500x350")
root.title("LOGIN SYSTEM")
root.configure(bg='lightblue')

validate_entry = root.register(validate_entry_content)
# create label,Entry widgate and Button
label_heading = tk.Label(root, text="EVANCE HEALTH ORGANIZATION SYSTEM", font=(
    'Times New Roman', 18), fg='blue', bg='lightblue')
label_heading.pack(pady=5)

# load image
image_path = 'C:/Users/Dommy/python/photo/logo.png'
img = tk.PhotoImage(file=image_path)

# customize the size of th photo
width_factor = 20
height_Factor = 20
resized_image = img.subsample(width_factor, height_Factor)

# create label to display the image
image_label = tk.Label(root, image=resized_image)
image_label.pack()


label_username = tk.Label(root, text="USERNAME: ", font=(
    'Times New Roman', 18), fg='black', bg='lightblue')
label_username.pack(pady=5)

entry_username = tk.Entry(root, width=25, font=('Aerial', 18), bg='lightyellow', fg='blue',
                          bd=1, relief=tk.SOLID, validate="focusout", validatecommand=(validate_entry, "%P"))
entry_username.pack(pady=5)

label_heading = tk.Label(root, text='')

label_password = tk.Label(root, text="PASSWORD: ", font=(
    'Times New Roman', 18), fg='black', bg='lightblue')
label_password.pack(pady=5)

entry_password = tk.Entry(root, width=25, font=('Aerial', 18), bg='lightyellow', fg='blue', bd='1', relief=tk.SOLID,
                          # use show to hide the password
                          show="*", validate="focusout", validatecommand=(validate_entry, "%P"))
entry_password.pack(pady=5)

label_create_account = tk.Label(root, text="If you don't have account click")

login_button = tk.Button(root, text="LOGIN", font=(
    'Times New Roman', 20), fg='blue', command=on_login)
login_button.pack(pady=10)


root.mainloop()