# Import the os module, which provides a way to interact with the file system
import os

# Define a function to read in the device list from a file
def read_device_list(file_path=None):
    # If no file path is specified, use the current working directory and the default file name
    if file_path is None or file_path == '':
        file_path = os.path.join(os.getcwd(), 'device_list.txt')
    
    # Open the file in read mode and read in each line as a separate element in a list
    with open(file_path, 'r') as f:
        device_list = [line.strip() for line in f.readlines()]

    # Return the list of devices
    return device_list

# Define a function to write the device list to a file
def write_device_list(file_path, device_list):
    # Open the file in write mode and write each device on a separate line
    with open(file_path, 'w') as f:
        for device in device_list:
            f.write(device + '\n')
