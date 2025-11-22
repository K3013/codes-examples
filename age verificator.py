age = input("Please enter your age: ")
age = int(age)
if age < 13:
    message = "Hey, you cannot login to the website : You are under 13 years old."
    print(message)
elif age < 18:
    email = input("Please enter your parent's email address: ")
    if "@" not in email or "." not in email:
        message = "Invalid email address. Please restart the process."
        print(message)
        input("Press Enter to exit...")
        exit()
    message = f"Hey, you need parental consent. A confirmation email will be sent to {email}."
    print(message)
    input("enter the code sent to your parent's email: ")
    if True:  # Simulating successful code entry
        message = "Parental consent verified. You can now login." 
        print(message)
else:
    email = input("Please enter your email address: ")
    if "@" not in email or "." not in email:
        message = "Invalid email address. Please restart the process."
        print(message)
        input("Press Enter to exit...")
        exit()
    message = f"Welcome! A confirmation email will be sent to {email}."
    print(message)
    input("enter the code sent to your email: ")
    if True:  # Simulating successful code entry
        message = "Email verified. You can now login."
        print(message)

input("Press Enter to exit...")