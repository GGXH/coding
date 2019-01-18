#include "sll.h"

sll::~sll() {
  node* nd = d_head;
  while ( nd != nullptr ) {
    node* ndn = nd->next();
    delete nd;
    nd = ndn;
  }
}

void sll::insertAfter(int key, int data) {
  node* nd = d_head;
  node* nnd = new node(data);
  while ( nd->data() != key ) {
    nd = nd->next();
  }
  
  nnd->setNext(nd->next());
  nd->setNext(nnd);
  ++d_size;
}

void sll::insertBefore(int key, int data) {
  node* nd = d_head;
  node* nnd = new node(data);
  
  if ( nd->data() == key ) {
    nnd->setNext(d_head);
    d_head = nnd;
    ++d_size;
    return ;
  }
  
  while ( nd->next() != nullptr ) {
    if ( nd->next()->data() == key ) {
      nnd->setNext(nd->next());
      nd->setNext(nnd);
      ++d_size;
      return ;
    }
  }
}
    
void sll::del(int data) {
  node* nd = d_head;
  if ( nd->data() == data ) {
    d_head = d_head->next();
    delete nd;
    --d_size;
    return ;
  }
  
  while ( nd->next() != nullptr ) {
    if ( nd->next()->data() == data ) {
      node* nnd = nd->next();
      nd->setNext(nnd->next());
      delete nnd;
      --d_size;
      return ;
    }
  }
}