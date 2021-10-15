package socketTest;

import java.net.*;

public class udpServer {
    public static void main(String argv[]) throws Exception {
        String sentence;

        DatagramSocket serverSocket = new DatagramSocket(9876); // 소켓 생성
        byte[] sendData = new byte[1024]; // 데이터 크기 설정
        byte[] receiveData = new byte[1024];
        while (true) {
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
            serverSocket.receive(receivePacket); // 패킷 받아옴
            sentence = new String(receivePacket.getData());
            System.out.println("From client : " + sentence);// 출력

            InetAddress ip = receivePacket.getAddress();
            int port = receivePacket.getPort();
            sentence = "20172673\n";
            sendData = sentence.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, ip, port);// 패킷 만듦
            serverSocket.send(sendPacket);// 해당 ip와 포트번호로 보냄
        }
    }
}
