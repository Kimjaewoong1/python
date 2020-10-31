#include<iostream>
using namespace std;

void myfunc(void)
{
	cout<<"myfunc(void) called"<<endl;
 }
 
 void myfunc(char c)
 {
 	cout<<"myfunc(char c) called"<<endl;
 }
 
 void myfunc(int a, int b)
 {
 	cout<<"my func(int a, int b) called"<<endl;
 }
 
 int main(void)
 {
 	myfunc();
 	myfunc('A');
 	myfunc(12, 13);
 	return 0;
 }
