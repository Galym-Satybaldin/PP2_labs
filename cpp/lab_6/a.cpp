#include <iostream>
using namespace std;

void calc(string expression) {
    string sign;
    for (int i = 0; i<expression.size(); ++i){
        if (i == '+' || i == '-' || i == '/' || i == '*'){
            sign = i;
        }
    }

    for (int i = 0; i<sign; ++i){
        
    }
    

    cout<<letter<<endl;;

}

int main() {
    string expression;
    getline (cin, expression);
    calc(expression);
    

    return 0;
}
