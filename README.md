# Random MAC Tool

A Python-based utility for changing MAC addresses on Linux systems.

---

## Current Status

This project is currently being refactored from standalone scripts into a modular CLI-based tool.

* Existing scripts (`MAC(basic).py`, `MAC(advanced).py`) are functional
* New modular structure (`mac_tool.py`, `mac_utils.py`) has been introduced
* CLI features and improvements are under development

---

## Project Structure

```
Random-MAC/
│
├── mac_tool.py          # CLI entry point (work in progress)
├── mac_utils.py         # Core logic (work in progress)
│
├── MAC(basic).py        # Legacy script (uses ifconfig)
├── MAC(advanced).py     # Legacy script (uses ip link)
│
├── README.md
└── LICENSE
```

---

## Prerequisites

* Linux-based OS
* Python 3.x
* Root privileges (sudo)

---

## Current Usage (Legacy Scripts)

### Basic Version

```
python MAC(basic).py
```

### Advanced Version

```
python MAC(advanced).py
```

---

## Notes

* Changes are temporary and reset after reboot
* Works only on Linux systems
* Requires root privileges

---

## Roadmap

* [ ] Remove hardcoded interface names
* [ ] Add proper MAC generation (valid hex format)
* [ ] Implement CLI using argparse
* [ ] Add input validation
* [ ] Improve error handling
* [ ] Deprecate legacy scripts

---

## License

GNU GPL v2.0
