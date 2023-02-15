# Cisco Network Configuration Backup Tool

The Cisco Network Configuration Backup Tool is a Python script that automates the process of saving the running configuration of Cisco network devices. This tool uses the `netmiko` library to connect to the devices over SSH and save their configurations to a file on the local machine. This guide will help you use the tool to back up the running configuration of your Cisco network devices.

## Prerequisites

Before you can use the Cisco Network Configuration Backup Tool, you must have the following:

- Python 3.x installed on your computer
- The `paramiko` and `netmiko` Python libraries installed
- A text file containing the IP addresses or hostnames of the Cisco devices you want to back up

## Installation

To install the Cisco Network Configuration Backup Tool, follow these steps:

1. Download the script from the GitHub repository: https://github.com/harzinn/cisco/blob/main/test/backup_cisco_config.py
2. Save the script to a directory on your computer.
3. Install the `paramiko` and `netmiko` libraries by running the following command in your terminal or command prompt:

    pip install paramiko netmiko

## Usage

To use the Cisco Network Configuration Backup Tool, follow these steps:

1. Open the `device_list.txt` file in a text editor and add the IP addresses or hostnames of the Cisco devices you want to back up, one per line.
2. Open a terminal or command prompt and navigate to the directory where the script is saved.
3. Run the script using the following command:

    python backup_cisco_config.py

4. When prompted, enter your username and password for the Cisco devices.
5. The script will connect to each device in the list, save its running configuration to a file, and disconnect. The configuration files will be saved in a directory named after the device's hostname and timestamp of the backup.
6. Once all configurations have been saved, the script will print a success message.

Note: If you want to change the name or location of the `device_list.txt` file, you can do so by modifying the following line in the script:

    with open('device_list.txt', 'r') as f:

Replace `device_list.txt` with the name and path of your text file.

## Troubleshooting

If the Cisco Network Configuration Backup Tool encounters an error, it will print an error message to the console. Some common issues and solutions are:

- Invalid login credentials: If the script cannot connect to a device, make sure that you have entered the correct username and password for the device.
- Firewall issues: If the script cannot connect to a device, make sure that the firewall on the device is not blocking the SSH connection.
- Incorrect device type: If you are backing up a device that is not a Cisco IOS device, you may need to modify the `device_type` variable in the script to match the device type.

If you encounter an error that is not listed here, try searching the issue on the [netmiko GitHub repository](https://github.com/ktbyers/netmiko/issues).

## Conclusion

The Cisco Network Configuration Backup Tool is a powerful and convenient tool for backing up the running configuration of your Cisco network devices. By automating the backup process, you can save time and reduce the risk of errors. If you have any questions or issues, feel free to reach out to the developer or the [netmiko community](https://github.com/ktbyers/netmiko).

## Contributing

Contributions to this project are welcome! If you find a bug or have an idea for a new feature, please open an issue on GitHub or submit a pull request.

Before making a contribution, please read the CONTRIBUTING.md file in the root of the project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

This project was inspired by the work of several other network automation projects, including Ansible and Nornir.
