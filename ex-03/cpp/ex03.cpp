// Código por Giovanni Sartori

#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

class Ex3Permutacao {
    private:
        int a;
        int b;
        int resultado;

        vector<int> contaDigitos(int n){
            vector<int> digitos(10, 0);

            n = abs(n); // garante que não há acesso indevido de memória

            // loop de preenchimento do vetor
            while(n > 0 )
            {
                if(n % 10) // se a unidade for diferente de 0 
                    digitos[n%10]++;
                
                n /= 10;
            }

            return digitos;
        };
        
        int checarPermutacao(int a, int b){
            // A lógica aqui é contar quantas vezes cada algarismo aparece em a e b e checar se os números batem
            vector<int> na = contaDigitos(a);
            vector<int> nb = contaDigitos(b);
            int igual = 1;
            for(int i = 0; i < 10; i++){
                if(na[i] != nb[i])
                    igual = 0;
            };

            return igual;
        };  

    public:
        Ex3Permutacao(){
            cout << "Digite A: ";
            cin >> a;
            cout << "Digite B: ";
            cin >> b;
            resultado = checarPermutacao(a, b);
        }

        int getResultado(){
            return resultado;
        }
};

int main(){
    Ex3Permutacao ex3;
    cout << ex3.getResultado() << endl;

    return 0;
}
