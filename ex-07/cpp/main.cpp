#include <stdio.h>
#include <string> 
#include <iostream>
using namespace std;

class Solution{
private:
    string s;
public:
    Solution(){
        s = "";
    }

    void exec(){
        getline(cin, s);
        inverter();
    }

    void inverter(){
        if(!s.length()) return;
        for(int i = s.length() - 1; i >= 0; i--){
            cout << s[i];
        };
        cout << endl;
    }
};

int main(){
    Solution* sol = new Solution();
    sol->exec();
    return 0;
}