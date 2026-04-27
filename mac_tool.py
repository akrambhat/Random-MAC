
import argparse
from mac_utils import (
    generate_mac,
    validate_mac,
    get_current_mac,
    change_mac,
    reset_mac
)


def main():
    parser = argparse.ArgumentParser(description="MAC Address Tool")

    parser.add_argument("--interface", required=True, help="Network interface (e.g., wlan0)")
    parser.add_argument("--random", action="store_true", help="Generate and apply random MAC")
    parser.add_argument("--set", help="Set a custom MAC address")
    parser.add_argument("--reset", action="store_true", help="Reset MAC address")
    parser.add_argument("--show", action="store_true", help="Show current MAC address")

    args = parser.parse_args()

    interface = args.interface

    if args.show:
        mac = get_current_mac(interface)
        if mac:
            print(f"[+] Current MAC: {mac}")
        else:
            print("[-] Could not retrieve MAC")

    elif args.random:
        new_mac = generate_mac()
        success = change_mac(interface, new_mac)

        if success:
            print(f"[+] Random MAC applied: {new_mac}")
        else:
            print("[-] Failed to change MAC")

    elif args.set:
        if not validate_mac(args.set):
            print("[-] Invalid MAC format")
            return

        success = change_mac(interface, args.set)

        if success:
            print(f"[+] MAC changed to: {args.set}")
        else:
            print("[-] Failed to change MAC")

    elif args.reset:
        success = reset_mac(interface)

        if success:
            print("[+] MAC reset successfully")
        else:
            print("[-] Failed to reset MAC")

    else:
        print("[-] No valid option provided. Use --help")


if __name__ == "__main__":
    main()
