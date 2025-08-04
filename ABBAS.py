def chatbot():
    print("Simple Chatbot started. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye!")
            break
        elif 'hello' in user_input:
            print("Chatbot: Hi there!")
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing well, thank you for asking.")
        elif 'name' in user_input:
            print("Chatbot: I am a simple chatbot.")
        else:
            print("Chatbot: I don't understand that yet.")

if _name__ == "_main_":
    chatbot()