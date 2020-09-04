import serial
import sys


def getline(port):
    buf = b''
    while True:
        c = port.read(1)
        if c == b'$':
            buf = buf + c
            break
    while True:
        c = port.read(1)
        buf = buf + c
        if c == b'\n':
            return buf


def try_get_register(port, nbr):
    port.reset_input_buffer()
    port.write('\r\n$VNRRG,{}*XX\r\n'.format(nbr).encode())
    for i in range(10):
        line = getline(port)
        if line.startswith(b'$VNRRG'):
            return line.decode()
    return None


def get_register(port, nbr):
    reg = None
    while reg is None:
        reg = try_get_register(port, nbr)
    return reg


def get_magnetic_field(port):
    reg = get_register(port, 17) # see page 95 of VN 100 user manual
    reg = reg.rstrip('\n\r')[:-3]
    r = reg.split(',')
    return {'mag': [float(mag) for mag in r[2:5]]}


def get_imu(port):
    reg = get_register(port, 15) # see page 95 of VN 100 user manual
    reg = reg.rstrip('\n\r')[:-3]
    r = reg.split(',')
    return {'q':[float(q) for q in r[2:6]],
            'acc':[float(a) for a in r[9:12]],
            'omega': [float(i) for i in r[12:15]]}


if __name__ == '__main__':
    port = serial.Serial(sys.argv[1], 115200)
    print(get_imu(port))

    import time

    while 1:
        print(get_imu(port))
        time.sleep(0.1)
