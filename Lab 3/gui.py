from tkinter import *
from tkinter import ttk
from random import randint
from PIL import ImageTk, Image
import paho.mqtt.client as mqtt
import numpy as np

pick_number = -1
user_choice_value_1 = 0

def print_screen (user_choice_value):
    print("me")
    print(user_choice_value)
    print("rival")
    print(pick_number)

    if user_choice_value == 0: # rock

        if pick_number == 0: # rock
            win_lose_label.config(text = "It's a tie! Pick again.")
        elif pick_number == 1: # paper
            win_lose_label.config(text = "Paper beats Rock. You lose! Pick again.")
        elif pick_number == 2: # scissors
            win_lose_label.config(text = "Rock beats Scissors. You win! Pick again.")

    elif user_choice_value == 1: # paper

        if pick_number == 0: #rock
            win_lose_label.config(text = "Paper beats Rock. You win! Pick again.")
        elif pick_number == 1: # paper
            win_lose_label.config(text = "It's a tie! Pick again.")
        elif pick_number == 2: # scissors
            win_lose_label.config(text = "Scissors beats Paper. You lose! Pick again.")

    elif user_choice_value == 2: # scissors

        if pick_number == 0: # rock
            win_lose_label.config(text = "Rock beats Scissors. You lose! Pick again.")
        elif pick_number == 1: # paper
            win_lose_label.config(text = "Scissors beats Paper. You win! Pick again.")
        elif pick_number == 2: # scissors
            win_lose_label.config(text = "It's a tie! Pick again.")

def on_connect(client, userdata, flags, rc):
  print("Connection returned result: " + str(rc))
  client.subscribe("ece180d/warren_rps", qos=1)


def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')

def on_message(client, userdata, message):
  if(message.topic == "ece180d/warren_rps"):
    print('Received message ' + str(message.payload) + ' on topic ' +
        message.topic + '" with QoS ' + str(message.qos))
    global pick_number
    pick_number = int(str(message.payload)[2:-1])
    print_screen(user_choice_value_1)


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async('mqtt.eclipseprojects.io')
client.loop_start()

print(pick_number)

root = Tk()
root.title('Rock, Paper, Scissors')
root.geometry("500x600")

root.config(bg="white")

# images
rock = ImageTk.PhotoImage(Image.open("rock.jpg"))
paper = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissors = ImageTk.PhotoImage(Image.open("scissors.jpg"))

# image list
image_list = [rock, paper, scissors]


# throw up an image when the program starts
image_label = Label(root, image=image_list[randint(0, 2)])
image_label.pack(pady=20)

#create spin function
def spin():

    if (pick_number == -1):
        win_lose_label.config(text = "Waiting for other player")

    # 0 = rock
    # 1 = paper
    # 2 = scissors
    global user_choice_value_1
    if user_choice.get() == "Rock":
        user_choice_value_1 = 0
    elif user_choice.get() == "Paper":
        user_choice_value_1 = 1
    elif user_choice.get() == "Scissors":
        user_choice_value_1 = 2
    win_lose_label.config(text = "Waiting for other player")
    print("i picked")
    print(user_choice_value_1)
    # show number
    image_label.config(image=image_list[user_choice_value_1])

    client.publish("ece180d/zeid_rps", user_choice_value_1, qos=1)

    print(pick_number)
    # determine if won or lost



# make choice
user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady = 20)

# create spin button
spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady = 10)

# label win lose
win_lose_label = Label(root, text = "Pick an option", font = ("Helvetica", 18), bg = "white")
win_lose_label.pack(pady = 10)

root.mainloop()

