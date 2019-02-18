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

bool isPalindrome(node* nd) {
  unsigned int size = linkedListSize(nd);
  std::vector<int> data(size/2);
  node* tmp = nd;
  for(int i = 0; i < size / 2; ++i) {
    data[i] = tmp->data();
    tmp = tmp->next();
  }
  
  if ( size % 2 == 1 ) {
     tmp = tmp->next();
  }
  for ( int i = size / 2 - 1; i >= 0; --i, tmp = tmp->next()) {
     if ( data[i] != tmp->data() ) {
        return false;
     }
   }
   
   return true;
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
  
  node* nd = slinked_list.head();
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
   

  nd = slinked_list.head();
  if ( isPalindrome(nd) ) {
     std::cout << "Palindrome";
  } else {
     std::cout << "is not";
  }
  
  std::cout << std::endl;
}
