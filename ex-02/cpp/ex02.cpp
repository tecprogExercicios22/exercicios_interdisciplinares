// Código por Giovanni Sartori

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
using namespace std;

class Ex2Sorteio{
    private:
        int sorteado;
    public:
    Ex2Sorteio(){
        srand(time(NULL));
        sorteado = rand()%1000;
    }

    ~Ex2Sorteio(){}

    void sorteio(){
        int palpite = -1, achou = 0;
        while(!achou){
        cout << "Digite seu palpite: ";
        cin >> palpite;
        if(palpite > sorteado){
            cout << "Quase! Um pouco menos..." << endl;
        }
        else if(palpite < sorteado){
            cout << "Quase! Um pouco mais..." << endl;
        }
        else
            achou = 1;
        }

        cout << "Parabéns! Você acertou o número correto: " << sorteado << endl;
    }
};

int main(){
    Ex2Sorteio ex2;
    ex2.sorteio();
}