#ifndef SLL_H
#define SLL_H

class node {
 public:
  node(int d) : d_data(d), d_next(nullptr) {}
  ~node() { delete d_next; }
  
  node* next() { return d_next; }
  int data() { return d_data; }
  void setNext(node* nn) { d_next = nn; }

 private:
  int d_data;
  node* d_next;
};


class sll {
 public:
  sll() : d_head(nullptr), d_last(nullptr), d_size(0) {}
   
  ~sll();
  
  node* head() { return d_head; }
  node* last() { return d_last; }
  unsigned size() { return d_size; }
  
  void insertAfter(int key, int data);
  void insertBefore(int key, int data);
  void del(int data);

 private:
  node* d_head;
  node* d_last;
  
  unsigned d_size;
};

#endif