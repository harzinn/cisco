#!/usr/bin/env python3

from netmiko import ConnectHandler
from datetime import datetime
import os
import getpass

def save_running_config():
    # Read in the file containing the IP addresses or hostnames of the devices to connect to
    with open('device_list.txt', 'r') as f:
        device_list = [line.strip() for line in f.readlines()]

    # Prompt the user for their login credentials
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Define the login credentials for the devices
    login = {
        'username': username,
        'password': password,
    }

    print("Connecting to devices...")

    # Loop over each device in the list and connect to it, saving its running configuration to a file in a directory named after the device's hostname
    for device_ip in device_list:
        device = {
            'device_type': 'cisco_ios',
            'ip': device_ip,
            **login,
        }
        try:
            net_connect = ConnectHandler(**device)
            hostname = net_connect.send_command('show run | include hostname').split()[1]
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            folder_path = f"{hostname}/"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            filename = f"{folder_path}{hostname}_{timestamp}.txt"
            output = net_connect.send_command('show running-config')
            with open(filename, 'w') as f:
                f.write(output)
            net_connect.disconnect()
            print(f"Configuration saved for device {hostname} ({device_ip}).")
        except Exception as e:
            print(f"Error while connecting to device {device_ip}: {e}")

    print("All configurations saved successfully.")


if __name__ == '__main__':
    while True:
        print("Choose an option:")
        print("1. Save running configuration of Cisco devices")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            save_running_config()
            print("Running configuration saved successfully.")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
