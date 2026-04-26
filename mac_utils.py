import random

def generate_mac():
    """
    Generate a valid random MAC address.
    Ensures:
    - Locally administered (LAA bit set)
    - Unicast address
    """
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]

    # Set locally administered bit and ensure unicast
    mac[0] = (mac[0] & 0b11111110) | 0b00000010

    return ':'.join(f"{x:02x}" for x in mac)