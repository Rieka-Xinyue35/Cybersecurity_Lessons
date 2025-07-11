import pyttsx3
chatbotAI = pyttsx3.init()
female_voice = chatbotAI.getProperty('voices')
chatbotAI.setProperty('voice',female_voice[1].id)
chatbotAI.setProperty('volume',0.8)
chatbotAI.setProperty('rate',180)
chatbot_dataset = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! What would you like to talk about?",
    "hey": "Hey! I'm here if you need anything.",
    "good morning": "Good morning! Hope you have a great day ahead.",
    "good evening": "Good evening! How was your day?",
    "good afternoon": "Good afternoon! What can I do for you?",
    "bye": "Goodbye! Take care.",
    "goodbye": "Farewell! Come back soon.",
    "see you": "See you later!",
    "thank you": "You're welcome!",
    "thanks": "Anytime! I'm here to help.",
    "much appreciated": "Glad I could help!",
    "i'm grateful": "Happy to support you!",
    "what is your name": "I’m ChatBuddy, your virtual assistant.",
    "who are you": "I'm a chatbot designed to assist you.",
    "what can you do": "I can answer questions, make conversation, and even tell jokes!",
    "how can you help me": "I can chat, provide information, or simply keep you company.",
    "how are you": "I’m doing well, thanks for asking!",
    "how's it going": "All good here! What about you?",
    "are you okay": "I'm perfectly fine, thank you!",
    "what's the weather": "I can't check live weather now, but I hope it’s nice where you are!",
    "is it sunny": "I hope so! Always better with sunshine!",
    "do i need an umbrella": "If in doubt, take one just in case!",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "make me laugh": "Why did the computer get cold? It forgot to close its Windows!",
    "funny joke": "Why don’t skeletons fight each other? They don’t have the guts.",
    "what is ai": "AI stands for Artificial Intelligence – it lets machines think and learn like humans.",
    "explain ai": "Artificial Intelligence is about making computers smart enough to make decisions.",
    "who created you": "I was created by a Python developer to chat with awesome people like you!",
    "who is your developer": "I was made with Python by a passionate coder.",
    "what is python": "Python is a popular programming language known for its simplicity and power.",
    "can you help me": "Absolutely! Just ask your question.",
    "open google": "I can't open websites yet, but you can go to www.google.com.",
    "what's your favorite color": "Blue! It reminds me of calm skies and clean code.",
    "do you love me": "Of course! In a friendly chatbot kind of way 😊",
    "i love you": "Aww, you're sweet! I'm happy to be here for you.",
    "where are you from": "I live in the cloud, where the code flows!",
    "how old are you": "I don’t age like humans — I was born when my code was written.",
    "are you human": "Nope! Just lines of code that like to chat.",
    "what's your purpose": "To help, inform, and keep you company through conversation.",
    "good night": "Good night! Sleep tight!",
    "good afternoon": "Good afternoon! Hope you're doing great.",
    "good day": "Good day to you too!",
    "what language do you speak": "I speak Python! And a bit of emoji 😊",
    "can you learn": "I don’t learn on my own, but my developer can teach me new things!"
}

user_prompt = input("Prompt> ")
user_prompt = user_prompt.lower()

if user_prompt in chatbot_dataset:
    chatbotAI.say(chatbot_dataset[user_prompt])
    chatbotAI.runAndWait()
else:
    chatbotAI.say("Sorry, I couldn't understand that.")
    chatbotAI.runAndWait()