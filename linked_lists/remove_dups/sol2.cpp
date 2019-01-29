#include "sll.h"

#include <iostream>
#include <unordered_map>
#include <vector>


void remove_dups(sll& slinked_list) {
  if ( slinked_list.size() <= 1 ) return;
  node* nd = slinked_list.head();
  while (nd) {
    node* nd_a = nd->next();
    int d = nd->data();
    while (nd_a) {
      if ( nd_a->data() == d ) {
        int k = nd_a->key();
        nd_a = nd_a->next();
        slinked_list.del(k);
      } else {
        nd_a = nd_a->next();
      }
    }
    nd = nd->next();
  }
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
  
  std::cout << "before remove" << std::endl;
  
  remove_dups(slinked_list);
  
  std::cout << "after remove" << std::endl;
  
  nd = slinked_list.head();
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
}