#include<iostream>
#include<cmath>
#include<opencv2/opencv.hpp>
#include<tuple>
#include<chrono>
#include<map>
#include<string>

using namespace std;
using namespace cv;


//TODO The colors are messed up. Change later
map<int, tuple<int, int, int>> color_map = {
    {1, {0, 0, 255}},     // Red
    {2, {0, 155, 255}},   // Orange
    {3, {0, 255, 255}},   // Yellow
    {4, {0, 255, 0}},     // Green
    {5, {255, 0, 0}},     // Blue
    {6, {255, 0, 255}}    // Purple
};

int calculate_y(double angle, const Point& upper_reference_point, const Point& centre_point) {
    double length = (upper_reference_point.y - centre_point.y) * tan(angle);
    return static_cast<int>(length);
}

int main() {
    cout << R"(
1->Red
2->Orange
3->Yellow
4->Green
5->Blue
6->Purple
)";

    int light_color;
    cout << "Choose the color of light: ";
    cin >> light_color;

    double incident_angle_deg;
    cout << "Incident angle (degrees): ";
    cin >> incident_angle_deg;

    double upper_refractive_index, lower_refractive_index;
    cout << "Refractive Index of Upper medium: ";
    cin >> upper_refractive_index;
    cout << "Refractive Index of Lower medium: ";
    cin >> lower_refractive_index;

    Point centre_point(300, 300);
    Point upper_reference_point(300, 0);
    Point lower_reference_point(300, 600);

    auto start = chrono::high_resolution_clock::now();

    double incident_angle_rad = incident_angle_deg * M_PI / 180.0;
    double refraction_angle = asin((upper_refractive_index / lower_refractive_index) * sin(incident_angle_rad));

    Point calculated_point_incident_ray(
        upper_reference_point.x + calculate_y(incident_angle_rad, upper_reference_point, centre_point),
        upper_reference_point.y
    );

    Point calculated_point_refracted_ray(
        lower_reference_point.x + calculate_y(refraction_angle, lower_reference_point, centre_point),
        lower_reference_point.y
    );

    Point calculated_point_reflected_ray(
        upper_reference_point.x - calculate_y(incident_angle_rad, upper_reference_point, centre_point),
        upper_reference_point.y
    );

    Mat screen = Mat::zeros(600, 600, CV_8UC3);

    for (int x = 0; x < 600; ++x) {
        for (int y = 0; y < 600; ++y) {
            if (x > 300) {
                screen.at<Vec3b>(x, y) = Vec3b(34, 42, 51);
            }
        }
    }

    line(screen, Point(300, 0), Point(300, 600), Scalar(105, 105, 105), 1);
    line(screen, Point(0, 300), Point(600, 300), Scalar(255, 255, 255), 1);

    auto color = Scalar(get<2>(color_map[light_color]), get<1>(color_map[light_color]), get<0>(color_map[light_color]));
    line(screen, centre_point, calculated_point_incident_ray, color, 1);
    line(screen, centre_point, calculated_point_reflected_ray, color, 1);
    line(screen, centre_point, calculated_point_refracted_ray, color, 1);

    string u_text = "n1=" + to_string(upper_refractive_index);
    string l_text = "n2=" + to_string(lower_refractive_index);
    string r_text = to_string(refraction_angle * 180.0 / M_PI);
    string i_text = to_string(incident_angle_deg);

    putText(screen, u_text, Point(80, 250), FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 255, 255), 1);
    putText(screen, l_text, Point(80, 350), FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 255, 255), 1);
    putText(screen, "Angle of Refraction=", Point(50, 500), FONT_HERSHEY_SIMPLEX, 0.35, Scalar(255, 255, 255), 1);
    putText(screen, r_text, Point(50, 520), FONT_HERSHEY_SIMPLEX, 0.35, Scalar(0, 255, 255), 1);
    putText(screen, "Angle of Incidence=", Point(50, 100), FONT_HERSHEY_SIMPLEX, 0.35, Scalar(255, 255, 255), 1);
    putText(screen, i_text, Point(50, 120), FONT_HERSHEY_SIMPLEX, 0.35, Scalar(0, 255, 255), 1);

    putText(screen, "X", Point(590, 290), FONT_HERSHEY_SIMPLEX, 0.35, Scalar(255, 255, 255), 1);
    putText(screen, "-X", Point(10, 290), FONT_HERSHEY_SIMPLEX, 0.35, Scalar(255, 255, 255), 1);
    putText(screen, "Y", Point(310, 10), FONT_HERSHEY_SIMPLEX, 0.35, Scalar(255, 255, 255), 1);
    putText(screen, "-Y", Point(310, 590), FONT_HERSHEY_SIMPLEX, 0.35, Scalar(255, 255, 255), 1);

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_time = end - start;

    imshow("Snell's Law Visualizer", screen);

    while (true) {
        if (waitKey(1) == 32) break; // Space key to exit
    }

    cout << "Elapsed time: " << elapsed_time.count() << " seconds" << endl;

    destroyAllWindows();

    return 0;
}