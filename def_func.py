def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

while True:
    print("\nAttempt all the Questions")
    print("Key in the character 'q' if you are feeling to quit the process.")
    fname = input("First name: ")
    if fname == 'q':
        break

    lname = input("Last name: ")
    if lname == 'q':
        break

    full_name = formatted_name(fname, lname)
    print(f"Congratulation {full_name.title()}, you have been successfully been registered, give space for the nest person.")