#include <stdio.h>
#include <math.h>
int main (){
    int sepatuA = 400000, sepatuB = 350000;
    printf("Harga sepatu A adalah %.f \n", sepatuA);
    printf("Harga sepatu B adalah %.f \n", sepatuB);
    printf("Sepatu A mendapat diskon 13%% sehingga harganya menjadi %d \n", sepatuA - sepatuA * 13/100);
    printf("Sepatu B mendapat diskon 21%% sehingga harganya menjadi %d \n", sepatuB - sepatuB * 21/100);
}