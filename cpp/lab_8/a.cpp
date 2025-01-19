#include <bits/stdc++.h>
using namespace std;
int main()
{
    vector<pair<int, int>> se;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        se.push_back({a, b});
    }
    sort(se.begin(), se.end());
    for (int it = 0; it < n; it++)
    {
        cout << (se[it]).first << " " << (se[it]).second << endl;
    }
    return 0;
}