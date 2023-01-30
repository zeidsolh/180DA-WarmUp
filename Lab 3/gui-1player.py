from tkinter import *
from tkinter import ttk
from random import randint
from PIL import ImageTk, Image


def print_screen (user_choice_value, pick_number):
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
pick_number = randint(0, 2)


# throw up an image when the program starts
image_label = Label(root, image=image_list[randint(0, 2)])
image_label.pack(pady=20)

#create spin function
def spin():
    pick_number = randint(0, 2)
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2
    print_screen(user_choice_value, pick_number)
    image_label.config(image=image_list[pick_number])



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

