# PYTHON-LOGIN-GUI-CTK
![readme](https://github.com/OJJJN/PYTHON-LOGIN-GUI-CTK/assets/99503707/9c9b071d-b1de-45a1-87ac-a3f23478299c)

# PYTHON LOGIN GUI CTK
The provided code is a simple Python script that creates a login GUI using the customtkinter library. The GUI consists of a window with a side image and a login form on the right side.

The login form includes input fields for email and password, along with corresponding icons. Users can enter their email and password in the respective fields. A login button is also provided.

Upon clicking the login button, the script validates the entered credentials by querying a MySQL database. If the entered email and password match a record in the database, a success message is displayed, and the application window is closed. Additionally, it runs another Python script named "guitest.py" using the subprocess module.

If the login credentials are invalid or the user is not found in the database, an appropriate error message is displayed.

Overall, this script provides a basic login interface using customtkinter and allows users to authenticate themselves by checking their credentials against a MySQL database.

## Requirements
- Python
- MYSQL
- customtkinter libraries
- Pillow libraries
- mysql-connector-python libraries

## Installation
- Install python 3.7
- Make your database on MYSQL
- Clone This Repository
- pip install -r requirements.txt
- Run py cpstart.py

