import datetime, serial, sys, time
from threading import Thread
import numpy as np
import pandas as pd 

# Global variable, thread running
thread_running = True
user_input = "1"


def take_input():
    """ Function that will wait for a keyboard input then return it """
    global user_input
    while thread_running == True:
        user_input = input('Type user input: ')
        
    
if __name__ == "__main__":
    print("Hello world")
    # Read csv of sensor data
    try:
        print("Reading data...")
        df = pd.read_csv("pinch_data.csv")
    except: 
        print("Could not ready csv file... creating new one...")
        df = pd.DataFrame(columns=["S1_mean","S1_t1", "S1_t2", "S1_t3", "S1_t4",
                                   "S1_t5", "S1_t6", "S1_t7", "S1_t8", "S1_t9",
                                   "S1_t10",
                                   "S2_mean","S2_t1", "S2_t2", "S2_t3", "S2_t4",
                                   "S2_t5", "S2_t6", "S2_t7", "S2_t8", "S2_t9",
                                   "S2_t10", "Label", "Timestamp"])
        df.to_csv("pinch_data.csv", index=False)
        print("File created.")
    try:
        u_in = input("To record pinch data press 1, to record \'not pinch\' data press 0: ")
        if (u_in == "1"):
            print("Recording pinches, press enter to save or q to quit...")

            # Create threads to recieve user input
            input_thread = Thread(target=take_input)
            # Start the thread
            input_thread.start()
            # Print the variable infinitely
            
            time.sleep(1)
            
            ctr = 0
            while True:
                ctr += 0.001
                if user_input == "":
                    print(ctr)
                    user_input = "1"

            
    except KeyboardInterrupt:
        print ('Caught KeyboardInterrupt')
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        sys.exit()
        print("Program ended.")