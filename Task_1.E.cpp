#include <iostream>
using namespace std;

int main() {
    int s, t, a, b, m, n; 
    cin >> s ;
    cin >> t ;
    cin >> a ;
    cin >> b;
    cin >> m;
    cin >> n;
    int ac = 0;
    int oc = 0;
    for (int i = 0; i < m; i++) {
        int d;
        cin >> d;
        int landing = a + d;
        if (landing >= s && landing <= t) {
            ac++;
        }
    }
    for (int i = 0; i < n; i++) {
        int d;
        cin >> d;
        int landing = b + d;
        if (landing >= s && landing <= t) {
            oc++;
        }
    }
    
    cout << ac << endl;
    cout << oc << endl;
    
    return 0;
}
