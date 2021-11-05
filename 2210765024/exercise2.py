a=input("Please enter your email: ")
if "@" and "." in a.strip():
    print("Valid email.")
else:
    print("Email is not valid.")