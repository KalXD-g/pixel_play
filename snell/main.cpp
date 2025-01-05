#include <iostream>
#include <cmath>
#include <opencv2/opencv.hpp>
#include <map>
#include <chrono> // Include chrono header

using namespace std;
using namespace cv;

int main() {
    // Color Map
    std::map<int, Vec3b> color_map = {
        {1, Vec3b(0, 0, 255)},    // Red
        {2, Vec3b(0, 155, 255)},  // Orange
        {3, Vec3b(0, 255, 255)},  // Yellow
        {4, Vec3b(0, 255, 0)},    // Green
        {5, Vec3b(255, 0, 0)},    // Blue
        {6, Vec3b(255, 0, 255)}   // Purple
    };

    cout << "1->Red\n" 
         << "2->Orange\n" 
         << "3->Yellow\n" 
         << "4->Green\n" 
         << "5->Blue\n" 
         << "6->Purple\n";

    // Input
    int light_color;
    float incident_angle_deg;
    float upper_refractive_index;
    float lower_refractive_index;

    cout << "Choose the color of light::";
    cin >> light_color; 
    cout << "Incident angle (degrees)::";
    cin >> incident_angle_deg;
    cout << "Refractive Index of Upper medium::";
    cin >> upper_refractive_index;
    cout << "Refractive Index of Lower medium::";
    cin >> lower_refractive_index;

}