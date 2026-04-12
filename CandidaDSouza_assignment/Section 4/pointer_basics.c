#include <stdio.h>

int main() {
    int port = 80;          // variable
    int *ptr = &port;       // pointer to port

    // print using variable
    printf("Port value (variable): %d\n", port);

    // print using pointer
    printf("Port value (pointer): %d\n", *ptr);

    // change value using pointer
    *ptr = 443;

    // print new value
    printf("New port value: %d\n", port);

    return 0;
}
