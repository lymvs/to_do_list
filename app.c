#include <stdio.h>
#include <stdlib.h>

#include "read_file.h"

const size_t dir_size = 512;

int main()
{
    int n;

    char *filepath = get_filepath(dir_size);
    check_app_folder(filepath);

    printf("To-Do List options:\n");
    printf("1. Add task.\n");
    printf("2. Delete task.\n");
    printf("3. Mark task as completed.\n");
    printf("4. Exit program.\n\n");

    printf("Please select an option [1-4] to proceed.\n");
    scanf("%d", &n);
    printf("%d", n);

    free(filepath);

    return 0;
}