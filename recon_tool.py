import socket

target = input("Enter domain: ")

try:
    ip = socket.gethostbyname(target)
    print(f"\nScanning target: {target} ({ip})")
    print("Starting scan...\n")

    ports = [21, 22, 80, 443]

    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        
        s.close()

except:
    print("Error occurred")
