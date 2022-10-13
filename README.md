# glfwpp-conan
A basic Conan package for the glfw-pp library

## How to install the package
```
git clone https://github.com/Ahajha/glfwpp-conan.git
conan create glfwpp-conan latest@<desired-user>/<desired-channel>
```

(I may look into getting a remote for this in the future, or uploading to conan-center-index directly)

Using the package: (Basic CMake example)

conanfile.txt:
```
[requires]
glfwpp/latest@<desired-user>/<desired-channel>

[generators]
CMakeDeps
CMakeToolchain
```

CMakeLists.txt:
```cmake
cmake_minimum_required(VERSION 3.15)

project(glfwpp-conan-test CXX)

find_package(glfwpp REQUIRED)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE glfwpp::glfwpp)
target_compile_features(main PRIVATE cxx_std_17)
```
