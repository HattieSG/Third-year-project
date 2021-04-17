import datetime, serial, sys, time
from threading import Thread
import numpy as np
import pandas as pd 

# Global variable, thread running
thread_running = True
user_input = ""


def take_input():
    """ Function that will wait for a keyboard input then return it """
    global user_input
    while thread_running == True:
        user_input = input('Type user input: ')
         
    
if __name__ == "__main__":
    print("Hello world")
    # Attempt to connect to the port with the arduino & sensors
    try:
        print("Connecting to board 1...")
        ser = serial.Serial('COM7', 57600)
    # If there is a failure to connect end the program
    except:
        print("Failed to connect")
        sys.exit()
        
    # Read csv of sensor data
    try:
        print("Connected!")
        print("Reading data...")
        df = pd.read_csv("pinch_data.csv")
        for col in df.columns:
            if "Unnamed" in col:
                df=df.drop(col, axis=1)
    # If no csv exists create a new empty csv
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
        print("Data loaded!")

        # Create threads to recieve user input
        input_thread = Thread(target=take_input)
        # Start the thread
        input_thread.start()
        time.sleep(1)
        
        
        # Initialise lists to store the last 10 values from each of the sensors
        sensors = np.asarray([np.asarray([255]*10)]*2)
        
        while True:
            # Read the raw data from the sensor
            hello = ser.readline()
            # Decode the message
            decoded = (hello.decode("utf-8"))
            # Split the message by underscoreses to extract the reading from each sensor
            sensor_readings = decoded[:-1].split("_") # Remove the last character ("\n")
            # Iterate through all sensor readings and save
            for j in range(0,len(sensor_readings)):
                # Append the current value to the appropriate array, and remove the last value
                sensors[j] = np.append(np.delete(sensors[j], 0), sensor_readings[j])
            
            # If the user input is one save the data as a grasp
            if user_input == "1":
                print("Grasp!")
                # Create the row of values for the csv
                row = ([np.mean(sensors[0,:])] + sensors[0,:].tolist() + 
                       [np.mean(sensors[1,:])] + sensors[1,:].tolist() + 
                       [user_input] + [str(datetime.datetime.now())])
                print(row)
                # Append the values to the csv
                df = df.append(pd.Series(row, index = df.columns),
                               ignore_index=True)
                # Reset the user input
                user_input = ""
            # If the user input is two save the data as fail grasp
            if user_input =="0":
                print("Fail grasp!")
                # Create the row of values for the csv
                row = ([np.mean(sensors[0,:])] + sensors[0,:].tolist() + 
                       [np.mean(sensors[1,:])] + sensors[1,:].tolist() + 
                       [user_input] + [str(datetime.datetime.now())])
                print(row)
                # Append the values to the csv
                df = df.append(pd.Series(row, index = df.columns),
                               ignore_index=True)
                # Reset the user input
                user_input = ""
                    
    except KeyboardInterrupt:
        print ('Caught KeyboardInterrupt')
        
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        print("Program ended.")
        print("Please restart the terminal.")
        df.to_csv("pinch_data.csv")
        ser.close()
        sys.exit()
        