#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

bool check_permutation(std::string str1, std::string str2) {
  std::sort(str1.begin(), str1.end());
  std::sort(str2.begin(), str2.end());
   
  return str1 == str2;
}

int main() {
  std::vector<std::string> test_str{"abc", "cba", "eeb"};
  
  std::cout << test_str[0] << " " << test_str[1] << " ";
  if (check_permutation(test_str[0], test_str[1])) {
    std::cout << "permutation";
  } else {
    std::cout << "not permutation";
  }
  std::cout << std::endl;
  
  std::cout << test_str[1] << " " << test_str[2] << " ";
  if (check_permutation(test_str[1], test_str[2])) {
    std::cout << "permutation";
  } else {
    std::cout << "not permutation";
  }
  std::cout << std::endl;
  
  return 0;
}