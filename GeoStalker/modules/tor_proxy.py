from stem import Signal
from stem.control import Controller
from color_utils.printx import print_success, print_error, print_info

def set_tor_proxy(port=9050, control_port=9051, password=None):
    print_info("Connecting to Tor control port...")
    try:
        controller = Controller.from_port(port=control_port)
        if password:
            controller.authenticate(password=password)
        else:
            controller.authenticate()
        controller.signal(Signal.NEWNYM)
        print_success("Tor proxy renewed successfully.")
        controller.close()
        return True
    except Exception as e:
        print_error(f"Failed to connect/authenticate to Tor: {e}")
        return False

if __name__ == "__main__":
    set_tor_proxy()
