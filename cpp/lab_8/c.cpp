# include <bits/stdc++.h>

using namespace std;

int main(){
    int n = 0;
    cin>>n;
    vector <int> arr1;
    set <int> arr2;

    for (int i = 0; i<n; ++i){
        int x = 0;
        cin>>x;
        arr1.push_back(x);
        arr2.insert(x);
    }

    int sum = 0;

    set<int>:: iterator it;

    for (it = arr2.begin(); it != arr2.end(); ++it){
        int count = 0;
        for (int j = 0; j<arr1.size(); ++j){
            if (*it==arr1[j]){
                count ++;
            }
            if (count>=2){
                sum++;
                break;
            }
        }
    }

    cout<<sum;


    return 0;
}