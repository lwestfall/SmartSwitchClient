import socket, sys
from netifaces import interfaces, ifaddresses, AF_INET

PORT = 5750

class SockSS:
    """ """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host):
        return self.sock.connect_ex((host, PORT))

    def settimeout(self, sec):
        self.sock.settimeout(sec)

    def get_state(self, addr):
        self.settimeout(0.05)
        result = self.connect(addr)
        if result == 0:
            sock.settimeout(1.2)
            switch_ips.append(subnet+str(i))
            sock.sock.send("CURRENT STATE?".encode("ascii"))
            data = sock.sock.recv(128)
            # print("From server: " + data)
            state = data
        sock.sock.close()
        return state

def toggle(addr, on_off=None):
    conn = SockSS(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    conn.settimeout(1)

    result = conn.connect(addr)

    if result == 0:
        conn.sock.send(("SWITCH " + on_off + "\r").encode("ascii"))
        ack = conn.sock.recv(32)
        return ack.decode()
    else:
        return result
    conn.sock.close()
    
def scan_switches(subnet):
    """ Scans subnet for devices on PORT """

    switch_ips = []
    switch_names = []
    strdata = ""
    j = 0
    print("Scanning devices on subnet %sXXX...\n" % subnet)
    for i in range(2,255):
        conn = SockSS(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        conn.settimeout(0.03)
        result = conn.connect(subnet+str(i))
        if i % 12 == 0:
            print("."),
        if result == 0:
            conn.settimeout(1.2)
            switch_ips.append(subnet+str(i))
            conn.sock.send("NAME?\r".encode("ascii"))
            data = b''
            data = conn.sock.recv(128)
            strdata += data.decode()
            # print("From server: " + strdata)
            switch_names.append(strdata)
            j += 1
        conn.sock.close()
    return switch_ips, switch_names


def get_subnet():
    local_ips = []

    for interface in interfaces():
        try:
            for link in ifaddresses(interface)[AF_INET]:
                if not link['addr'].endswith("1"):
                    if link['addr'].startswith("192") or link['addr'].startswith("10"):
                        local_ips.append(link['addr'])
        except KeyError:
            pass

    if local_ips.__len__() == 1:
        print('Connected to network with local IP: %s\n' % local_ips[0])
    elif local_ips.__len__() == 0:
        print('No local IPs found. Are you connected to a network?\n')
    elif local_ips.__len__() > 1:
        print('Multiple local IPs found.\nConnected to network with first found IP: %s\n' % local_ips[0])

    split_ips = local_ips[0].split(".")

    subnet = split_ips[0] + "." +  split_ips[1] + "." + split_ips[2] + "."

    return subnet

