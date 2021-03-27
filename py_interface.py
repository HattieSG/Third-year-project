import serial
import numpy as np

if __name__ == "__main__":
    print("Hello world")

    # Attempt to connect to the port with the arduino & sensors
    try:
        ser = serial.Serial('COM5', 57600)
        ser2 = serial.Serial('COM7', 57600)
    # If there is a failure to connect end the program
    except:
        print("Failed to connect")
        exit()

    # Run the code until ctrl+c is pressed then close the connection
    try:
        signal = np.asarray([255]*10)
        # Run an infinite loop
        while True:
            # Iterate a counter in cycles of 10 to store output values for the last second
            for i in range(0,10):
                # Read the raw data from the sensor
                hello = ser.readline()
                # Decode the data and exclude the last character (\n) and store in signal
                signal[i] = float(hello[0:len(hello)-1].decode("utf-8"))   
                print(signal)

                # If the average signal value is low, send red led signal
                if (np.mean(signal) < 150):
                    ser2.write(str(1).encode())
                # If the average signal value is medium, send yellow led signal
                elif (np.mean(signal) < 220):
                    ser2.write(str(2).encode())
                # Otherwise the average signal value is high, send green led signal
                else:
                    ser2.write(str(3).encode())
    # When ctrl+c is pressed close the port
    except KeyboardInterrupt:
        print ('Caught KeyboardInterrupt')
        ser.close()
        ser2.close()