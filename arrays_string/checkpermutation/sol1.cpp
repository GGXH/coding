#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

bool check_permutation(const std::string& str1, const std::string& str2) {
  std::unordered_map<char, unsigned> res;
  for(auto& s : str1) {
    if ( res.find(s) == res.end() ) {
      res[s] = 1;
    } else {
      ++res[s];
    }
  }
  
  for(auto& s : str2) {
    if ( res.find(s) == res.end() || res[s] == 0 ) {
      return false;
    } else {
      --res[s];
    }
  }
  
  return true;
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