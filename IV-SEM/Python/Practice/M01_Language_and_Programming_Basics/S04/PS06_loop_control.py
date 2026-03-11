'''
Password retry system (max 3 attempts)
If password is correct show login successful
else ask for password 3 times
Once attempts exceed show locked
'''
password = "spoorthi06"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    input = str(input("Enter your password:"))
    if input == password:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")
        if attempts == max_attempts:
            print("Account locked due to too many failed attempts.")
"break and continue statements"