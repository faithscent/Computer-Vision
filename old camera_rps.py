
import time 
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
starttime = time.time()
def get_prediction(prediction):
    rock = prediction[0][0]
    paper = prediction[0][1]
    scissor =prediction[0][2]
    nothing = prediction[0][3]
    if rock > paper and rock > scissor and rock > nothing:
        print("rock is greater")
    elif paper > rock and paper > scissor and paper > nothing:
        print("paper is greater")
    elif scissor > rock and scissor > paper and scissor > nothing:
        print("scissor is greater")
    else:
        print("nothing is greater")


 

while True: 
    current_time =time.time()
    game_time = current_time - starttime
    if game_time >= 5:
        print(f' winner is{prediction}')
    else:
        get_prediction(prediction) 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)

    get_prediction(prediction) 
   
    if cv2.waitKey(1) & 0xFF == ord('q'): #wait upto 1 millesec till you do something
        break
    
       
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

# give 5 secs to get prediction, after 5 less than 5 - diSPLAY WINNER after 5 secs show winner and then restart game 
#initialize start time, create a loop that runs indefinetly 
#intialize current time 
#if lapsed time is greater than this, if reaches this do this - use a while loop 



    





    
    



