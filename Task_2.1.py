
user_name = None
print("Chatbot: Hi! I'm your Python Chatbot. Type 'exit' to quit.")

while True:
    if user_name is None:
        user_name = input("Chatbot: What's your name?\nYou: ").strip()
        print(f"Chatbot: Nice to meet you, {user_name}!")
        continue


    print("Chatbot: Do you want to do addition (+) or subtraction (-) or end operation (exit)?")
    choice = input("You: ").strip().lower()

    if choice in ["exit"]:
        print("Chatbot: Goodbye! Have a nice day.")
        break

    if choice in ["+", "addition", "-", "subtraction"]:
        nums = input("Chatbot: Enter two numbers separated by a space:\nYou: ").strip().split()

        if len(nums) == 2 and nums[0].isdigit() and nums[1].isdigit():
            num1, num2 = int(nums[0]), int(nums[1])

            if choice in ["+", "addition"]:
                print(f"Chatbot: The result is {num1 + num2}")
            else:
                print(f"Chatbot: The result is {num1 - num2}")
        else:
            print("Chatbot: Please enter exactly two valid numbers.")
    else:
        print("Chatbot: Please choose '+' for addition or '-' for subtraction.")
