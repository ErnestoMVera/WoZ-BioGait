import socket
import signal
import sys
import cv2
import numpy as np
import argparse
import select
def recv_timeout(sock, bytes_to_read, timeout_seconds):
    sock.setblocking(0)
    ready = select.select([sock], [], [], timeout_seconds)
    if ready[0]:
        return sock.recv(bytes_to_read)
def handler(signum, f):
    connection.close()
    print("Se forzo la salida del programa")
    print(f"video {video}")
    exit(1)
def agarrarVideo(cap):
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            yield frame

signal.signal(signal.SIGINT, handler)
argparser = argparse.ArgumentParser("Servidor reproductor de videos WoZ")
argparser.add_argument('-d', '--direccion', default = '127.0.0.1')
argparser.add_argument('-p', '--puerto', default = 8001, type = int)
argparser.add_argument('-v', '--video', default = "11.mp4")
args = argparser.parse_args()
print("host ip: " + args.direccion)
 
host = socket.gethostname() 

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (args.direccion, args.puerto) #DIRECCION mi CASA
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)


# Listen for incoming connections
sock.listen(1)
sock.settimeout(10)
print("Iniciando...")
########################################
video = args.video
while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            cap = cv2.VideoCapture(video)
            for frame in agarrarVideo(cap):
                data = recv_timeout(connection, 2, 0.01)
                if data != None:
                    if data == b'\x00\x02':
                        continue
                    print(data.hex())
                    dataFormat = str(data,'UTF-8')
                    print(f"se leyo {dataFormat}")
                    video = dataFormat + ".mp4"
                    print(f"{dataFormat}.mp4")
                    cap.release()
                    break
                cv2.imshow("Juego",frame)
                cv2.waitKey(1)
            
    finally:
        # Clean up the connection
        connection.close()

