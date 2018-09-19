#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class DirectShowBaseClassesConan(ConanFile):
    name = "directshowbaseclasses"
    version = "7.1A"
    description = "Microsoft DirectShow Base Classes are a set of C++ classes and utility functions designed for " \
                  "implementing DirectShow filters"
    url = "https://github.com/bincrafters/conan-directshowbaseclasses"
    homepage = "https://docs.microsoft.com/en-us/windows/desktop/directshow/directshow-base-classes"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = {"os": ["Windows"], "arch": ["x86", "x86_64"], "compiler": None, "build_type": None}
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    short_paths = True

    def source(self):
        source_url = "https://github.com/Microsoft/Windows-classic-samples/archive/master.zip"
        tools.get(source_url)
        os.rename('Windows-classic-samples-master', self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ['strmbasd' if self.settings.build_type == 'Debug' else 'strmbase',
                              'strmiids',
                              'winmm']
