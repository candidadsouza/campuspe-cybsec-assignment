#include <stdio.h>
#include <unistd.h>
#include <arpa/inet.h>

// function to check if a port is open or closed
int scan_port(int port) {

    int sock;  // variable for socket
    struct sockaddr_in target;  // structure to store IP and port

    // create a socket
    sock = socket(AF_INET, SOCK_STREAM, 0);

    // set IP address (localhost)
    target.sin_family = AF_INET;
    target.sin_port = htons(port);  // convert port to network format
    target.sin_addr.s_addr = inet_addr("127.0.0.1");  // localhost IP

    // try to connect to the port
    if (connect(sock, (struct sockaddr *)&target, sizeof(target)) == 0) {
        close(sock);  // close socket
        return 1;     // port is OPEN
    }

    close(sock);      // close socket
    return 0;         // port is CLOSED
}

int main() {

    // ports we want to check
    int ports[] = {22, 80, 443, 3306};

    printf("Scanning ports on localhost (127.0.0.1)...\n");

    // loop through each port
    for (int i = 0; i < 4; i++) {

        int port = ports[i];  // get current port

        // check if port is open or closed
        if (scan_port(port) == 1) {
            printf("Port %d: OPEN\n", port);
        } else {
            printf("Port %d: CLOSED\n", port);
        }
    }

    return 0;  // end of program
}
