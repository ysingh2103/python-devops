# Server Config Manager
# Chapter 1 Project

# --- Default config ---
config = {
    "server_name": "web-server-01",
    "ip_address": "192.168.1.10",
    "port": 443,
    "https_enabled": True,
    "max_connections": 500
}

# --- Function: display config ---
def show_config():
    # YOUR CODE: print each key-value from config
    print(f"Server Name : {config['server_name']}")
    print(f"IP Address  : {config['ip_address']}")
    print(f"Port        : {config['port']}")
    print(f"HTTPS       : {config['https_enabled']}")
    print(f"Max Conn    : {config['max_connections']}")

# --- Function: update a setting ---
def update_setting():
    # YOUR CODE: ask user which key to update, then new value
    key = input("Which setting do you want to update?: ")

    if key in config:
        print(f"Current value: {config[key]}")   # add this line
        new_value = input(f"Enter new value for {key}: ")
        config[key] = new_value
        print(f"updated! {key} is now: {config[key]}")
    else:
        print(f"Setting ' {key}' not found.")

# --- Function: check port ---
def check_port():
    # YOUR CODE: ask for port number, return service name
    port = input("Enter port number:")
    if port == '80':
        print("HTTP")
    elif port == '443':
        print("HTTPS")
    elif port == '22':
        print("SSH")
    elif port == '3306':
        print("MySQL")
    elif port == '53':
        print("DNS") 
    else:
        print("Unknown ")

# --- Main menu loop ---
def main():
    print("==== Server Config Manager ====")
    print("\n1. View current config")
    print("2. Update a setting")
    print("3. Check port info")
    print("4. Exit")
    while True:
        choice = input("Enter Choice: ")
        if choice == '1':
            show_config()
        elif choice == '2':
            update_setting()
        elif choice == '3':
            check_port()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
main()