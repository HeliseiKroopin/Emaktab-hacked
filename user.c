#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char login[100];
    char password[100] = "a12345";
    char command[2048];

    printf("=== Emaktab Login (Windows Curl) ===\n");
    printf("Login: ");
    scanf("%99s", login);
    // Curl buyrug'ini shakllantiramiz
    // -s: jim rejim, -i: headerlarni ko'rsatish
    sprintf(command, 
        "curl -s -i -X POST \"https://login.emaktab.uz/login/?ReturnUrl=https%%3a%%2f%%2femaktab.uz%%2fuserfeed\" "
        "-H \"Content-Type: application/x-www-form-urlencoded\" "
        "--data-raw \"exceededAttempts=False&ReturnUrl=https%%3A%%2F%%2Femaktab.uz%%2Fuserfeed&FingerprintId=&login=%s&password=%s&Captcha.Input=&Captcha.Id=012d78f8-f94a-4f29-b2c1-f800a2bd8971\"", 
        login, password);

    printf("\nSo'rov yuborilmoqda...\n");
    
    // Buyruqni tizimga yuboramiz va natijani o'qiymiz
    FILE *fp = _popen(command, "r");
    if (fp == NULL) {
        printf("Curl topilmadi!\n");
        return 1;
    }

    char line[1024];
    int found = 0;
    while (fgets(line, sizeof(line), fp) != NULL) {
        // Faqat bizga kerakli tokenni ekranga chiqaramiz
        if (strstr(line, "UZDnevnikAuth_a=")) {
            printf("\n[MUVAFFAQIYATLI] Token topildi:\n%s", line);
            found = 1;
        }
    }

    if (!found) {
        printf("\n[XATO] Token topilmadi. Login/parol xato yoki Captcha so'ralmoqda.\n");
    }

    _pclose(fp);
    return 0;
}