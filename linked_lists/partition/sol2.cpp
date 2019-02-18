#include "sll.h"

#include <iostream>
#include <vector>

node* partition(node* nd, const int& value) {
  node* beforehead = 0;
  node* beforetail = 0;
  node* afterhead = 0;
  node* aftertail = 0;

  while ( nd ) {
    if ( nd->data() < value ) {
       if ( beforehead ) {
          node* nd1 = nd->copy();
          beforetail->setNext(nd1);
          beforetail = nd1;
       } else {
          beforehead = nd->copy();
          beforetail = beforehead;
       }
    } else {
       if ( afterhead ) {
          node* nd1 = nd->copy();
          aftertail->setNext(nd1);
          aftertail = nd1;
       } else {
          afterhead = nd->copy();
          aftertail = afterhead;
       }
    }
    nd = nd->next();
  }
  
  node* res;
  if ( beforehead ) {
     beforetail->setNext(afterhead);
     res = beforehead;
  } else {
     res = afterhead;
  }
  
  return res;
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
  nd = partition(nd, 3);
  
  std::cout << "getting result: ";
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
}