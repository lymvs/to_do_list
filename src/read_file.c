#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>

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
    strcat(filepath, "\\.todolist");
#else
    strcpy(filepath, getenv("HOME"));
    strcat(filepath, "/.todolist");
#endif

    return filepath;
}

int check_app_folder(const char *path)
{
    DIR *dir;
    struct dirent *entry;
    int status = 0;

    dir = opendir(path);
    if (dir == NULL)
    {
        status = mkdir(path, 0755);
        if (status == 0)
        {
            printf("Directory '%s' created successfully.\n", path);
            dir = opendir(path);
            if (dir == NULL) {
                printf("Unable to create directory. Please check permissions.\n");
                return 1;
            }
        }
        else
        {
            printf("Unable to create directory.\n");
            return 1;
        }
    }
    while ((entry = readdir(dir)) != NULL)
    {
        printf("%s\n", entry->d_name);
    }
    closedir(dir);
    return 0;
}

void read_file(char *filepath, FILE *fptr, int chunk)
{
    fptr = fopen(filepath, "r");

    char read_chunk[chunk];

    if (fptr != NULL)
    {
        while (fgets(read_chunk, chunk, fptr))
        {
            printf("%s", read_chunk);
        }
        fclose(fptr);
    }
    else
    {
        printf("No project started yet!\n");
    }
}
