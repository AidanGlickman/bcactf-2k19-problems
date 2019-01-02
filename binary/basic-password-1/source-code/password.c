#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc == 2) {
        if (atoi(argv[1]) == 1234) {
            printf("Congrats! The key is bcactf{hey_its_a_password}\n");
        } else {
            printf("Incorrect passcode.\n");
            return 1;
        }
    } else {
        fprintf(stderr, "Usage: %s <passcode>", argv[0]);
        return 1;
    }

    return 0;
}