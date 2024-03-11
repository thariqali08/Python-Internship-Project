import nltk
from nltk.chat.util import Chat


#download nltk data
nltk.download('punkt')


#response between person and chatbot
responses = [
   
    [
        "hi",["Hello,How are you?"]
    ],
    [
        "i am good.what about you", ["I am doing well,thank you"]
    ],
    [
       "what is your name", ["I am ChatBot"]
    ],
    [
         "what can you do", [ "I am assist you"]
    ],
    [
       "that's great", [ "Thank you..."]
    ],
    [
          "what is your favorite colour",[ "Sorry,As a chatbot.I dont have personal preference"]
    ],
    [
        "what is the capital of india?", ["The capital of India is New Delhi"]
    ],
    [ 
        "thankyou for your help",[ "your are welcome!"]
    ],
    
    [ 
        "bye",["Bye.Take care!"]
    ]

]



def chatbot():
    chat = Chat(responses)
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot:",chat.respond(user_input))
            break
        print("ChatBot:",chat.respond(user_input))

# Run the chatbot
chatbot()