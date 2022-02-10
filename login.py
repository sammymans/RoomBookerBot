
login_file = open("login.txt", "r")

user = login_file.readline()
password = login_file.readline()

login_file.close()

response = int(input("Is this the correct username and password (1 - yes, 0 - no)? \n" + "User: " + user + "Password: " + password + "\n"))

if response == 0:
    login_file = open("login.txt", "w")

    user = input("New Username: ")
    login_file.write(user)
    login_file.write("\n")

    password = input("New Password: ")
    login_file.write(password)

    print("Information Saved")



