#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int num1, num2, num3, num4, total;
    int tot256 = 0, tot32 = 0;
    cout << "enter the first number: " << endl;
    cin >> num1;
    cout << "enter the second number: " << endl;
    cin >> num2;
    cout << "enter the third number: " << endl;
    cin >> num3;
    cout << "enter the fourth number: " << endl;
    cin >> num4;

    
        while(num1 >0 && num3>0 && num4>0){
            num1--;
            num3--;
            num4--;
            tot256++;
        
        } 
            while(num1 > 0 && num2 > 0){
                num1--;
                num2--;
                tot32++;
            }
        total = tot256 * 256 + tot32 * 32;
        
        cout << total;
        return 0;
}