def greet_users(names):
    """"Print a simple greeting text to the users via the help of the for loop"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'peter']
greet_users(usernames)

