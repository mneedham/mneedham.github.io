+++
draft = false
date="2013-07-14 14:31:44"
title="Java: Testing a socket is listening on all network interfaces/wildcard interface"
tag=['software-development']
category=['Networking']
+++

<p>I previously wrote <a href="http://www.markhneedham.com/blog/2013/07/14/learning-more-about-network-sockets/">a blog post describing how I've been trying to learn more about network sockets</a> in which I created some server sockets and connected to them using <a href="http://nc110.sourceforge.net/">netcat</a>.</p>


<p>The next step was to do the same thing in Java and I started out by writing a server socket which echoed any messages sent by the client:</p>



~~~java

public class EchoServer {
    public static void main(String[] args) throws IOException {
        int port = 4444;
        ServerSocket serverSocket = new ServerSocket(port, 50, InetAddress.getByAddress(new byte[] {0x7f,0x00,0x00,0x01}));
        System.err.println("Started server on port " + port);

        while (true) {
            Socket clientSocket = serverSocket.accept();
            System.err.println("Accepted connection from client: "  + clientSocket.getRemoteSocketAddress() );

            In  in  = new In (clientSocket);
            Out out = new Out(clientSocket);

            String s;
            while ((s = in.readLine()) != null) {
                out.println(s);
            }

            System.err.println("Closing connection with client: " + clientSocket.getInetAddress());
            out.close();
            in.close();
            clientSocket.close();
        }
    }
}

public final class In {
    private Scanner scanner;

    public In(java.net.Socket socket) {
        try {
            InputStream is = socket.getInputStream();
            scanner = new Scanner(new BufferedInputStream(is), "UTF-8");
        } catch (IOException ioe) {
            System.err.println("Could not open " + socket);
        }
    }

    public String readLine() {
        String line;
        try {
            line = scanner.nextLine();
        } catch (Exception e) {
            line = null;
        }
        return line;
    }

    public void close() {
        scanner.close();
    }
}

public class Out {
    private PrintWriter out;

    public Out(Socket socket) {
        try {
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }

    public void close() {
        out.close();
    }

    public void println(Object x) {
        out.println(x);
        out.flush();
    }
}
~~~

<p>I ran the main method of the class and this creates a server socket on port 4444 listening on the 127.0.0.1 interface and we can connect to it using netcat like so:</p>



~~~bash

$ nc -v 127.0.0.1 4444
Connection to 127.0.0.1 4444 port [tcp/krb524] succeeded!
hello
hello
~~~

<p>The output in my IntelliJ console looked like this:</p>



~~~text

Started server on port 4444
Accepted connection from client: /127.0.0.1:63222
Closing connection with client: /127.0.0.1
~~~

<p>Using netcat is fine but what I actually wanted to do was write some test code which would check that I'd made sure the server socket on port 4444 was accessible via all interfaces i.e. bound to 0.0.0.0.</p>


<p>There are actually some <a href="http://docs.oracle.com/javase/tutorial/networking/nifs/retrieving.html">quite nice classes in Java</a> which make this very easy to do and wiring those together I ended up with the following client code:</p>



~~~java

public class EchoClient {
    public static void main(String[] args) throws IOException {
        Enumeration<NetworkInterface> nets = NetworkInterface.getNetworkInterfaces();
        for (NetworkInterface networkInterface : Collections.list(nets)) {
            for (InetAddress inetAddress : Collections.list(networkInterface.getInetAddresses())) {
                Socket socket = null;
                try {
                    socket = new Socket(inetAddress, 4444);
                    System.out.println(String.format("Connected using %s [%s]", networkInterface.getDisplayName(), inetAddress));
                } catch (ConnectException ex) {
                    System.out.println(String.format("Failed to connect using %s [%s]", networkInterface.getDisplayName(), inetAddress));
                } finally {
                    if (socket != null) {
                        socket.close();
                    }
                }
            }
        }

    }
}
~~~

<p>If we run the main method of that class we'll see the following output (on my machine at least!):</p>



~~~text

Failed to connect using en0 [/fe80:0:0:0:9afe:94ff:fe4f:ee50%4]
Failed to connect using en0 [/192.168.1.89]
Failed to connect using lo0 [/0:0:0:0:0:0:0:1]
Failed to connect using lo0 [/fe80:0:0:0:0:0:0:1%1]
Connected using lo0 [/127.0.0.1]
~~~

<p>Interestingly we can't even connect via the loopback interface using IPv6 which is perhaps not that surprising in retrospect given we bound using an IPv4 address.</p>


<p>If we tweak the second line of EchoServer from:</p>



~~~java

ServerSocket serverSocket = new ServerSocket(port, 50, InetAddress.getByAddress(new byte[] {0x7f,0x00,0x00,0x01}));
~~~

<p>to:</p>



~~~java

ServerSocket serverSocket = new ServerSocket(port, 50, InetAddress.getByAddress(new byte[] {0x00,0x00,0x00,0x00}));
~~~

<p>And restart the server before re-running the client we can now connect through all interfaces:</p>



~~~text

Connected using en0 [/fe80:0:0:0:9afe:94ff:fe4f:ee50%4]
Connected using en0 [/192.168.1.89]
Connected using lo0 [/0:0:0:0:0:0:0:1]
Connected using lo0 [/fe80:0:0:0:0:0:0:1%1]
Connected using lo0 [/127.0.0.1]
~~~

<p>We can then wrap the EchoClient code into our testing framework to assert that we can connect via all the interfaces.</p>

