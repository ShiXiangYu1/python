def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    # reading a name
    print(f"What a great name you have, {input()}!")


# Now we can use these functions
greet("Aid", 2023)
remind_name()
