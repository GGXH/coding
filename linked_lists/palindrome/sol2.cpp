#include "sll.h"

#include <iostream>
#include <vector>


node* reverseLinkedList(node* nd) {
  if ( !nd ) return nd;
  node* tail = nd;
  node* head = nd;
  
  while ( tail->next() ) {
    node* curr = tail->next();
    tail->setNext(curr->next());
    curr->setNext(head);
    head = curr;
  }
  return head;
}


bool isPalindrome(node* nd) {
  node* slow = nd;
  node* fast = nd;
  
  while ( fast && fast->next() ) {
     slow = slow->next();
     fast = fast->next()->next();
  }
  
  if ( fast ) {
    slow = slow->next();
  }
  
  slow = reverseLinkedList(slow);
  
  fast = nd;
  while ( fast && slow ) {
    if ( fast->data() != slow->data() ) {
      return false;
    }
    fast = fast->next();
    slow = slow->next();
  }
  
  return true;
}
  

int main() {
  sll slinked_list;
  std::vector<int> value{1, 2, 3, 2, 1};
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
