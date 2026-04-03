from scanner import PortScanner
def banner():
    print("""
╔══════════════════════════════╗
║       Network Tool v1.0      ║
╚══════════════════════════════╝
Usage:
  - Enter target IP  (e.g. 127.0.0.1)
  - Enter port range (e.g. 1024 = scan 1-1024)
  - Max ports: 65535
""")

def menu():
    print("\n=== Network Tool ===")
    print("[1] Scan ports")
    print("[2] Exit")
    return input("Choose: ")

def main():
    banner()
    while True:
        choice = menu()

        if choice == "1":
            target = input("Target IP: ")
            end    = int(input("How many ports to scan: "))
            
            scanner = PortScanner(target)
            scanner.scan_all_port(end=end)
            scanner.save_as_json()

        elif choice == "2":
            print("Bye!")
            break

if __name__ == "__main__":
    main()