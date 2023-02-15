from netmiko import ConnectHandler
from datetime import datetime
import os
import getpass

def save_running_config(device_ip, login):
    # create device dictionary with device type, ip and login information
    device = {
        'device_type': 'cisco_ios',
        'ip': device_ip,
        **login,
    }

    try:
        # connect to the device
        net_connect = ConnectHandler(**device)

        # get the hostname of the device
        hostname = net_connect.send_command('show run | include hostname').split()[1]

        # create a timestamp for the backup file name
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # create a folder for the hostname, if it doesn't already exist
        folder_path = f"{hostname}/"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # create a file name for the backup
        filename = f"{folder_path}{hostname}_{timestamp}.txt"

        # backup the running configuration to a file
        output = net_connect.send_command('show running-config')
        with open(filename, 'w') as f:
            f.write(output)

        # disconnect from the device
        net_connect.disconnect()

        # return a success message
        return True, f"Configuration saved for device {hostname} ({device_ip})."

    except Exception as e:
        # return an error message
        return False, f"Error while connecting to device {device_ip}: {e}"
