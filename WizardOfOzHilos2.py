'''
# Import everything needed to edit video clips
from moviepy.editor import *
  
# loading video gfg
clip = VideoFileClip("appJosue.mp4")
  
# showing clip
print(str(clip.duration))
'''
import socket
import sys
import cv2
import numpy as np
import threading
import argparse
import signal

global archivo
global cambio 
def handler(signum, f):
    #connection.close()
    print("Se forzo la salida del programa")
    exit(1)

def play_video(arch):
    cap = cv2.VideoCapture(arch)
    cambio = False
    print("Inicia play video...")   
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame',frame)
            if cambio:
                cap = cv2.VideoCapture(arch)
                cambio = False
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        # Break the loop displaying video
        else: 
            break
    
            # When everything done, release the video capture object
    cap.release()
    
        # Closes all the frames
    cv2.destroyAllWindows()

def conectar(direccion, puerto):
    #definición de códigos para ejecutar videos
    codigo11="11"
    codigo12="12"
    codigo13="13"
    codigo21="21"
    codigo22="22"
    codigo23="23"
    codigo31="31"
    codigo32="32"
    codigo33="33"

    host = socket.gethostname() 
    print("este servidor se llama:")
    print(host)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    #server_address = ('148.231.81.79', 5000) DIRECCION DE FIM
    server_address = (direccion, puerto) #DIRECCION mi CASA
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)
    print("Iniciando...")

    ########################################
    while True:

        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            while True:
                data = str(connection.recv(2), 'UTF-8')
                print("recibido: ", data)
                if data == codigo11:
                    print('Desplegar video con codigo 11')
                    archivo = "11.mp4"
                elif data == codigo12:
                    print('Desplegar video con codigo 12')
                    archivo = "12.mp4"
                elif data == codigo13:
                    print('Desplegar video con codigo 13')
                    archivo = "13.mp4"
                elif data == codigo21:
                    print('Desplegar video con codigo 21')
                    archivo = "21.mp4"
                elif data == codigo22:
                    print('Desplegar video con codigo 22')
                    archivo = "22.mp4"
                elif data == codigo23:
                    print('Desplegar video con codigo 23')
                    archivo = "23.mp4"
                elif data == codigo31:
                    print('Desplegar video con codigo 31')
                    archivo = "31.mp4"
                elif data == codigo32:
                    print('Desplegar video con codigo 32')
                    archivo = "32.mp4"
                elif data == codigo33:
                    print('Desplegar video con codigo 33')
                    archivo = "33.mp4" 
                ## Si una de las anteriores opciones fue verdadera, entonces ejecutar el video cap
                if data:
                    print('sending data back to the client')
                    cambio = True
                    #connection.sendall(data)
                else:
                    print('no data from', client_address)
                    break
        finally:
            # Clean up the connection
            connection.close()
def main(args):
    h2=threading.Thread(target=conectar, args = (args.direccion, args.puerto))
    h2.start()
    archivo = args.video
    cambio = False
    play_video(archivo)
    while True:
        if cambio:
            print("archivo actual: " + archivo)
            play_video(archivo)
            cambio = False

# Manejar las interrupciones con esta funcion
signal.signal(signal.SIGINT, handler)

# Parsear argumentos de entrada
argparser = argparse.ArgumentParser("Servidor reproductor de videos WoZ")
argparser.add_argument('-d', '--direccion', default = '127.0.0.1')
argparser.add_argument('-p', '--puerto', default = 8001, type = int)
argparser.add_argument('-v', '--video', default = "11.mp4")
args = argparser.parse_args()
main(args)
