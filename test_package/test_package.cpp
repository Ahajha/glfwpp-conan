#include <glfwpp/glfwpp.h>

int main() {
  [[maybe_unused]] glfw::GlfwLibrary library = glfw::init();

  auto monitor = glfw::getPrimaryMonitor();

  [[maybe_unused]] auto window =
      glfw::Window(640, 480, "Window name", &monitor);
}
