from customtkinter import *
from PIL import Image
import mysql.connector
import subprocess

db = mysql.connector.connect(
    host="localhost",
    port=9999,
    user="your_username",
    password="your_password",
    database="your_database_name"
)


app = CTk()
app.geometry("600x480")
app.resizable(0, 0)

side_img_data = Image.open("side-.png")
email_icon_data = Image.open("email-icon.png")
password_icon_data = Image.open("password-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome!", text_color="#5766F9", anchor="w", justify="left",
         font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Login ke akunmu...", text_color="#7E7E7E", anchor="w", justify="left",
         font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Email:", text_color="#5766F9", anchor="w", justify="left",
         font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
email_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#5766F9", border_width=1,
                       text_color="#000000")
email_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#5766F9", anchor="w", justify="left",
         font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#5766F9", border_width=1,
                          text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

status_label = CTkLabel(master=frame, text="", text_color="#FF0000", anchor="w", justify="left",
                        font=("Arial Bold", 12))
status_label.pack(anchor="w", padx=(25, 0))


def login():
    # Retrieve login credentials
    email = email_entry.get()
    password = password_entry.get()

    # Construct SQL query to fetch user record
    query = "SELECT * FROM users WHERE email = %s"
    cursor = db.cursor()
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user is not None:
        # Compare passwords
        stored_password = user[2]  # Assuming password is stored at index 2 in the user record
        if password == stored_password:
            # Login successful
            status_label.configure(text="Login successful!", text_color="#00FF00")
            app.destroy()
            subprocess.run(["python", "guitest.py"])  # Run guitest.py using subprocess
        else:
            # Invalid password
            status_label.configure(text="Invalid password!", text_color="#FF0000")
    else:
        # User not found
        status_label.configure(text="User not found!", text_color="#FF0000")


CTkButton(master=frame, text="Login", fg_color="#5766F9", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225, command=login).pack(anchor="w", pady=(40, 0), padx=(25, 0))

app.mainloop()