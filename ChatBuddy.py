import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "I am": "you are",
    "I was": "you were",
    "I": "you",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

pairs = [
    [
        r"(?i)my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"(?i)hi|hey|hello|what is up|how is it going|what is new|how is life treating you|what is poppin|what is good|yo",
        ["Hello!", "Hey there!", "Hi, how can I assist you today?"]
    ],
    [
        r"(?i)what is your name ?",
        ["I am a bot named Chat Buddy."]
    ],
    [
        r"(?i)how are you ?",
        ["I'm doing as well as a chatbot can do. How about yourself?"]
    ],
    [
        r"(?i)sorry (.*)",
        ["It's alright", "It's OK, never mind."]
    ],
    [
        r"(?i)i am fine",
        ["Great to hear that! How can I assist you?"]
    ],
    [
        r"(?i)exit|bye",
        ["Goodbye!", "It was nice talking to you. Have a great day!"]
    ]
]

# Add a list of additional responses for retrieval-based approach
additional_responses = [
    "I'm sorry, but I'm not sure I understand. Can you please rephrase your question?",
    "That's an interesting question. Let me find the information for you.",
    "I don't have the answer to that at the moment. Is there anything else I can help you with?"
]

def retrieve_response(input_text):
    # Implement the retrieval logic here
    # You can use TF-IDF, word embeddings, or any other matching mechanism
    # to retrieve the most appropriate response based on the input text
    
    # For demonstration purposes, we'll simply return a random additional response
    import random
    return random.choice(additional_responses)

def chatbot():
    print("Hello there. I am a chatbot built to carry on a conversation based on a variety of human inputs. How are you doing?")
    chat = Chat(pairs, reflections)
    chat._respond = retrieve_response  # Override the default _respond method with the retrieval-based approach
    chat.converse()

if __name__ == "__main__":
    chatbot()

