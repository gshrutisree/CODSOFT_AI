def chatbot(user):
    user = user.lower()
    response = {
        "hi": "Hello! How can I assist you today?",
        "how are you": "I'm fine thankyou, how are you?",
        "bye": "Bye bye! Have a great day!",
        "default": "Sorry, I didn't understand that. Can you try again?"
    }

    for i, j in response.items():
        if i in user:
            return j
    return response["default"]

print("Bot: Hello! How can I assist you today?")
while True:
    user = input("You: ")
    bot = chatbot(user)
    print("Bot:", bot)
    if user.lower() == "bye":
        break
