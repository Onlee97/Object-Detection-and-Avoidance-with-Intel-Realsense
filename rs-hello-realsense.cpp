// License: Apache 2.0. See LICENSE file in root directory.
// Copyright(c) 2019 Intel Corporation. All Rights Reserved.

#include <librealsense2/rs.hpp> // Include RealSense Cross Platform API
#include <iostream>             // for cout



// Hello RealSense example demonstrates the basics of connecting to a RealSense device
// and taking advantage of depth data
int main(int argc, char * argv[]) try {

    // Create a Pipeline - this serves as a top-level API for streaming and processing frames
    rs2::pipeline p;

    // Configure and start the pipeline
    p.start();

    while (true)
    {
        // Block program until frames arrive
        rs2::frameset frames = p.wait_for_frames();

        // Try to get a frame of a depth image
        rs2::depth_frame depth = frames.get_depth_frame();

        // Get the depth frame's dimensions
        int width = depth.get_width();
        int height = depth.get_height();

        float min_z = 0.1;
        float threshold_z = 0.5;
        int min_x = 0;
        int min_y = 0;
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                float z = depth.get_distance(x, y);
                if (z != 0 && z < threshold_z) {
                    min_x = x;
                    min_y = y;
                    if (x < width / 3) {
                        std::cout << "Object on the Left in " << z << " meters \r";
                    }
                    else if (x > width * 2 / 3) {
                    
                        std::cout << "Object on the Right in " << z << " meters \r";
                    }
                    else {
                        std::cout << "Object on the Front in " << z << " meters \r";
                    }
                }
            }
        }
        
        // Distance from the camera to the object in the left of the image
         //std::cout << min_x << " " << min_y <<  " " << min_z << std::endl;


        float dist_to_left = depth.get_distance(width / 6, height / 2);

        // Distance from the camera to the object in the right of the image
        float dist_to_right = depth.get_distance(width * 5 / 6, height / 2);

        // Query the distance from the camera to the object in the center of the image
        float dist_to_center = depth.get_distance(width / 2, height / 2);

        // Print the distance
        //std::cout << "The camera is facing an object on the center " << dist_to_center << " meters away \r";
        //std::cout << "The camera is facing an object on the left " << dist_to_left << " metters away \r";
        //std::cout << "The camera is facing an object on the right " << dist_to_right << " metters away \r";
    }

    return EXIT_SUCCESS;
}
catch (const rs2::error & e)
{
    std::cerr << "RealSense error calling " << e.get_failed_function() << "(" << e.get_failed_args() << "):\n    " << e.what() << std::endl;
    return EXIT_FAILURE;
}
catch (const std::exception& e)
{
    std::cerr << e.what() << std::endl;
    return EXIT_FAILURE;
}
