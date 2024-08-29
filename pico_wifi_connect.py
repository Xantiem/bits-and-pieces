import network
import time
import sys
import socket
import machine

# Turn on onboard led
led = machine.Pin("LED", machine.Pin.OUT)

# connect to wifi

for i in range(3):
    led.toggle()
    time.sleep(2)


SSID= "TCL30"
PHRASE = "pepper333"

retry = 5
retry_con = 0
not_con = True

while not_con and retry_con < retry:
    net = network.WLAN(network.STA_IF)
    net.active(True)

    time.sleep(4)
    
    net.connect(SSID, PHRASE)

    time.sleep(4)
    
    if net.isconnected():
        not_con = False
        print('[connected]: success')
        led.on()
    else:
        retry_con += 1
        time.sleep(2)
        print(f'[disconnected]: retrying (attempt {retry_con})')
        led.off()
if not_con:
    print(f"[disconnected]: connection failure after {retry} attempt(s) ABORTING...")
    sys.exit()

ip_conf = net.ifconfig()
print(f"[connected]: connected {ip_conf}")

# socket part
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8000))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    print(f'[socket connection]: {addr}')
    led.off()

    try:
        rec = conn.recv(1024)
        print(f'[socket receive]: {rec}')

        response = """\
HTTP/1.1 200 OK

{}
""".format("Hello world")
        conn.send(response.encode('utf-8'))
    except Exception as e:
        print(f'[socket error]: {e}')
    finally:
        conn.close()  # Ensure the connection is closed
        net.active(False)
