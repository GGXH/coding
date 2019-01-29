#include "sll.h"

#include <iostream>
#include <unordered_map>
#include <vector>


void remove_dups(sll& slinked_list) {
  node* nd = slinked_list.head();
  
  std::unordered_map<int, std::vector<int>> res;
  
  while (nd) {
   int k = nd->data();
   if (res.find(k) == res.end() ) {
     std::vector<int> key_list{nd->key()};
     res.insert(std::pair<int, std::vector<int>>(nd->data(), key_list));
   } else {
     res[nd->data()].push_back(nd->key());
   }
   nd = nd->next();
  }
  
  for (auto& it : res) {
     if ( it.second.size() > 1 ) {
       for (auto i = 1; i < it.second.size(); ++i) {
         slinked_list.del(it.second[i]);
       }
     }
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