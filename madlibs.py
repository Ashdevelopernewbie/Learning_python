# string concatenation (aka how to put strings together) 
# youtube_channel = input ("What is the name of your youtube channel: ")
# print("Subscribe to " + youtube_channel) #first way to concat
# print("Subscribe to {}".format(youtube_channel)) #second way to concat
# print(f"Subscribe to {youtube_channel}") #third way to concat

adj = input("Adjective: ")
verb1 = input("First verb: ")
verb2 = input("Second verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)