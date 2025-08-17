# WAP which takes a list of names as argument and greet "Hello" to everyone

def greet_names(names):
    for name in names:
        print("Hello", name)

names = ["Alice", "Bob", "Charlie"]
greet_names(names)