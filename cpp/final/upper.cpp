#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main(){
    string n;
    getline(cin, n);
    for (int i = 0; i<n.size(); ++i){
        if (n[i]>='A' && n[i]<='Z'){
            n[i]=n[i]+32;
        }
    }
    cout<<n<<endl;


    return 0;
}