package socketTest;

import java.net.*;

public class udpClient {
    public static void main(String argv[]) throws Exception {
        String sentence;

        DatagramSocket clientSocket = new DatagramSocket(); // 소켓 생성
        InetAddress ip = InetAddress.getLocalHost(); // ip 가져옴
        byte[] sendData = new byte[1024]; // 데이터 크기 설정
        byte[] receiveData = new byte[1024];
        sentence = "MUNSOO\n";
        sendData = sentence.getBytes();
        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, ip, 9876);// 패킷 만듦
        clientSocket.send(sendPacket);// 해당 ip와 포트번호로 보냄

        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        clientSocket.receive(receivePacket);// 패킷 받아옴
        sentence = new String(receivePacket.getData());

        System.out.println("From server : " + sentence);// 출력
        clientSocket.close();
    }
}
