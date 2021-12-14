#include<iostream>
using namespace std;
class node{
public:
int prn;
node* next;
node(){
    prn=0;
    next=NULL;
}
};
class linkedlist{
    node* head=NULL;
public:
void insertnode(int a){
    node* newnode=new node();
    newnode->prn=a;
    newnode->next=NULL;
    if(head==NULL){
        head=newnode;
    }
    else{
        node* temp=head;
        while(temp->next!=NULL){
            temp=temp->next;
        }
        temp->next=newnode;
    }
}
void deletenode(int n){
    node *a;
    node* b;
    node* c;
    a=head;
    while(true){
        if(a->next->prn==n){
            b=a->next;
            c=b->next;
            a->next=c;
            delete b;
            break;
        }
    }
}
void concatenation(linkedlist l1,linkedlist l2){
    node *q;
    node*w;
    q=l1.head;
    w=l2.head;
    while(true){
        if(q->next==NULL){
            
            q->next=w;
            cout<<"\n occured"<<endl;
            break;
        }
        else{
            q=q->next;
        }
    }
}
void display(){
    node* temp=head;
    while(temp!=NULL){
        cout<<temp->prn<<"-";
        temp=temp->next;
    }
    }
void displayconcat(linkedlist l1,linkedlist l2){
        node*temp=l1.head;
        while(temp!=NULL){
            cout<<temp->prn<<"-";
            temp=temp->next;

        }
    }

};
int main(){
    linkedlist l1,l2,l3;
    int n,num,del;
    cout<<"How many students data is to be entered ";
    cin>>n;
    for(int i=0;i<n;i++){
        cout<<"Enter the data ";
        cin>>num;
        l1.insertnode(num);
    }
    cout<<"Linked list looks like this "<<endl;
    l1.display();
    cout<<"\n delete node? "<<endl;
    cout<<"Enter the number that need to be deleted ";
    cin>>del;
    l1.deletenode(del);
    l1.display();
    //---------------------------------------------------------------------
    cout<<"2nd linked list"<<endl;
    cout<<"How many students data is to be entered ";
    cin>>n;
    for(int i=0;i<n;i++){
        cout<<"Enter the data ";
        cin>>num;
        l2.insertnode(num);
    }
    cout<<"Linked list looks like this "<<endl;
    l2.display();
    //-------------------------------------------------------------------
    l3.concatenation(l1,l2);
    l3.displayconcat(l1,l2);
    return 0;
}
