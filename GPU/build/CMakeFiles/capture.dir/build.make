# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jetbot/Eye-for-Blind/GPU

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jetbot/Eye-for-Blind/GPU/build

# Include any dependencies generated for this target.
include CMakeFiles/capture.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/capture.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/capture.dir/flags.make

CMakeFiles/capture.dir/test.cpp.o: CMakeFiles/capture.dir/flags.make
CMakeFiles/capture.dir/test.cpp.o: ../test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jetbot/Eye-for-Blind/GPU/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/capture.dir/test.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/capture.dir/test.cpp.o -c /home/jetbot/Eye-for-Blind/GPU/test.cpp

CMakeFiles/capture.dir/test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/capture.dir/test.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jetbot/Eye-for-Blind/GPU/test.cpp > CMakeFiles/capture.dir/test.cpp.i

CMakeFiles/capture.dir/test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/capture.dir/test.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jetbot/Eye-for-Blind/GPU/test.cpp -o CMakeFiles/capture.dir/test.cpp.s

CMakeFiles/capture.dir/test.cpp.o.requires:

.PHONY : CMakeFiles/capture.dir/test.cpp.o.requires

CMakeFiles/capture.dir/test.cpp.o.provides: CMakeFiles/capture.dir/test.cpp.o.requires
	$(MAKE) -f CMakeFiles/capture.dir/build.make CMakeFiles/capture.dir/test.cpp.o.provides.build
.PHONY : CMakeFiles/capture.dir/test.cpp.o.provides

CMakeFiles/capture.dir/test.cpp.o.provides.build: CMakeFiles/capture.dir/test.cpp.o


# Object files for target capture
capture_OBJECTS = \
"CMakeFiles/capture.dir/test.cpp.o"

# External object files for target capture
capture_EXTERNAL_OBJECTS =

capture: CMakeFiles/capture.dir/test.cpp.o
capture: CMakeFiles/capture.dir/build.make
capture: /usr/local/lib/libopencv_gapi.so.4.1.1
capture: /usr/local/lib/libopencv_stitching.so.4.1.1
capture: /usr/local/lib/libopencv_aruco.so.4.1.1
capture: /usr/local/lib/libopencv_bgsegm.so.4.1.1
capture: /usr/local/lib/libopencv_bioinspired.so.4.1.1
capture: /usr/local/lib/libopencv_ccalib.so.4.1.1
capture: /usr/local/lib/libopencv_cudabgsegm.so.4.1.1
capture: /usr/local/lib/libopencv_cudafeatures2d.so.4.1.1
capture: /usr/local/lib/libopencv_cudaobjdetect.so.4.1.1
capture: /usr/local/lib/libopencv_cudastereo.so.4.1.1
capture: /usr/local/lib/libopencv_cvv.so.4.1.1
capture: /usr/local/lib/libopencv_dnn_objdetect.so.4.1.1
capture: /usr/local/lib/libopencv_dpm.so.4.1.1
capture: /usr/local/lib/libopencv_face.so.4.1.1
capture: /usr/local/lib/libopencv_freetype.so.4.1.1
capture: /usr/local/lib/libopencv_fuzzy.so.4.1.1
capture: /usr/local/lib/libopencv_hdf.so.4.1.1
capture: /usr/local/lib/libopencv_hfs.so.4.1.1
capture: /usr/local/lib/libopencv_img_hash.so.4.1.1
capture: /usr/local/lib/libopencv_line_descriptor.so.4.1.1
capture: /usr/local/lib/libopencv_quality.so.4.1.1
capture: /usr/local/lib/libopencv_reg.so.4.1.1
capture: /usr/local/lib/libopencv_rgbd.so.4.1.1
capture: /usr/local/lib/libopencv_saliency.so.4.1.1
capture: /usr/local/lib/libopencv_stereo.so.4.1.1
capture: /usr/local/lib/libopencv_structured_light.so.4.1.1
capture: /usr/local/lib/libopencv_superres.so.4.1.1
capture: /usr/local/lib/libopencv_surface_matching.so.4.1.1
capture: /usr/local/lib/libopencv_tracking.so.4.1.1
capture: /usr/local/lib/libopencv_videostab.so.4.1.1
capture: /usr/local/lib/libopencv_viz.so.4.1.1
capture: /usr/local/lib/libopencv_xfeatures2d.so.4.1.1
capture: /usr/local/lib/libopencv_xobjdetect.so.4.1.1
capture: /usr/local/lib/libopencv_xphoto.so.4.1.1
capture: /usr/local/lib/libopencv_shape.so.4.1.1
capture: /usr/local/lib/libopencv_datasets.so.4.1.1
capture: /usr/local/lib/libopencv_plot.so.4.1.1
capture: /usr/local/lib/libopencv_text.so.4.1.1
capture: /usr/local/lib/libopencv_dnn.so.4.1.1
capture: /usr/local/lib/libopencv_highgui.so.4.1.1
capture: /usr/local/lib/libopencv_ml.so.4.1.1
capture: /usr/local/lib/libopencv_phase_unwrapping.so.4.1.1
capture: /usr/local/lib/libopencv_cudacodec.so.4.1.1
capture: /usr/local/lib/libopencv_videoio.so.4.1.1
capture: /usr/local/lib/libopencv_cudaoptflow.so.4.1.1
capture: /usr/local/lib/libopencv_cudalegacy.so.4.1.1
capture: /usr/local/lib/libopencv_cudawarping.so.4.1.1
capture: /usr/local/lib/libopencv_optflow.so.4.1.1
capture: /usr/local/lib/libopencv_video.so.4.1.1
capture: /usr/local/lib/libopencv_ximgproc.so.4.1.1
capture: /usr/local/lib/libopencv_imgcodecs.so.4.1.1
capture: /usr/local/lib/libopencv_objdetect.so.4.1.1
capture: /usr/local/lib/libopencv_calib3d.so.4.1.1
capture: /usr/local/lib/libopencv_features2d.so.4.1.1
capture: /usr/local/lib/libopencv_flann.so.4.1.1
capture: /usr/local/lib/libopencv_photo.so.4.1.1
capture: /usr/local/lib/libopencv_cudaimgproc.so.4.1.1
capture: /usr/local/lib/libopencv_cudafilters.so.4.1.1
capture: /usr/local/lib/libopencv_imgproc.so.4.1.1
capture: /usr/local/lib/libopencv_cudaarithm.so.4.1.1
capture: /usr/local/lib/libopencv_core.so.4.1.1
capture: /usr/local/lib/libopencv_cudev.so.4.1.1
capture: CMakeFiles/capture.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jetbot/Eye-for-Blind/GPU/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable capture"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/capture.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/capture.dir/build: capture

.PHONY : CMakeFiles/capture.dir/build

CMakeFiles/capture.dir/requires: CMakeFiles/capture.dir/test.cpp.o.requires

.PHONY : CMakeFiles/capture.dir/requires

CMakeFiles/capture.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/capture.dir/cmake_clean.cmake
.PHONY : CMakeFiles/capture.dir/clean

CMakeFiles/capture.dir/depend:
	cd /home/jetbot/Eye-for-Blind/GPU/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jetbot/Eye-for-Blind/GPU /home/jetbot/Eye-for-Blind/GPU /home/jetbot/Eye-for-Blind/GPU/build /home/jetbot/Eye-for-Blind/GPU/build /home/jetbot/Eye-for-Blind/GPU/build/CMakeFiles/capture.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/capture.dir/depend

