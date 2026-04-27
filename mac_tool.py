
import argparse
from mac_utils import (
    generate_mac,
    validate_mac,
    get_current_mac,
    change_mac,
    reset_mac,
    get_interfaces
)


def main():
    parser = argparse.ArgumentParser(description="MAC Address Tool")

    parser.add_argument("--interface", help="Network interface (e.g., wlan0)")
    parser.add_argument("--random", action="store_true", help="Generate and apply random MAC")
    parser.add_argument("--set", help="Set a custom MAC address")
    parser.add_argument("--reset", action="store_true", help="Reset MAC address")
    parser.add_argument("--show", action="store_true", help="Show current MAC address")
    parser.add_argument("--list", action="store_true", help="List available network interfaces")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without applying changes")

    args = parser.parse_args()

    if args.list:
        interfaces = get_interfaces()

        if interfaces:
            print("[+] Available interfaces:")
            for iface in interfaces:
                print(f"  - {iface}")
        else:
            print("[-] No interfaces found")

        return

    if not args.interface:
        print("[-] Interface is required for this operation. Use --list to see available interfaces.")
        return

    interface = args.interface

    # interface validation
    available_interfaces = get_interfaces()

    if interface not in available_interfaces:
        print("[-] Invalid interface")
        print(f"[i] Available interfaces: {', '.join(available_interfaces)}")
        return

    if args.show:
        mac = get_current_mac(interface)
        if mac:
            print(f"[+] Current MAC: {mac}")
        else:
            print("[-] Could not retrieve MAC")

    elif args.random:
        old_mac = get_current_mac(interface)
        new_mac = generate_mac()

        if args.dry_run:
            print(f"[DRY-RUN] Would change MAC: {old_mac} → {new_mac}")
            return

        success = change_mac(interface, new_mac)

        if success:
            updated_mac = get_current_mac(interface)
            print(f"[+] MAC changed: {old_mac} → {updated_mac}")
        else:
            print("[-] Failed to change MAC (check interface name or permissions)")
            
    elif args.set:
        if not validate_mac(args.set):
            print("[-] Invalid MAC format")
            return

        old_mac = get_current_mac(interface)

        if args.dry_run:
            print(f"[DRY-RUN] Would change MAC: {old_mac} → {args.set}")
            return

        success = change_mac(interface, args.set)

        if success:
            updated_mac = get_current_mac(interface)
            print(f"[+] MAC changed: {old_mac} → {updated_mac}")
        else:
            print("[-] Failed to change MAC (check interface name or permissions)")

    elif args.reset:
        old_mac = get_current_mac(interface)

        if args.dry_run:
            print(f"[DRY-RUN] Would reset MAC for interface: {interface} (current: {old_mac})")
            return

        success = reset_mac(interface)

        if success:
            updated_mac = get_current_mac(interface)
            print(f"[+] MAC reset: {old_mac} → {updated_mac}")
        else:
            print("[-] Failed to reset MAC (check interface or permissions)")

    else:
        print("[-] No valid option provided. Use --help")


if __name__ == "__main__":
    main()
