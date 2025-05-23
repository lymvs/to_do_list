#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char *get_filepath(size_t dir_size)
{
    char *filepath = (char *)malloc(dir_size);
    if (filepath == NULL)
    {
        return NULL;
    }

#ifdef _WIN32
    strcpy(filepath, "C:\\Users\\");
    strcat(filepath, getenv("USERNAME"));
    strcat(filepath, "\\todo_tasks.txt");
#else
    strcat(filepath, getenv("HOME"));
    strcat(filepath, "/.todo_tasks.txt");
#endif

    return filepath;
}

void read_file(char *filepath, FILE *fptr, int chunk)
{
    fptr = fopen(filepath, 'r');

    char *read_chunk[chunk];

    if (fptr != NULL)
    {
        while (fgets(read_chunk, chunk, fptr))
        {
            printf("%s", read_chunk);
        }
    }
    else
    {
        printf("No project started yet!\n");
    }

    fclose(fptr);
}
