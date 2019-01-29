#include "sll.h"

#include <iostream>
#include <vector>

void del_mid(node* nd) {
   node* nd_a = nd->next();
   nd->setData(nd_a->data());
   nd->setKey(nd_a->key());
   nd->setNext(nd_a->next());
   delete nd_a;
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
  
  std::cout << "getting result: ";
  int k;
  std::cin >> k;
  
  nd = slinked_list.head();
  for(auto i = 0; i < k; ++i) {
    nd = nd->next();
  }
  del_mid(nd);
  
  nd = slinked_list.head();
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
}