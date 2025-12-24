#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *file;
    char token[2048]; 
    char command[5120];
    int count = 0;

    const char *url = "https://login.emaktab.uz/login/?ReturnUrl=https%3a%2f%2femaktab.uz%2fuserfeed";
    const char *sst = "2200b7cc-c1b9-4d74-a31c-e4542ca0f065|24/12/2025 20:24:57";
    const char *auth_l = "1snyX7Tt2Ff6tG%2Fne6O9DZnId3yyUam74szC%2B5zZzq34CPYa54ERtAFZqb7K4%2B4is%2FBDICMPksqFb9MMp%2BcIsT1eknJFFeYeVs45PBOf907JFxZQ8wLaN8Bd6EdRkD%2Bc1TRfiJQk00WhSif3utopO17ibp%2BrJk%2FT%2BJ12x8rjhTrUDHyEcwbvtkhsxRbwAOgo0uZCpHTLgsINgQzDEaEqdmM3iGxdijS6g%2FDaTVi4Iav3rnyVapJPEtRTPefsH106OBxzKm%2FCP7nJS1YDIyknydyxmSXJYTs%2BVAxvkBntXMfiGixH5IH9CNLIjb%2FfOE97qSKdpw%3D%3D";

    file = fopen("token.txt", "r");
    if (file == NULL) {
        printf("Xato: token.txt fayli topilmadi!\n");
        return 1;
    }

    printf("Jarayon boshlandi. Barcha tokenlar bajarilmoqda...\n\n");

    // %s orqali o'qish bo'shliqlarni va qatorlarni yaxshiroq ajratadi
    while (fscanf(file, "%2047s", token) == 1) {
        
        // Token juda qisqa bo'lsa (shubhali bo'lsa) tashlab o'tadi
        if (strlen(token) < 20) continue; 

        count++;

        // Curl buyrug'i
        snprintf(command, sizeof(command), 
            "curl -s -o NUL -X POST \"%s\" "
            "-H \"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\" "
            "-b \"sst=%s; UZDnevnikAuth_l=%s; UZDnevnikAuth_a=%s; Dnevnik_localization=uz-Latn-UZ; a_r_p_i=23.3\"",
            url, sst, auth_l, token);

        // Buyruqni bajarish
        system(command);
        
        printf("[%d] Bajarildi: %.15s...\n", count, token);
    }

    fclose(file);
    printf("\n------------------------------\n");
    printf("Tugadi! Jami bajarilgan tokenlar: %d\n", count);

    return 0;
}