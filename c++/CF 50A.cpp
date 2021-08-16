#include <iostream>
 
using namespace std;
 
int main(){
 
    int m,n;
    cin >> m >> n;
 
    if ((m*n)%2==1){
        cout << (m-1) * n/2 + static_cast<int>(n)/2 << endl;
    }
 
    else{
        cout << m*n/2 << endl;
    }
 
 
    return 0;
}
