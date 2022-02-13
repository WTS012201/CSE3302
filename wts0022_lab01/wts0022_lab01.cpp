//  William Sigala
//  CSE 3302
//  Lab 1
//  ID# 1001730022

//  compile: g++ --std=c++17 wts0022_lab01.cpp

//  Compile on school VM

/*
1)  Was one language easier or faster to write the code for this?  If so, describe in 
detail why, as in what about the language made that the case. 
    Python was the easiest language to write this in. Didn't have to deal with semicolons,
    types, brackets or blocks, and namespaces.

2)  Even though a language may not (e.g. FORTRAN) does not support recursion, 
describe how you could write a program to produce the same results without 
using recursion.  Would that approach have any limitations and if so, what would 
they be?  
    Instead of using recursion, you could just do it iterativly but it would require more work.
    Perhaps you could run a while loop that gets the size of all the files. 
    If it finds a subfolder, put it in a stack or queue. Open folder in stack
    or queue once there are no files left and repeat the process until they are empty.

    There are no apparent limitations with this approach. As far as resource use goes,
    the stack or queue would be negligible but it would require more memory than the
    recursive solution.
*/

#include <iostream>
#include <vector>
#include <string>
#include <filesystem>

int get_size(std::string path){
    auto total = 0;
    
    for(const auto& elem : std::filesystem::directory_iterator(path))
        if(std::filesystem::is_directory(elem.path()))
            total += get_size(elem.path());
        else
            total += std::filesystem::file_size(elem.path());
    return total;
}

int main(){
    auto total_size = get_size(std::filesystem::current_path());

    std::cout << total_size << " bytes" << std::endl;
}