#include <bits/stdc++.h>
using namespace std;
int main(){
	int a,b,c;
	int resp = 0;
	cin >> a >> b >> c;
	cout << max(b - a,c - b) - 1 << endl;
	return 0;
}