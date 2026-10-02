#include "stdio.h"
#include "string"
#include "iostream"
using namespace std;

// Referências da classe string: https://cplusplus.com/reference/string/string/

class Solution {
private:
    std::string s;
public:
    std::string abreviado;

    Solution(std::string s) {
        this->s = s;
        abreviado = "";
        abreviar();
    }

    void abreviar(){
        if(!s.length()) return;
        string* palavras = split(s, ' ');
        if(!palavras) return;
        // Para cada palavra no array, pega a primeira letra (se o tamanho for maior que 2)
        for(int i = 0; i < s.length(); i++){        
            char primeiraLetra = palavras[i][0];
            if(palavras[i].length() > 2){
                abreviado += primeiraLetra;
                abreviado += ".";
            } else {
                abreviado += " ";
                abreviado += palavras[i];
                abreviado += " ";
            }
        };
    }

    string* split(std::string s, char delimitador){
        // Algoritmo de separação de uma string em palavras
        // Repetidamente pega a primeira ocorrencia do delimitador e separa a string em duas partes
        // A primeira parte é armazenada em um array de strings e a segunda parte é usada para a próxima iteração
        if(!s.length()) return nullptr;
        string* palavras = new string[s.length()];
        int i = 0;
        while(s.length()){
            size_t pos = s.find(delimitador, 0);
            if(pos == s.npos){
                // acabou as palavras
                palavras[i] = s;
                break;
            }
            palavras[i] = s.substr(0, pos);
            s = s.substr(pos + 1, s.length() - pos);
            i++;
        }
        return palavras;
    }
};

int main(){
    Solution* solucao = new Solution("Exercicio de Giovanni Schrickte Sartori");
    std::cout << solucao->abreviado << std::endl;
    return 0;
}