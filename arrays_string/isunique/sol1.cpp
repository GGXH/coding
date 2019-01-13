#include <iostream>
#include <string>
#include <vector>

bool isunqiue(const std::string& str) {
  int a_ord = 'a';
  int res = 0;
  for (auto& c : str) {
    int b = c;
    b = 1 << b;
    if (res & b) {
      return false;
    }
    res |= b;
  }
  return true;
}


int main() {
  std::vector<std::string> test_str{"aaaaa", "abcdea", "abcdefg"};
  for(auto& s : test_str) {
    std::cout << s << " ";
    if (isunqiue(s)) {
      std::cout << "unique";
    } else {
      std::cout << "not unique";
    }
    std::cout << std::endl;
  }
  return 0;
}