import time 
import cv2
from keras.models import load_model
import numpy as np
import random

global computer_chances
global user_chances 
computer_chances = 3
user_chances = 3


choices = ["rock", "paper", "scissors","nothing"]
model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def get_computer_choice():  #name functions with verb - i.e get, do - doing/ activity being carried out 
    computer_pick = random.choice(choices[0:3])
    return computer_pick

def get_predictions():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    start_time = time.time()
    while True:
        current_time = time.time()
        game_time = current_time - start_time
        print(game_time)
        if game_time > 5 and game_time <= 7:
           prediction = model.predict(data)

        elif game_time > 7 and game_time <=10:
            max_index = np.argmax(prediction[0])
            user_choice = choices[max_index]
            

        elif game_time > 10:
            computer_pick = get_computer_choice()
            users_input = user_choice
            get_winner(computer_pick, users_input)
            
            
            start_time = time.time()
            
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        if computer_chances == 0:
            print("User has won")
            break
        elif user_chances == 0:
            print("Computer won")
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



def get_winner(computer_pick, users_input):
    global computer_chances
    global user_chances 
    print(f"computer: {computer_pick}")
    print(f"user: {users_input}")

    if computer_pick == users_input:
        print(f"Tie")

    elif(computer_pick == 'rock' and users_input == 'scissors'):
        print(f"You lost! {computer_pick} won {users_input}")
        user_chances -= 1
        print(user_chances)

    elif (computer_pick == 'paper' and users_input == 'rock'):
        print(f"You lost! {computer_pick} won {users_input}") 
        user_chances -= 1
        print(user_chances)
    
    elif (computer_pick == 'scissors' and users_input == 'paper'):
        print(f"You lost! {computer_pick} won {users_input}") 
        user_chances -= 1
        print(user_chances)
        
    else: 
        print(f"User won! {users_input} you beat {computer_pick}")
        computer_chances -= 1
        print(computer_chances)
       
get_predictions()






