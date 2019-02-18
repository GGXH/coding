#include "sll.h"

#include <iostream>
#include <vector>

unsigned int linkedListSize(node* nd) {
  unsigned int res = 0;
  while ( nd != nullptr ) {
     ++res;
     nd = nd->next();
  }
  return res;
}

node* intersection(node* nd1, node* nd2) {
   unsigned int size1 = linkedListSize(nd1);
   unsigned int size2 = linkedListSize(nd2);
   if ( size1 < size2 ) {
     return intersection(nd2, nd1);
   }
   
   for (int i = 0; i < size1 - size2; ++i) {
      nd1 = nd1->next();
   }
   
   for ( int i = 0; i < size2; ++i ) {
      if ( nd1 == nd2 ) {
         return nd1;
      }
      nd1 = nd1->next();
      nd2 = nd2->next();
   }
   return nullptr;
}
  

int main() {
  sll slinked_list;
  std::vector<int> value{1, 2, 3, 2, 1, 1};
  int key = 0;
  for (auto& it : value) {
    if (key == 0) {
      slinked_list.insertHead(it, key);
    } else {
      slinked_list.insertLast(it, key);
    }
    ++key;
  }
  
  
  sll slinked_list1;
  std::vector<int> value1{1, 2, 3, 2, 1, 1};
  key = 0;
  for (auto& it : value1) {
    if (key == 0) {
      slinked_list1.insertHead(it, key);
    } else {
      slinked_list1.insertLast(it, key);
    }
    ++key;
  }
  
  node* nd = slinked_list.head();
  node* nd1 = slinked_list1.head();
  node* ndres = intersection(nd, nd->next()->next());

  if ( ndres == nullptr ) {
     std::cout << "no intersection";
  } else {
     std::cout << ndres->data();
  }
  
  std::cout << std::endl;
}
