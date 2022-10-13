from conan import ConanFile
from conan.tools.files import copy
from conan.tools.scm import Git
from conan.tools.layout import basic_layout
import os


required_conan_version = ">=1.52.0"


class PackageConan(ConanFile):
    name = "glfwpp"
    description = "GLFW C++ Wrapper - thin, modern, C++17, header-only GLFW wrapper"
    author = "janekb04"
    license = "MIT"
    url = "https://github.com/janekb04/glfwpp"
    topics = ("glfw", "raii", "wrapper", "header-only")
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True

    def layout(self):
        basic_layout(self, src_folder="src")

    def requirements(self):
        self.requires("glfw/3.3.6")
        # TODO imgui support?

    def package_id(self):
        self.info.clear()

    def source(self):
        git = Git(self)
        sources = self.conan_data["sources"][self.version]
        git.clone(url=sources["url"], target=self.source_folder)
        git.checkout(commit=sources["commit"])

    def build(self):
        pass

    # copy all files to the package folder
    def package(self):
        copy(self, pattern="LICENSE", dst=os.path.join(self.package_folder, "licenses"), src=self.source_folder)
        copy(
            self,
            pattern="*.h",
            dst=os.path.join(self.package_folder, "include"),
            src=os.path.join(self.source_folder, "include"),
        )

    def package_info(self):
        # folders not used for header-only
        self.cpp_info.bindirs = []
        self.cpp_info.frameworkdirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
