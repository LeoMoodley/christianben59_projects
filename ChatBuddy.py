import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(?i)my name is (.*)",
        ["Hello %1, How are you today ?",],
    ],
    [
        r"(?i)hi|hey|hello",
        ["Hello", "Hey there",],
    ],
    [
        r"(?i)what is your name ?",
        ["I am a bot created by you. You can call me whatever you like.",],
    ],
    [
        r"(?i)how are you ?",
        ["I'm doing good. How about You ?",],
    ],
    [
        r"(?i)sorry (.*)",
        ["Its alright", "Its OK, never mind",],
    ],
    [
        r"(?i)i am fine",
        ["Great to hear that, How can I help you?",],
    ],
]

def chatbot():
    print("Hello there. I am a chatbot built to carry on a conversation based off a variety of human inputs. How are you doing?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot() 
