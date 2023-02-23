#!/bin/bash

# Read the device list from the device_list.txt file
devices=($(cat device_list.txt))

# Prompt for the username for the SSH connections
read -p "Enter username: " username

# Loop through the device list and establish an SSH connection to each device in a separate terminal window
for device in "${devices[@]}"
do
    gnome-terminal --tab --title="$device" -- ssh "$username@$device"
done
