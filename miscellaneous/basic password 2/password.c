#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc == 2) {
        char compare[] = "this is a much more secure password, i think";
        if (strcmp(argv[1], compare) == 0) {
            printf("Congrats! The key is bcactf{its_another_password}\n");
        } else {
            printf("Incorrect passcode.\n");
            return 1;
        }
    } else {
        fprintf(stderr, "Usage: %s <password>", argv[0]);
        return 1;
    }

    return 0;
}