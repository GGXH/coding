#include "sll.h"

#include <iostream>
#include <vector>

node* partition(node* nd, const int& value) {
  node* head = nd->copy();
  node* tail = head;
  while ( nd->next() ) {
    nd = nd->next();
    if ( nd->data() > value ) {
      node* nd1 = nd->copy();
      tail->setNext(nd1);
      tail = nd1;
    } else {
      node* nd1 = nd->copy();
      nd1->setNext(head);
      head = nd1;
    }
  }
  return head;
}
  
  

int main() {
  sll slinked_list;
  std::vector<int> value{1, 2, 3, 1, 3, 4, 5, 1, 2, 3};
  int key = 0;
  for (auto& it : value) {
    std::cout << key << std::endl;
    if (key == 0) {
      slinked_list.insertHead(it, key);
    } else {
      slinked_list.insertLast(it, key);
    }
    ++key;
  }
  
  node* nd = slinked_list.head();
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
  
  nd = slinked_list.head();
  nd = partition(nd, 2);
  
  std::cout << "getting result: ";
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
}