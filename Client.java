//////CLIENTE EN TABLET-PC ///
import java.io.*;
import java.net.*;
import java.util.Scanner; 

public class Client {
 
    private static String HOST = "127.0.0.1";
    private static int PUERTO = 8001;
 
    public static void main(String args[]) {
         
        Socket socket;
        DataOutputStream mensaje;
         
        try { 
            
            Scanner entrada=new Scanner(System.in);
            
            //Creamos nuestro socket
            System.out.println("Cliente iniciando conexión....");
            socket = new Socket(HOST, PUERTO);
            System.out.println("Cliente conectado!");
            mensaje = new DataOutputStream(socket.getOutputStream());
            
            while(true)
            {   
                System.out.println("Código de video?");
                String cadena=entrada.nextLine();
                System.out.println(cadena);
                           
                //mensaje = new DataOutputStream(socket.getOutputStream());
                if (cadena.equals("salir"))
                    break;
                //Enviamos el código
                mensaje.writeUTF(cadena);
                //mensaje.flush();


            }
            //Cerramos la conexión
            socket.close();
 
        } catch (UnknownHostException e) {
            System.out.println("El host no existe o no está activo.");
        } catch (IOException e) {
            System.out.println("Error de entrada/salida." + e.toString());
        }
         
    }
}
