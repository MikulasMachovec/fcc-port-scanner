import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    try: 
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return "Error: Invalid hostname"
        # need to add ip error check
    is_ip = target.replace('.', '').isdigit()
    
    if is_ip:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = ip
    else:
        hostname = target

    for port in range(port_range[0], port_range[1] + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            continue

    if verbose:
        output = f"Open ports for {hostname} ({ip})\n"
        output += "PORT     SERVICE\n"
        for port in open_ports:
            service = ports_and_services.get(port, 'unknown')
            output += f"{port:<9}{service}\n"
        return output.strip()
    else:
        return open_ports
