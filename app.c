#include <stdio.h>

int main() {
    int n;

    printf("To-Do List options:\n");
    printf("1. Add task.\n");
    printf("2. Delete task.\n");
    printf("3. Mark task as completed.\n");
    printf("4. Exit program.\n\n");

    printf("Please select an option [1-4] to proceed.\n");
    scanf("%d", &n);
    printf("%d", n);

    return 0;
}