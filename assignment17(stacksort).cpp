#include<iostream>
#define max 50
using namespace std;
class stack{
 int arr[max],top,checkarr[max];
 public:
 stack(){
     top=-1;
 }
 int isempty(){
     if(top==-1){
         return 0;
     }
     else{
         return 1;
     }
 }
 int isfull(){
     if (top>=max){
         return 0;
     }
     else{
         return 1;
     }
 }
 void push(int val){
     if(isfull()==0){
         cout<<"Stack is full";
     }
     else{
         top++;
         arr[top]=val;
         cout<<arr[top]<<" pushed in the stack"<<endl;
     }
 }
 int pop(){
     if(isempty()==0){
         cout<<"Stack is empty";
     }
     else{
         int z;
        z=arr[top];
        top--;
        cout<<z<<" is popped"<<endl;
        return z;
     }
 }
 void display(int n){
     cout<<"Stack elements are"<<endl;
     for(int i=0;i<n;i++){
         cout<<arr[i]<<" ";
     }
     cout<<"\n";
 }

 void sortit(int n){
     for(int i=0;i<n;i++){
            checkarr[i]=pop();
     }
        for(int i=0;i<n-1;i++){
            int min=i;
                for(int j=i+1;j<n;j++){
                    if(checkarr[min]<checkarr[j]){
                        min=j;
                    }
                }
                if(min!=i){
                    swap(checkarr[min],checkarr[i]);
                }
            
        }

    for(int i=n-1;i>0;i--){
        cout<<checkarr[i]<<" ";
    }

 }
 
};
int main(){
    stack s1;
    int n,num;
    cout<<"Enter the number of numbers in the array ";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cout<<"Enter the number ";
        cin>>num;
        s1.push(num);
    }
    s1.display(n);
    s1.sortit(n);

    return 0;
}
