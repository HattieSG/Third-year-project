import serial, sys
import numpy as np

if __name__ == "__main__":
    print("Hello world")

    # Attempt to connect to the port with the arduino & sensors
    try:
        print("Connecting to board 1...")
        ser = serial.Serial('COM5', 57600)
        print("Connecting to board 2...")
        ser2 = serial.Serial('COM6', 57600)
        
    # If there is a failure to connect end the program
    except:
        print("Failed to connect")
        sys.exit()

    # Run the code until ctrl+c is pressed then close the connection
    try:
        print("Connected!")
        # Initialise lists to store the last 10 values from each of the sensors
        sensors = np.asarray([np.asarray([255]*10)]*4)
        
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
                # Iterate through all sensor readings
                for j in range(0,len(sensor_readings)):
                    sensors[j,i] = sensor_readings[j]
                # Create a counter to count the number of sensors that are on
                on_ctr = 0
                # Iterate throug each sensor
                for i in range(0,4):
                    # If the average for the past second of readings is great than 290, count sensor as on
                    if np.mean(sensors[i,:]) > 275:
                        # Iterate count of on sensors
                        on_ctr+=1
                # Write to the arduino the number of sensors under pressure
                ser2.write(str(on_ctr).encode())
                print(on_ctr)
                print(ser2.readline())
                
    # When ctrl+c is pressed close the port
    except KeyboardInterrupt:
        print ('Caught KeyboardInterrupt')
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        ser.close()
        ser2.close()