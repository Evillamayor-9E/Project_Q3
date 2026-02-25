from pyscript import display # pyright: ignore[reportMissingImports]
from js import document # pyright: ignore[reportMissingImports]

def Create(e):
    document.getElementById("output").innerHTML = ""
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    
   
    number = any(char.isdigit() for char in password)
    
   
    limit = len(password) > 12
    
    if not number:
        display("Password must contain at least one number", target="output")
    elif limit:
        display("Password cannot exceed 12 characters", target="output")
    else:
        display(f"You successfully made an account {username}", target="output")