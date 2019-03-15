#Imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import random
from time import sleep

# Used for getting random names
firstNameList = ["Masichuvio", "Vipponah", "Aranck", "Micco", "Tooantuh", "Hinto", "Kimama", "Tula", "Takchawee"]

# Used for getting random responses
responseList = ["Hello, how are you?", "I'm doing good. There are a lot of things to fix in our village.",
                "I'm trying to improve the camp a bit. Do you think you can help out?",
                "Sure, I will gather all of my sons and we will try our best to help out.",
                "The oceans are bringing in big tides today.", "We should set up barriers.",
                "I agree, let's get started on that.", "Are there any huts that need to be fixed?",
                "My house is a bit worn down from the years of it being ran over by wind and the rain.",
                "Greetings.",
                "Hi there.", "How is your family?", "I love my family.", "Me too.",
                "Great! All of the kids are finally growing up", "I was wondering if you have any left overs.",
                "You can grab from my hut and I'll give you some more when we're stocked."]
civilianList = []  # List of civilians


# Class for a person
class Person:

    # Init Method that takes a name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Custom print override
    def __str__(self):
        return "Type: {} [Name: {} | Age: {}]".format(self.__class__.__name__, self.name, self.age)


# Class for a leader
class Leader(Person):

    # Init method that takes a name
    def __init__(self, first,age):
        super().__init__(first,age)

    # Creates amount of bots
    def CreateBots(self, amount):

        # Iterate through the range
        for i in range(amount):
            newBot = Civilian(random.choice(firstNameList), 20)  # Create a new bot

            # Add the bot to the list
            civilianList.append(newBot)


# Class called civilian
class Civilian(Person):

    # Init method
    def __init__(self, first,age):
        super().__init__(first, age)


# Initiate conversation with leader and civilian

leader = Leader(input("Enter a name for the leader:"), 20)  # Create a new leader
bot = ChatBot(leader.name)  # Create a new bot from the leader

bot.storage.drop()  # Remove all of the original training data

trainer = ListTrainer(bot)  # Create a new trainer


# Training data
trainer.train(["Hello, how are you?", "I'm doing good. There are a lot of things to fix in our village."])
trainer.train(["I'm trying to improve the camp a bit. Do you think you can help out?",
               "Sure, I will gather all of my sons and we will try our best to help out."])
trainer.train(["The oceans are bringing in big tides today.", "We should set up barriers.",
               "I agree, let's get started on that."])
trainer.train(["Are there any huts that need to be fixed?",
               "My house is a bit worn down from the years of it being ran over by wind and the rain."])
trainer.train(["Greetings.", "Hi there.", "How is your family?", "Great! All of the kids are finally growing up"])
trainer.train(["I was wondering if you have any left overs.",
               "You can grab from my hut and I'll give you some more when we're stocked."])
trainer.train(["I love my family.", "Me too."])
trainer.train(["John 3:16"])

# Create bots
leader.CreateBots(int(input("How many bots do you want to make: ")))


# Main loop
while True:
    number = random.randint(0, 1)  # Random choice
    conversationLength = random.randint(2, 4)  # Chose a random length for the conversation

    print("New conversation:")
    # If we have 0, The civilian starts the conversation
    if number is 0:

        for i in range(conversationLength):
            # The civilian starts the conversation
            civilian = random.choice(civilianList)  # Create a civilian
            civilianText = random.choice(responseList)  # Get some random text
            print("{}({}) says: ".format(civilian.name, civilian.__class__.__name__) + civilianText)
            response = bot.get_response(civilianText)   # Have the leader respond
            print("{} says: {} ".format(leader.name, response))
            sleep(2)


# If we get 1, the leader starts the conversation
    if number is 1:
        for i in range(conversationLength):
            civilian = random.choice(civilianList)  # Create a random civilian
            bot = ChatBot(civilian.name)  # Create a chatbot from the civilian
            leaderText = random.choice(responseList)  # Get random text
            print("{} says: {} ".format(leader.name, leaderText))
            bot.get_response(leaderText)  # Have the civilian respond
            print("{}({}) says: ".format(civilian.name, civilian.__class__.__name__) + leaderText)
            sleep(2)
    print("_______________________________")
    print("")


