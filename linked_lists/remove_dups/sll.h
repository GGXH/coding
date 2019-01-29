#ifndef SLL_H
#define SLL_H

class node {
 public:
  node(int d, int k) : d_data(d), d_key(k), d_next(nullptr) {}
  ~node() { }
  
  node* next() { return d_next; }
  int data() { return d_data; }
  int key() { return d_key; }
  void setNext(node* nn) { d_next = nn; }

 private:
  int d_data;
  int d_key;
  node* d_next;
};


class sll {
 public:
  sll() : d_head(nullptr), d_last(nullptr), d_size(0) {}
   
  ~sll();
  
  node* head() { return d_head; }
  node* last() { return d_last; }
  unsigned size() { return d_size; }
  
  void insertHead(int data, int key);
  void insertAfter(int key, int data, int nkey);
  void insertBefore(int key, int data, int nkey);
  void insertLast(int data, int key);
  void del(int key);

 private:
  node* d_head;
  node* d_last;
  
  unsigned d_size;
};

#endif