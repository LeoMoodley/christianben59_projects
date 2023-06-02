#Allows for natural language processing and pattern recognition
import nltk
from nltk.chat.util import Chat, reflections

#A list of patterns and there corresponding responses stored in a list
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
#Function takes the pairs and responds based on its knowledge of the inputs
def chatbot():
    print("Hi, I'm the chatbot you built")

chat = Chat(pairs, reflections)
chat.converse()
#initializes the program
if __name__ == "__main__":
    chatbot()
