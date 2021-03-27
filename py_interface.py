import serial, sys
import numpy as np

if __name__ == "__main__":
    print("Hello world")

    # Attempt to connect to the port with the arduino & sensors
    try:
        print("Connecting to board 1...")
        ser = serial.Serial('COM5', 57600)
        # print("Connecting to board 2...")
        # ser2 = serial.Serial('COM6', 57600)
    # If there is a failure to connect end the program
    except:
        print("Failed to connect")
        sys.exit()

    # Run the code until ctrl+c is pressed then close the connection
    try:
        # Initialise lists to store the last 10 values from each of the sensors
        sensor1 = np.asarray([255]*10)
        sensor2 = np.asarray([255]*10)
        
        # Run an infinite loop
        while True:
            # Iterate a counter in cycles of 10 to store output values for the last second
            for i in range(0,10):
                # Read the raw data from the sensor
                hello = ser.readline()
                # Decode the message
                decoded = (hello.decode("utf-8"))
                # Split the message by underscoreses to extract the reading from each sensor
                sensor_readings = decoded[:-1].split("_") # Remove the last character ("\n")
                # Append the sensor readings to the list for each sensor
                sensor1[i] = float(sensor_readings[0])
                sensor2[i] = float(sensor_readings[1])
                #print(f"Sensor1: {sensor1}")
                #print(f"Sensor2: {sensor2}")
                
                # If either sensor is experiencing pressure print to the console!
                if (np.mean(sensor1) > 265 and np.mean(sensor2) > 265):
                    print("Both sensors are on!")
                elif (np.mean(sensor1) > 265):
                    print("Sensor1 on!")
                elif (np.mean(sensor2) > 265):
                    print("Sensor2 on!")
                else:
                    print("...")
                    
                    #ser2.write(str(2).encode())
                    #ser2.write(str(1).encode())
                    #ser2.write(str(3).encode())
    # When ctrl+c is pressed close the port
    except KeyboardInterrupt:
        print ('Caught KeyboardInterrupt')
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        ser.close()
        # ser2.close()