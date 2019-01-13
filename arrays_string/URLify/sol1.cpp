#include <iostream>
#include <string>
#include <string.h>
#include <vector>

std::string urlify(const std::string& str) {
  unsigned space_cnt = 0;
  
  for (auto& s : str) {
    if ( s == ' ' ) {
      ++space_cnt;
    }
  }
  
  std::string new_str;
  new_str.resize(str.size() + 2 * space_cnt, ' ');
   
  int m = str.size() - 1;
  int new_m = new_str.size() - 1;
  for (; m >= 0; --m, --new_m) {
    if (str[m] == ' ') {
      new_str[new_m] = '0';
      --new_m;
      new_str[new_m] = '2';
      --new_m;
      new_str[new_m] = '%';
    } else {
      new_str[new_m] = str[m];
    }
  }
  return new_str;
}

int main() {
  std::vector<std::string> test_str{"a  ", " a  ", "a b  ", "  bc    "};
 
  for(auto& s : test_str){
    std::cout << s << " ";
    std::cout << urlify(s) << std::endl;
  }
  
  return 0;
}