# Random MAC Tool

A Python-based CLI utility to generate, change, and manage MAC addresses on Linux systems.

---

## Features

* Generate valid random MAC addresses
* Set custom MAC addresses
* Reset MAC address
* Display current MAC address
* List available network interfaces
* Validate interface before execution
* Dry-run mode to preview changes without applying them

---

## Prerequisites

* Linux-based OS
* Python 3.x
* Root privileges (sudo)
* `ip` command available

---

## Usage

### List available interfaces

```
python mac_tool.py --list
```

### Show current MAC

```
python mac_tool.py --interface wlan0 --show
```

### Apply random MAC

```
python mac_tool.py --interface wlan0 --random
```

### Set custom MAC

```
python mac_tool.py --interface wlan0 --set 00:11:22:33:44:55
```

### Reset MAC

```
python mac_tool.py --interface wlan0 --reset
```

### Dry run (no changes applied)

```
python mac_tool.py --interface wlan0 --random --dry-run
```

---

## Notes

* Changes are temporary and reset after reboot
* Requires root privileges
* Works on Linux systems only

---

## License

GNU GPL v2.0
