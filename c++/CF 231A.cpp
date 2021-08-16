#include <iostream>

using namespace std;

int main(){
    int count {0};
    int a;
    cin >> a;

    for (int counter = 0; counter < a; counter++){
        int x,y,z;
        cin >> x >> y >> z;

        if (x + y + z > 1){
            count++;
        }

    }

    cout << count << endl;
    return 0;
}
