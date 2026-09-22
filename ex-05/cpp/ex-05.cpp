#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

class ExecString{
    private:
        string str1, str2;
        int ocorrencias;
    public:
        ExecString(){
            getline(cin, str1);
            getline(cin, str2);
            ocorrencias = 0;
            if(str2.length() && str1.length()){
                calculaOcorrencias(str1, str2);
            }
        };
        
        void calculaOcorrencias(string s1, string s2){
            size_t pos = s1.find(s2, 0);
            while(pos != s1.npos){
                ocorrencias++;
                pos = s1.find(s2, pos + 1);
            }

            cout << "Os caracteres '" << s2 << "' aparecem " << ocorrencias << " vezes na string '" << s1 << "'." << endl;
        };
};  

int main (){
    ExecString exString;
    return 0;
}