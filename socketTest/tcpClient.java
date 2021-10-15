package socketTest;

import java.io.*;
import java.net.*;

public class tcpClient {
    public static void main(String argv[]) throws Exception {
        String sentence;

        Socket clientSocket = new Socket("127.0.0.1", 6789); // 서버에 연결
        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream()); // 서버에 보낼 버퍼
        BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream())); // 서버한테
                                                                                                                // 받을 버퍼
        sentence = "MUNSOO\n";
        outToServer.writeBytes(sentence); // 서버한테 보냄
        sentence = inFromServer.readLine(); // 서버한테 받은거 읽어옴

        System.out.println("From Server : " + sentence);

        clientSocket.close(); // socket 닫음
    }
}
