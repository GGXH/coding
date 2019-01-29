#include "sll.h"

#include <iostream>
#include <vector>

int kth_to_last(sll& slinked_list, int k) {
  node* nd = slinked_list.head();
  
  int s = slinked_list.size();
  
  for(auto i = 0; i < s - k; ++i) {
    nd = nd->next();
  }
  
  return nd->data();
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
  while (std::cin >> k) { 
   int res = kth_to_last(slinked_list, k);
   std::cout << "result is " << res << std::endl;
  }
}