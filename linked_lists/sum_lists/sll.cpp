#include "sll.h"

#include <iostream>

sll::~sll() {
  node* nd = d_head;
  while ( nd != nullptr ) {
    node* ndn = nd->next();
    delete nd;
    nd = ndn;
  }
}

void sll::insertHead(int data, int key) {
  node* nd = new node(data, key);
  if (d_head) {
    nd->setNext(d_head->next());
  } else {
    d_last = nd;
  }
  d_head = nd;
  ++d_size;
}

void sll::insertAfter(int key, int data, int nkey) {
  node* nd = d_head;
  node* nnd = new node(data, nkey);
  while ( nd->key() != key ) {
    nd = nd->next();
  }
  
  nnd->setNext(nd->next());
  nd->setNext(nnd);
  ++d_size;
}

void sll::insertBefore(int key, int data, int nkey) {
  node* nd = d_head;
  node* nnd = new node(data, nkey);
  
  if ( nd->key() == key ) {
    nnd->setNext(d_head);
    d_head = nnd;
    ++d_size;
    return ;
  }
  
  while ( nd->next() != nullptr ) {
    if ( nd->next()->key() == key ) {
      nnd->setNext(nd->next());
      nd->setNext(nnd);
      ++d_size;
      return ;
    }
  }
}

void sll::insertLast(int data, int key) {
  node* nd = new node(data, key);
  if ( !d_last && !d_head ) {
   d_head = nd;
   d_last = nd;
  } else {
   d_last->setNext(nd);
   d_last = nd;
  }
  ++d_size;
}
    
void sll::del(int key) {
  node* nd = d_head;
  if ( nd->key() == key ) {
    d_head = d_head->next();
    delete nd;
    --d_size; 
    return ;
  }
  
  while ( nd->next() != nullptr ) {
    if ( nd->next()->key() == key ) {
      node* nnd = nd->next();
      nd->setNext(nnd->next());
      //
     // std::cout << nnd->data() << " " << nd->data() << " " << nd->next()->data() << std::endl;
      //
      delete nnd;
      --d_size;
      return ;
    }
    nd = nd->next();
  }
}