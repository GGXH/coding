#include "sll.h"

#include <iostream>
#include <vector>

int kth_to_last(node* nd, int& target, int& k) {
  if ( !nd ) {
    k = 0;
    return -1;
  }
 
  int res = kth_to_last(nd->next(), target, k);
  ++k;
  if ( k == target ) {
    return nd->data();
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
  
  std::cout << "getting result: ";
  int target, k;
  while (std::cin >> target) { 
   int res = kth_to_last(slinked_list.head(), target, k);
   std::cout << "result is " << res << std::endl;
  }
}