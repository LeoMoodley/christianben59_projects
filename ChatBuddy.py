import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",],
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",],
    ],
    [
        r"what is your name ?",
        ["I am a bot created by you. You can call me whatever you like.",],
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You ?",],
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",],
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",],
    ],
]

def chatbot():
    print("Hi, I'm the chatbot you built")

chat = Chat(pairs, reflections)
chat.converse()

if __name__ == "__main__":
    chatbot()
