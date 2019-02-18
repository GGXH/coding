#include "sll.h"

#include <iostream>
#include <vector>

node* sumLists(node* nd1, node* nd2) {
   unsigned int add = 0;
   int k = 0;
   node* head = 0;
   node* tail = 0;
   while ( nd1 || nd2 ) {
      int s = 0;
      if ( nd1 ) {
         s += nd1->data();
         nd1 = nd1->next();
      }
      if ( nd2 ) {
         s += nd2->data();
         nd2 = nd2->next();
      }
      s += add;
      node* nd = new node(s%10, k);
      if ( !head ) {
         head = nd;
         tail = head;
      } else {
         tail->setNext(nd);
         tail = nd;
      }
      add = s / 10;
      ++k;
   }
   if ( add == 1 ) {
      node* nd = new node(add, k);
      tail->setNext(nd);
   }
   return head;
}


int main() {
  sll slinked_list;
  sll slinked_list1;
  std::vector<int> value{1, 2, 3};
  std::vector<int> value1{9, 2, 1};
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
  
  for (auto& it : value1) {
    std::cout << key << std::endl;
    if (key == 0) {
      slinked_list1.insertHead(it, key);
    } else {
      slinked_list1.insertLast(it, key);
    }
    ++key;
  }
  
  node* nd = slinked_list.head();
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
   
  nd = slinked_list1.head();
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
   
  nd = slinked_list.head();
  node* nd1 = slinked_list1.head();
  nd = sumLists(nd, nd1);
  
  std::cout << "getting result: ";
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
}
       