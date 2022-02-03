#include <iostream>
#include <vector>
#include <string>
#include <filesystem>

int get_size(std::string path){
    auto total = 0;
    
    for(const auto& elem : std::filesystem::directory_iterator(path)){
        if(std::filesystem::is_directory(elem.path()))
            total += get_size(elem.path());
        else
            total += std::filesystem::file_size(elem.path());
    }
    return total;
}

int main(){
    auto total_size = get_size(std::filesystem::current_path());
    std::cout << total_size << " bytes" << std::endl;
}