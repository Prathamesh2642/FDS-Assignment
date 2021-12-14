#include<iostream>
#include<string.h>
#define max 50
using namespace std;

class stack{
    char arr[max];
    int top;
    int length;
    public:
    stack(){
        top=-1;
    }
    int isfull(){
        if(top>=max-1){
            return 0;
        }
        else{
            return 1;
        }
    }
    int isempty(){
        if(top==-1){
            return 0;
        }
        else{
            return 1;
        }
    }
    void push(char val){
        if(isfull()==0){
            cout<<"Stack is full";
        }
        else{
            top++;
            arr[top]=val;
            cout<<val<<" is pushed now"<<endl;
        }
    }
        char pop(){
            if(isempty()==0){
                cout<<"Stack is empty";
            }
            else{
                char c=arr[top];
                top--;
                cout<<c<<" is popped now"<<endl;
                return c;
            }

        }

        void palindrome(char q[50],int length){
            int count=0;
            for(int i=0;i<length;i++){
                char x=q[i];
                if(x==pop()){
                    count++;
                }
            }
        if (count==length){
            cout<<"Palindrome";
        }
        else{
            cout<<"Not a palindrome";
        }

        }
};
int main(){
    stack s1;
    char z[50];
    int len;
    cout<<"Enter string ";
    cin>>z;
    len=strlen(z);
    for(int i=0;i<len;i++){
        char q=z[i];
        s1.push(q);
    }
    s1.palindrome(z,len);
    return 0;
}
