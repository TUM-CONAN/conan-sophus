from conans import ConanFile, CMake, tools
import os


class SophusConan(ConanFile):
    name = "sophus"
    version = "1.0.0"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"

    options = {
    }

    default_options = (
        )

    exports = ["CMakeLists.txt",]

    url="http://github.com/ulricheck/conan-sophus"
    license="as is .."
    description="Sophus SO3 Math library"
    
    requires = (
        "eigen/3.3.7@camposs/stable",
        )

    scm = {
        "type": "git",
        "subfolder": "sources",
        "url": "https://github.com/strasdat/Sophus.git",
        "revision": "v%s" % version,
    }

    def _cmake_configure(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_EXAMPLES'] = 'OFF'
        cmake.definitions['BUILD_TESTS'] = 'OFF'
        cmake.configure()
        return cmake


    def build(self):
        """ Define your project building. You decide the way of building it
            to reuse it later in any other project.
        """
        cmake = self._cmake_configure()
        cmake.build()

    def package(self):
        """ Define your conan structure: headers, libs, bins and data. After building your
            project, this method is called to create a defined structure:
        """
        cmake = self._cmake_configure()
        cmake.install()
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
