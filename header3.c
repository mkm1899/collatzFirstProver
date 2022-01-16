#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>


struct equation{
    unsigned long long k,c;
};

#define SIZE 30
unsigned int *arr[SIZE];
unsigned int ks[SIZE];
unsigned int length[SIZE];
unsigned int ksLength = 0;

//returns true if found and false otherwise
char binarySearch(int arr[], int n, int num){
    int low = 0;
    int high = n;
    while(low < high){
        int mid = (low + high)/2;
        if(arr[mid] == num){
            return 1;
        }
        else if(arr[mid] > num){
            high = mid;
        }
        else {
            low = mid+1;
        }
    }
    return 0;
}

// returns true if it is checked in checkBasics
char isBasic(unsigned long long num){
    return num == 3 || num == 9 || num == 81 || num == 729;
}

//checks the cases where there are only one or two equations
char checkBasics(unsigned long long num){
    if((num-2)%3 == 0){
        return 1;
    }
    else if((num-4)%9 == 0){
        return 1;
    }
    else if((num-10)%81 == 0){
        return 1;
    }
    else if((num-604)%729 == 0 || (num-433)%729 == 0){
        return 1;
    }
    return 0;
}

struct equation readLine(FILE *fp){
    char c;
    const unsigned int size = 30;
    char num[size];
    int i = 0;
    struct equation rtn;
    rtn.c = 0;
    char first = 1;
    do {
        c = fgetc(fp);
        if(isdigit(c) && i < size){
            num[i] = c;
            i++;
        } else if(isdigit(c) && i >= size){
            perror("sizeToStoreNumbers is not large enough");
            exit(1);
        } else if (!isdigit(c) && i != 0){
            //not a digit;
            num[i] = '\0';
            i = 0;
            if(first){
                rtn.k = strtoull(num, NULL, 10);
            }
            else{
                rtn.c = strtoull(num, NULL, 10);
            }
            first = 0;
        }
        if(c == '\n'){
            break;
        }
    } while(!feof(fp));
    return rtn;
}

unsigned int log3(unsigned long long num){
    unsigned int i = 0;
    while(num > 1){
        num /= 3;
        i++;
    }
    return i;
}

void readFromFile(char *filename, void(*fun)(struct equation)){
    FILE *fp;
    fp = fopen(filename, "r");
    if(fp == NULL){
        perror("Error opening file");
        exit(1);
    }

    char prev = '\0';
    do {
        char c = fgetc(fp);
        if(c == '\t' && prev == '\n'){
            struct equation eq = readLine(fp);
            fun(eq);
            c = '\n';
        }
        if(c == '\n'){
            prev = '\n';
        }
        else{
            prev = '\0';
        }
    } while(!feof(fp));
}

void updateLength(struct equation eq){
    if(!isBasic(eq.k)){
        unsigned int l3 = log3(eq.k);
        if(l3 >= SIZE){
            perror("length of array is inadequate");
            exit(-1);
        }
        if (length[l3] == 0){
            ks[ksLength] = eq.k;
            ksLength++;
        }
        length[l3]++;
    }
}

void updateArray(struct equation eq){
    static unsigned int i = 0;
    if(!isBasic(eq.k)){
        unsigned int l3 = log3(eq.k);
        if(l3 >= SIZE){
            perror("length of array is inadequate");
            exit(-1);
        }
        arr[l3][i] = eq.c;
        i++;
        if(i >= length[l3]){
            i = 0;
        }
    }
}

int compare (const void * num1, const void * num2) {
   if(*(unsigned int*)num1 > *(unsigned int*)num2)
    return 1;
   else
    return -1;
}


void initComplexChecks(char *fileName){
    for(int i = 0; i< SIZE; i++){
        length[i] = 0;
    }

    readFromFile(fileName, updateLength);

    for(int i=0; i<SIZE; i++){
        if(length[i] != 0){
            arr[i] = (unsigned int*) malloc(sizeof(**arr)*length[i]);
        }
    }

    readFromFile(fileName, updateArray);

    for(int i=0; i<SIZE; i++){
        if(length[i] != 0){
            qsort(arr[i], length[i], sizeof(**arr), compare);
        }
    }
}

void printArr(unsigned int j){
    j = log3(j);
    for(int i=0; i<length[j]; i++){
        printf("%d, ", arr[j][i]);
    }
    printf("\n");
}

//returns 0 if not in any of the equations
char check(unsigned int n){
    if(checkBasics(n)){
        return 1;
    }
    for(int i=0; i<ksLength; i++){
        unsigned int l3 = log3(ks[i]);
        if( binarySearch(arr[l3], length[l3], n%ks[i])){
            return 1;
        }
    }
    return 0;
}

void main(){
    initComplexChecks("./equationsV1-1.txt");
    //printArr(2187);
    for(unsigned int i=3; i<1000; i++){
        if(!check(i)){
            printf("%d\n", i);
        }
    }
}

