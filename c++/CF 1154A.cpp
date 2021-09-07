#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){

    int p,q,r,s;

    cin >> p >> q >> r >> s;
    vector<int> nums {p,q,r,s};

    int m = max({p,q,r,s});

    for (int n:nums){
        if (m-n != 0)
            cout  <<  m-n << " ";
    }

    return 0;
}
