package socketTest;

import java.io.*;
import java.net.*;

public class tcpServer {
    public static void main(String argv[]) throws Exception {
        String sentence;

        ServerSocket socket = new ServerSocket(6789); // 서버소켓 생성
        while (true) {
            Socket connect = socket.accept(); // 연결 요청 올때까지 기다림
            DataOutputStream outToClient = new DataOutputStream(connect.getOutputStream()); // client한테 보낼 버퍼
            BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connect.getInputStream())); // client한테
                                                                                                               // 받을 버퍼
            sentence = "20172673\n";
            outToClient.writeBytes(sentence); // 버퍼에 넣고 보냄
            sentence = inFromClient.readLine(); // client한테 받은 거 읽어옴

            System.out.println("From Client : " + sentence);
        }
    }
}
