// License: Apache 2.0. See LICENSE file in root directory.
// Copyright(c) 2019 Intel Corporation. All Rights Reserved.

#include <librealsense2/rs.hpp> // Include RealSense Cross Platform API
#include <iostream>             // for cout
#include <Windows.h>
#include <windows.media.speechrecognition.h>
#include <roapi.h>
#include <wrl.h>



using namespace ABI::Windows::Media::SpeechRecognition;
using namespace Microsoft::WRL;
using namespace Microsoft::WRL::Wrappers;

// Hello RealSense example demonstrates the basics of connecting to a RealSense device
// and taking advantage of depth data
int main(int argc, char * argv[]) try {

    //// Create a Pipeline - this serves as a top-level API for streaming and processing frames
    //rs2::pipeline p;

    //// Configure and start the pipeline
    //p.start();

    //while (true)
    //{
    //    // Block program until frames arrive
    //    rs2::frameset frames = p.wait_for_frames();

    //    // Try to get a frame of a depth image
    //    rs2::depth_frame depth = frames.get_depth_frame();

    //    // Get the depth frame's dimensions
    //    int width = depth.get_width();
    //    int height = depth.get_height();

    //    float min_z_left = 10;
    //    float min_z_right = 10;
    //    float threshold_z = 0.5;
    //    int min_x_left = width;
    //    //int min_y_left = height;
    //    int min_x_right = width;
    //    //int min_y_right = height;
    //    //int left_x = 100;
    //    for (int x = 0; x < width/2; x = x + 10) {
    //        for (int y = 0; y < height; y = y + 10) {
    //            float z = depth.get_distance(x, y);
    //            if (z != 0 && z < min_z_left) {
    //                min_z_left = z;
    //                min_x_left = x;
    //                //min_y_left = y;
    //            }
    //        }
    //    }
    //    
    //    for (int x = width / 2; x < width; x = x + 10) {
    //        for (int y = 0; y < height; y = y + 10) {
    //            float z = depth.get_distance(x, y);
    //            if (z != 0 && z < min_z_right) {
    //                min_z_right = z;
    //                min_x_right = x;
    //                //min_y_right = y;
    //            }
    //        }
    //    }
    //    if (min_z_left < threshold_z) {
    //            std::cout << "Object on the Left in " << min_z_left << " meters \r\n";
    //        //else {
    //            //std::cout << "Object on the Front in " << z << " meters \r";
    //        //}
    //            if (min_z_left < .5 && min_z_left >= .4) {
    //                Beep(500, 200);
    //                Sleep(1000);
    //            }
    //            else if (min_z_left < .4 && min_z_left >= .3) {
    //                Beep(500, 200);
    //                Sleep(500);
    //            }
    //            else if (min_z_left < .3 && min_z_left >= .2) {
    //                Beep(500, 200);
    //                Sleep(100);
    //            }
    //            else if (min_z_left < .2 && min_z_left >= .1) {
    //                Beep(500, 200);
    //                Sleep(20);
    //            }
    //            else {
    //                Beep(500, 200);
    //                Sleep(0);
    //            }
    //    }
    //    if (min_z_right < threshold_z) {
    //            std::cout << "Object on the Right in " << min_z_right << " meters\r\n";
    //        //else {
    //            //std::cout << "Object on the Front in " << z << " meters \r";
    //        //}
    //            if (min_z_right < .5 && min_z_right >= .4) {
    //                Beep(1000, 200);
    //                Sleep(1000);
    //            }
    //            else if (min_z_right < .4 && min_z_right >= .3) {
    //                Beep(1000, 200);
    //                Sleep(500);
    //            }
    //            else if (min_z_right < .3 && min_z_right >= .2) {
    //                Beep(1000, 200);
    //                Sleep(100);
    //            }
    //            else if (min_z_right < .2 && min_z_right >= .1) {
    //                Beep(1000, 200);
    //                Sleep(20);
    //            }
    //            else {
    //                Beep(1000, 200);
    //                Sleep(0);
    //            }
    //    }
    //    
    //    // Distance from the camera to the object in the left of the image
    //     //std::cout << min_x << " " << min_y <<  " " << min_z << std::endl;


    //    float dist_to_left = depth.get_distance(width / 6, height / 2);

    //    // Distance from the camera to the object in the right of the image
    //    float dist_to_right = depth.get_distance(width * 5 / 6, height / 2);

    //    // Query the distance from the camera to the object in the center of the image
    //    float dist_to_center = depth.get_distance(width / 2, height / 2);

    //    // Print the distance
    //    //std::cout << "The camera is facing an object on the center " << dist_to_center << " meters away \r";
    //    //std::cout << "The camera is facing an object on the left " << dist_to_left << " metters away \r";
    //    //std::cout << "The camera is facing an object on the right " << dist_to_right << " metters away \r";

    //    
    //}

    HRESULT hr = RoInitialize(RO_INIT_MULTITHREADED);
    if (FAILED(hr))
        return hr;

    ComPtr<IInspectable> instance;
    ComPtr<ISpeechRecognizer> recognizer;
    hr = RoActivateInstance(HStringReference(L"Windows.Media.SpeechRecognition.SpeechRecognizer").Get(), &instance);
    if (FAILED(hr))
        return hr;

    hr = instance.As(&recognizer);
    if (FAILED(hr))
        return hr;

    // do stuff with recognizer

    RoUninitialize();

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
