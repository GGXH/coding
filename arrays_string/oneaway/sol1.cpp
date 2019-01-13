#include <iostream>
#include <string>
#include <vector>

bool oneaway(const std::string& str1, const std::string& str2) {
  if (str1.size() < str2.size()) {
    return oneaway(str2, str1);
  }
  
  auto len_diff = str1.size() - str2.size();
  
  if (len_diff > 1) {
    return false;
  }
  
  unsigned allowed_diff = 1;
  
  std::string::size_type i = 0;
  std::string::size_type j = 0;
   
  for(; i < str1.size(); ++i, ++j) {
    if (str1[i] == str2[j]) {
      continue;
    } else {
      if ( allowed_diff == 0 ) {
        return false;
      } else {
        j -= len_diff;
        --allowed_diff;
      }
    }
  }
  return true;
}

int main() {
  std::vector<std::vector<std::string>> test_list{{"pale", "ple"}, {"pale", "ple"}, {"pales", "pale"}, {"pale", "bale"}, {"bake", "pale"}};
  
  for(auto& tl: test_list) {
    std::cout << tl[0] << " " << tl[1] << " ";
    std::string res;
    if (oneaway(tl[0], tl[1])) {
      res = "true";
    } else {
      res = "false";
    }
    std::cout << res << std::endl;
  }
  
  return 0;
}