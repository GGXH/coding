#include <ctype.h>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

bool Palinedrome_permutation(const std::string& str) {
  int char_a = 'a';
  unsigned marker = 0;
  for(auto& s : str) {
    if (s == ' ') {
      continue;
    }
    int c = tolower(s);
    marker ^= 1 << (c - char_a);
  }
  
  return marker == 0 || !( marker & marker - 1);
}

int main() {
  std::vector<std::string> test_list{"Tact Coa", "Tact Coaw", "Tact wCoaw"};
  
  for(auto& s : test_list) {
    std::cout << s << " ";
    if (Palinedrome_permutation(s)) {
      std::cout << "True";
    } else {
      std::cout << "False";
    }
    std::cout << std::endl;
  }
  return 0;
}