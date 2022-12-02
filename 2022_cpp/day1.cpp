#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    std::vector<int> data{};

    int current{ 0 };
    std::string line{};
    while(std::getline(std::cin, line)) {
        if(line.length() > 0) {
            current += std::stoi(line);
        } else {
            data.push_back(current);
            current = 0;
        }
    }

    std::sort(data.rbegin(), data.rend());

    std::cout << data[0] << '\n';
    std::cout << data[0] + data[1] + data[2] << '\n';
}