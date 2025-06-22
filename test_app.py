from app import CareerChatbotApp

app = CareerChatbotApp()
print("App initialized successfully!")
print("Testing responses:")
print("Q: I love chemistry and math")
print("A:", app.generate_response("I love chemistry and math"))
print("Q: Can I do law if I'm not good at math?")
print("A:", app.generate_response("Can I do law if I'm not good at math?"))