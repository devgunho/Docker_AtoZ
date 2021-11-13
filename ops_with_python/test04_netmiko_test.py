from netmiko import (
    ConnectHandler,
    NetMikoTimeoutException,
    NetMikoAuthenticationException,
)

# Define the device details
device = {
    "device_type": "linux",  # Use 'linux' for Ubuntu
    "ip": "172.16.0.123",  # Replace with the actual IP address
    "username": "ubuntu",  # Username
    "password": "1",  # Password
    "port": 22,  # SSH port
}

try:
    # Establish the connection
    net_connect = ConnectHandler(**device)
    print(f"Successfully connected to {device['ip']}")

    # List of commands to execute
    commands = ["uptime", "df -h", "free -m", "who"]

    # Execute each command and print the output
    for command in commands:
        print(f"\nExecuting command: {command}")
        output = net_connect.send_command(command)
        print(f"Output:\n{output}")

except NetMikoTimeoutException:
    print(f"Connection to {device['ip']} timed out. Please check the device status.")
except NetMikoAuthenticationException:
    print(f"Authentication failed for {device['ip']}. Please check your credentials.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection if it was established
    try:
        net_connect.disconnect()
        print(f"Disconnected from {device['ip']}")
    except:
        print("Failed to disconnect.")
