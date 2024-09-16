#include <stdio.h>
#include <stdlib.h>

int main() {
    char ascii_number[] = "12345.67";
    double number = atof(ascii_number);

    printf("Double: %f\n", number);
    return 0;
}
