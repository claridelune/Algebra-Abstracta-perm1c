#include <iostream>
using namespace std;
 
int invMod(int, int, int*, int*);
int euclidesExtendido(int, int, int*, int*);
int mod(int, int);

int main()
{
  int o = -40 % 121;
  int x, y, a = 13, m = 7;
  int i = invMod(a, m, &x, &y);
  cout << o << endl;
  if(i!=0) cout << "El inverso es: " << i << endl;
  return 0;
}

int mod(int x,int n){ // para que funcione con positivos y negativos
    return (x % n + n) %n; 
} 

int invMod(int a, int m, int *x, int *y){
  int mcd = euclidesExtendido(a, m, x, y);
  if(mcd == 1){
    cout << *x << endl;
    cout << m << endl;
    int ans = mod(*x, m);
    cout << ans;
    return ans;
  }
  cout << "No tiene inverso" << endl;
  return 0;
}

int euclidesExtendido(int a, int b, int *x, int *y)
{
  if (b == 0)
  {
    *x = 1;
    *y = 0;
    return a;
  }

  int x1, y1;
  int mcd = euclidesExtendido(b, a%b, &x1, &y1);

  *x = y1;
  *y = x1 - (a/b) * y1;

  return mcd;
}
