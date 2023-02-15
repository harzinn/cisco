# import necessary functions from other modules
from device_list import read_device_list, write_device_list
from netmiko_utils import save_running_config
import getpass

# create an infinite loop that repeatedly prompts user for input
while True:
    # print the options menu
    print("Choose an option:")
    print("1. Save running configuration of Cisco devices")
    print("2. Exit")

    # get the user's choice
    choice = input("Enter your choice: ")

    # if user chooses option 1, prompt for device list file, username, and password
    if choice == "1":
        device_list_file = input("Enter the path to the device list file: ")
        device_list = read_device_list(device_list_file)
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        login = {
            'username': username,
            'password': password,
        }
        print("Connecting to devices...")
        
        # iterate over each device in the list and attempt to save the running configuration
        for device_ip in device_list:
            success, message = save_running_config(device_ip, login)
            if success:
                print(message)
            else:
                print(f"Failed: {message}")
        print("All configurations saved successfully.")

    # if user chooses option 2, break out of the loop and exit the program
    elif choice == "2":
        print("Exiting program.")
        break

    # if user inputs an invalid choice, prompt them to try again
    else:
        print("Invalid choice. Please try again.")
