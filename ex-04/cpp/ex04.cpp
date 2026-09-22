// Código por Giovanni Sartori

#include <stdio.h>
#include <time.h>
#include <random>
#include <unistd.h>
#include <iostream>
using namespace std;

void sementear(){
    srand(time(NULL));
}

int main(){

    struct timespec inicio, fim;
    double tempo_gasto;

    int dig = 0;
    sementear();
    cout << "Se prepare..." << endl;
    unsigned int tempoAleatorioMS = rand()%5000; // dara o tempo em ms ate o aviso
    usleep(tempoAleatorioMS * 1000);

    cout << "AGORA! ";
    clock_gettime(CLOCK_MONOTONIC, &inicio);
    cin >> dig;
    clock_gettime(CLOCK_MONOTONIC, &fim);

    tempo_gasto = (fim.tv_sec - inicio.tv_sec) +
                  (fim.tv_nsec - inicio.tv_nsec) / 1000000000.0; // pega os nanosegundos decorridos
    cout << "Voce demorou " << tempo_gasto << " segundos." << endl;

    return 0;
}