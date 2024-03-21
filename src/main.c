#include <stdio.h>
#include <stdlib.h>

void main_menu();
void coc_nvim();
void yt_dl();
void download();
void clear_screen();

int main() {
    char choice;
    
    while (1) {
        main_menu();
        printf("select-| ");
        scanf(" %c", &choice);
        
        switch (choice) {
            case '0':
                exit(0);
            case '1':
                coc_nvim();
                break;
            case '2':
                yt_dl();
                break;
            default:
                printf("Invalid Option\n");
        }
    }
    return 0;
}

void main_menu() {
    clear_screen();
    printf("\n");
    printf(" _________  _______   ________  _____ ______      \n");
    printf("|\\___   ___\\  ___ \\ |\\   __  \\|\\   _ \\  _   \\    \n");
    printf("\\|___ \\  \\_\\ \\   __/|\\ \\  \\|\\  \\ \\  \\\\\\__\\ \\  \\   \n");
    printf("     \\ \\  \\ \\ \\  \\_|/_\\ \\   _  _\\ \\  \\\\|__| \\  \\  \n");
    printf("      \\ \\  \\ \\ \\  \\_|\\ \\ \\  \\\\  \\\\ \\  \\    \\ \\  \\ \n");
    printf("       \\ \\__\\ \\ \\_______\\ \\__\\\\ _\\\\ \\__\\    \\ \\__\\\n");
    printf("        \\|__|  \\|_______|\\|__|\\|__|\\|__|     \\|__|\n");
    printf("[Term Master.py, (c) by subuntux]\n");
    printf("[v.1.0]\n\n");
    printf("Special Menu\n");
    printf("[1]-Coc-Nvim Setup\n");
    printf("[2]-YouTube Downloader\n");
    printf("[0]-Exit\n");
}

void coc_nvim() {
    clear_screen();
    printf("\n[*] Start Setup\n\n");
    system("termux-wake-lock");
    system("cd $HOME");
    system("mkdir -p ~/.config/nvim/");
    system("cp /data/data/com.termux/files/usr/shared/pyterm/init.vim ~/.config/nvim/");
    system("cp /data/data/com.termux/files/usr/shared/pyterm/coc-setting.json ~/.config/nvim");
    system("curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim");
    printf("[*] Finish run: :PlugInstall in nvim\n");
    system("termux-wake-unlock");
    printf("\nPress Enter to continue...");
    while(getchar() != '\n');
    getchar(); // Wait for Enter key press
}

void yt_dl() {
    char choice;
    
    while (1) {
        clear_screen();
        printf("\nYT Downloader\n");
        printf("[1]-Install pytube\n");
        printf("[2]-Download Video\n");
        printf("[0]-Exit\n");
        printf("select-| ");
        scanf(" %c", &choice);
        
        switch (choice) {
            case '0':
                return;
            case '1':
                system("pip install pytube");
                break;
            case '2':
                download();
                break;
            default:
                printf("Invalid Option\n");
        }
    }
}

void download() {
    char url[100];
    clear_screen();
    printf("Enter YouTube URL-| ");
    scanf("%s", url);
    
    char command[100];
    sprintf(command, "pytube %s", url);
    system(command);
    printf("\nPress Enter to continue...");
    while(getchar() != '\n');
    getchar(); // Wait for Enter key press
}

void clear_screen() {
    printf("\033[2J\033[1;1H"); // ANSI escape code to clear screen
}