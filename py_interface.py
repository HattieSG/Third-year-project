import pickle
import serial
import sklearn
import sys
import numpy as np

if __name__ == "__main__":
    print("Hello world")

    # Attempt to connect to the port with the arduino & sensors
    try:
        print("Connecting to board 1...")
        ser = serial.Serial('COM5', 57600)
        print("Connecting to board 2...")
        ser2 = serial.Serial('COM3', 9600)        
    # If there is a failure to connect end the program
    except:
        print("Failed to connect")
        sys.exit()
        
    # Load the machine learning model of choice
    try:
        print("Loading machine learning model...")
        model = pickle.load(open("logistic_regression", 'rb'))
        #model = pickle.load(open("svm", 'rb'))
        #model = pickle.load(open("random_forest", 'rb'))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit()
        

    # Run the code until ctrl+c is pressed then close the connection
    try:
        # Initialise lists to store the last 10 values from each of the sensors
        sensors = np.asarray([np.asarray([255]*10)]*2)
        
        # Initialise a counter to determine number of grasp predictions in a row
        grasp_ctr = 0
        
        # Run an infinite loop
        while True:
            # Read the raw data from the sensor
            hello = ser.readline()
            # Decode the message
            decoded = (hello.decode("utf-8"))
            # Split the message by underscoreses to extract the reading from each sensor
            sensor_readings = decoded[:-1].split("_") # Remove the last character ("\n")
            # Iterate through all sensor readings recieved and save to appropriate array
            for j in range(0,len(sensor_readings)):
                # Append the current value to the appropriate array, and remove the oldest value
                sensors[j] = np.append(np.delete(sensors[j], 0), sensor_readings[j])
            
            # Create a array of sensor values to pass into the model
            X = np.concatenate((sensors[0,:], sensors[1,:]), axis=None)
            # Query the model using the sensor values
            pred = model.predict(X.reshape(1,-1)) # Reshape array as only one sample
            # Write the model output to the board      
            print(pred[0])
            # Check if the grasp is 0, if it is reset the counter
            if pred[0] == 0:
                grasp_ctr = 0
            # If it is not zero increase the value by one
            elif pred[0] == 1:
                grasp_ctr += 1
            # Once 5 grasps have been predicted in a row send the command to the hand to stop moving
            if grasp_ctr == 5:
                ser2.write(str(1).encode())
                grasp_ctr = 0
            
    # When ctrl+c is pressed close the port
    except KeyboardInterrupt:
        print ('Caught KeyboardInterrupt')
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        ser.close()
        ser2.close()