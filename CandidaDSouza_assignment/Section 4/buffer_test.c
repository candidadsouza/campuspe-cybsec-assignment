#include <stdio.h>
#include <string.h>

int main() {
    char buffer[16];   // vulnerable buffer
    char input[100];   // user input

    printf("Enter some text: ");
    fgets(input, 100, stdin);

    // remove newline character
    input[strcspn(input, "\n")] = 0;

    // check input length
    if (strlen(input) <= 15) {
        printf("Safe input (within buffer limit)\n");
    } else {
        printf("Warning: Input too long! Possible buffer overflow\n");
    }

    // unsafe copy (intentional vulnerability)
    strcpy(buffer, input);

    printf("You entered: %s\n", buffer);

    return 0;
}

/*
1. What happens with long input?
If the input is longer than the buffer size (16 characters), it causes a buffer overflow. This may lead to unexpected behavior or crash the program (segmentation fault).

2. Why is this dangerous?
It is dangerous because it can overwrite memory and allow attackers to execute malicious code or gain control of the system.

3. How would you fix it?
Use safer functions like fgets() or strncpy() and limit the input size to prevent overflow.
*/
