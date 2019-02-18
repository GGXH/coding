#include "sll.h"

#include <iostream>
#include <vector>

class res {
public:
  res(node* nd, bool res) : d_nd(nd), d_res(res) {}
  
  node* getnd() { return d_nd; }
  bool getres() { return d_res; }
  
  void setnd(node* nd) { d_nd = nd; }
  void setres(bool res) { d_res = res; }
  
private:
  node* d_nd;
  bool d_res;
};

unsigned int linkedListSize(node* nd) {
  unsigned int res = 0;
  while ( nd != nullptr ) {
     ++res;
     nd = nd->next();
  }
  return res;
}

res* isPalindrome(node* nd, const int& size) {
  if ( nd == nullptr || size <= 0 ) {
     return new res(nd, true);
  } else if ( size == 1 ) {
     return new res(nd->next(), true);
  }
  
  res* Res = isPalindrome(nd->next(), size - 2);
  
  if ( !Res->getres() ) {
     return Res;
  }
  
  if ( Res->getnd()->data() == nd->data() ) {
     Res->setnd(Res->getnd()->next());
     return Res;
  }
  
  Res->setres(false);
  return Res;
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
  int size = linkedListSize(nd);
  if ( isPalindrome(nd, size)->getres() ) {
     std::cout << "Palindrome";
  } else {
     std::cout << "is not";
  }
  
  std::cout << std::endl;
}
