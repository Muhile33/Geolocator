import requests
from stem import Signal
from stem.control import Controller

def use_tor_proxy():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)  # Request a new Tor circuit
    
    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }
    
    response = requests.get("http://httpbin.org/ip", proxies=proxies)
    print(f"Using Tor, new IP: {response.json()}")
