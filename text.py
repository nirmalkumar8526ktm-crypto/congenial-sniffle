def get_user_info():
    """Get user's name and age"""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def print_greeting(name, age):
    """Print a greeting message"""
    print(f"Hello, {name}! You are {age} years old.")

def main():
    name, age = get_user_info()
    print_greeting(name, age)

if __name__ == "__main__":
    main()