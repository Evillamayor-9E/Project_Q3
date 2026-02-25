from pyscript import document, display  # pyright: ignore[reportMissingImports]

def checkRegistration(e):
    document.getElementById("result").innerHTML = ""
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    if registration == "yes" and clearance == "yes" and grade in ["7", "8", "9", "10"]:
        eligible = "Yes"
    else:
        eligible = "You are not eligible for registration."

    eligibility = eligible

    if eligibility == "Yes" and section in ["topaz"]:
        team="Red Team"
    elif eligibility == "Yes" and section in ["ruby"]:
        team="Blue Team"
    elif eligibility == "Yes" and section in ["sapphire"]:
        team="Green Team"
    elif eligibility == "Yes" and section in ["emerald"]:
        team="Yellow Team"
    elif eligibility == "You are not eligible for registration.":
        team="none"

    if team == "Red Team":
        display(f'You are.. Red Bulldogs', target='result')

    elif team == "Blue Team":
        display(f'You are.. Blue bears', target='result')

    elif team == "Green Team":
        display(f'You are.. Green hornets', target='result')

    elif team == "Yellow Team":
        display(f'You are.. Yellow Tigers', target='result')
        
    elif team == "none":
        display(f'Sorry, but you are not registered.', target='result')