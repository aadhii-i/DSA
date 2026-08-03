#include<iostream>
using namespace std;
 class node
 {
    public :
      int data;
      node* next;
      
      
      node(int value)
      {
        data = value;
        next = nullptr;

      }
 };


 int main()
 {
    node*first = new node(2);
    node*second = new node(3);
    node*third = new node(4);
    
    first->next = second;
    second->next = third;
    cout<<first->data<<" "<<second->data<<" "<<third->data<<endl;
    return 0;

 }