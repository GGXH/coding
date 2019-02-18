#include "sll.h"

#include <iostream>
#include <vector>

unsigned int linkedListSize(node* nd) {
  unsigned int size = 0;
  while ( nd ) {
     ++size;
     nd = nd->next();
  }
  return size;
}

node* addNode(node* nd1, node* nd2, int& add) {
  int res = nd1->data() +add;
  if ( nd2 != nullptr ) {
     res +=  nd2->data();
  }
  node* resND = new node(res % 10, res);
  add = res / 10;
  return resND;
}

node* sumListsNode(node* nd1, node* nd2, unsigned int k, int& add) {
  node* resND, *addcurrent;
  
  if ( nd1->next() == nullptr && nd2->next() == nullptr ) {
    return addNode(nd1, nd2, add);
  }
  
  if ( k > 0 ) {
    resND = sumListsNode(nd1->next(), nd2, --k, add);
    addcurrent = addNode(nd1, nullptr, add);
    addcurrent->setNext(resND);
  } else {
    resND = sumListsNode(nd1->next(), nd2->next(), k, add);
    addcurrent = addNode(nd1, nd2, add);
    addcurrent->setNext(resND);
  }
  return addcurrent;
}

node* sumLists(node* nd1, node* nd2) {
   unsigned int size1 = linkedListSize(nd1);
   unsigned int size2 = linkedListSize(nd2);
   if ( size1 < size2 ) {
      return sumLists(nd2, nd1);
   }
   
   int add = 0;
   node* head = sumListsNode(nd1, nd2, size1 - size2, add);
   if ( add == 1 ) {
     node* tmp = new node(add, 0);
     tmp->setNext(head);
     head = tmp;
   }
   
   return head;
}


int main() {
  sll slinked_list;
  sll slinked_list1;
  std::vector<int> value{1, 2, 3, 2, 3};
  std::vector<int> value1{9, 2, 1};
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
  
  for (auto& it : value1) {
    std::cout << key << std::endl;
    if (key == 0) {
      slinked_list1.insertHead(it, key);
    } else {
      slinked_list1.insertLast(it, key);
    }
    ++key;
  }
  
  node* nd = slinked_list.head();
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
   
  nd = slinked_list1.head();
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
   
  nd = slinked_list.head();
  node* nd1 = slinked_list1.head();
  nd = sumLists(nd, nd1);
  
  std::cout << "getting result: ";
  while (nd) {
    std::cout << nd->data() << " ";
    nd = nd->next();
  }
  std::cout << std::endl;
}