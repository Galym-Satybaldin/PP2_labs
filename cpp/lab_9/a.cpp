#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main(){

    int n = 0;
    cin>>n;

    vector <int> arr;
    set <int> st;

    for (int i = 0; i<n; ++i){
        int x;
        cin>>x;
        arr.push_back(x);
    }

    sort(arr.begin(), arr.end());

    for (int i = 0; i<n; ++i){
        st.insert(arr[i]);
    }

    set <int> :: iterator it;

    vector <int> counterArr;

    

    for (it = st.begin(); it!= st.end(); ++it){
        int counter = 0;
        for (int i = 0; i<n; ++i){
            if (*it == arr[i]){
                counter++;
            }
            counterArr.push_back(counter);
        }
    }

    int highest = 0;

    for (int i = 1; i < counterArr.size(); ++i){
        if (counterArr[i-1]<counterArr[i]){
            highest = counterArr[i];
        }
    }

    for (int i = 1; i < counterArr.size(); ++i){
        if (counterArr[i] == highest){
            cout<<st[i]<<endl;
            break;
        }
    }





    
    return 0;
}
