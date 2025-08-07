#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main (){
    int numb;
    double percent;
    double total;
    double totalper;
    cout << "enter the number of orange-containing drinks: ";
    cin >> numb;
    if(numb <= 0 ){    cout << "invalid number" << endl;
    return 0;}
    
    for(int i=1; i<=numb;i++){
    cout << "enter the percentage of orange juice in the drink" << endl;

      cin >> percent; 
     total += percent;
      if(percent < 0 ||percent> 100){
        cout << "invalid number" << endl;
    return 0;}

      } 
     cout << "the number of drinks: " << numb <<endl;
    
      totalper = total/(numb*100) *100;
    cout << "the total percentage of orange juice in the drinks is: "<< setprecision(4) << totalper << "%";
    cout << totalper;
    
      return 0;
    }

