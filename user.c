#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char login[100];
    char password[100]; // Standart parol
    char command[2048];

    printf("=== Emaktab Login (Token Extractor) ===\n");
    printf("Login: ");
    scanf("%99s", login);
    // Curl buyrug'i
    sprintf(command, 
        "curl -s -i -X POST \"https://login.emaktab.uz/login/?ReturnUrl=https%%3a%%2f%%2femaktab.uz%%2fuserfeed\" "
        "-H \"Content-Type: application/x-www-form-urlencoded\" "
        "--data-raw \"exceededAttempts=False&ReturnUrl=https%%3A%%2F%%2Femaktab.uz%%2Fuserfeed&FingerprintId=&login=%s&password=%s&Captcha.Input=&Captcha.Id=012d78f8-f94a-4f29-b2c1-f800a2bd8971\"", 
        login, password);

    printf("\nSo'rov yuborilmoqda...\n");
    
    FILE *fp = _popen(command, "r");
    if (fp == NULL) {
        printf("Xato: Curl bajarilmadi!\n");
        return 1;
    }

    char line[2048];
    int found = 0;
    while (fgets(line, sizeof(line), fp) != NULL) {
        // "UZDnevnikAuth_a=" qismini qidiramiz
        char *start = strstr(line, "UZDnevnikAuth_a=");
        if (start) {
            // Nuqtali vergulgacha bo'lgan qismini topamiz
            char *end = strchr(start, ';');
            if (end) {
                *end = '\0'; // Satrni nuqtali vergulda to'xtatamiz
            }
            
            printf("\n[MUVAFFAQIYATLI] Cookie topildi:\n%s\n", start);
            found = 1;
            break; // Token topilgach tsiklni to'xtatish
        }
    }

    if (!found) {
        printf("\n[XATO] Token topilmadi. Login yoki parol xato bo'lishi mumkin.\n");
    }

    _pclose(fp);
    return 0;
}