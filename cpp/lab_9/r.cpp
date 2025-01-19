#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

long long factorial (int n){
    int fact = 1;
    for (int i = 1; i<=n; ++i){
        fact*=i;
    }
    return fact;
}

long long combination(int n, int k){
    if (k>n){return 0;}
    return factorial(n)/(factorial(k)*factorial(n-k));
}

long long derangement(int n){
    if (n == 0) return 1; // Base case: D(0) = 1
    if (n == 1) return 0; // Base case: D(1) = 0
    // Compute using the recursive formula: D(n) = (n-1) * (D(n-1) + D(n-2))
    long long prev2 = 1; // D(0)
    long long prev1 = 0; // D(1)
    long long current = 0;
    for (int i = 2; i <= n; ++i) {
        current = (i - 1) * (prev1 + prev2);
        prev2 = prev1;
        prev1 = current;
    }
    return current;
}



int main(){
    int n = 0, k = 0;
    cin>>n>>k;
       

    long long combinations = combination(n,k);
    long long derangements = derangement(n-k);
    long long result = combinations * derangements;

    cout<<result<<endl;
    return 0; 
}