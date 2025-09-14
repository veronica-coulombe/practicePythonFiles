print("Welcome to the mini story game!")

chooseCharacter = input("Please choose your character: Fred or Kay ")

if chooseCharacter == "Fred":
    print("Your character is Fred")
elif chooseCharacter == "Kay":
    print("Your character is Kay")
else:
    print("Please choose Fred or Kay. (Use caps for first letter)")
    exit()

charOne = "Fred"
charTwo = "Kay"

if chooseCharacter == charOne:
    print(f"{charOne} is going to a bakery to get a cake.")
    cake = input(f"Choose a cake for {charOne}: vanilla or chocolate ")
    if cake == "vanilla":
        print(f"Nice! {charOne} bought a vanilla cake!")
    elif cake == "chocolate":
        print(f"Cool! {charOne} bought a chocolate cake!")
elif chooseCharacter == charTwo:
    print(f"{charTwo} is going to a cat cafe.")
    cat = input(f"Choose a cat for {charTwo} to pet: fluffy or shorthair ")
    if cat == "fluffy":
        print("This cat is very fluffy!")
    elif cat == "shorthair":
        print("This cat is very smooth!")

print("Thank you for playing the mini story game!")