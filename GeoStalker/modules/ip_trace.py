import requests
from color_utils.printx import print_success, print_error, print_info

def ip_trace(ip):
    print_info(f"Tracing IP: {ip}")
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as,query")
        data = res.json()
        if data['status'] != 'success':
            print_error(f"Failed to trace IP: {data.get('message', 'Unknown error')}")
            return None
        print_success(f"IP {ip} traced successfully.")
        return data
    except Exception as e:
        print_error(f"Exception while tracing IP: {e}")
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ip_trace.py <ip_address>")
        sys.exit(1)
    ip = sys.argv[1]
    info = ip_trace(ip)
    if info:
        for k, v in info.items():
            print(f"{k}: {v}")
