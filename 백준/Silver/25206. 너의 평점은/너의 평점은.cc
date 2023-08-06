#include <iostream>

int main()
{
    float gradesXsubjectgrade_sum = 0;
    int grade_sum = 0;
    
    for (int i=0; i<20; i++)
    {
        std::string subject_name, grade, subject_grade;
        std::cin >> subject_name >> grade >> subject_grade;
        
        float number_subject_grade = 0;
        if (subject_grade == "A+") number_subject_grade = 4.5;
        else if (subject_grade == "A0") number_subject_grade = 4.0;
        else if (subject_grade == "B+") number_subject_grade = 3.5;
        else if (subject_grade == "B0") number_subject_grade = 3.0;
        else if (subject_grade == "C+") number_subject_grade = 2.5;
        else if (subject_grade == "C0") number_subject_grade = 2.0;
        else if (subject_grade == "D+") number_subject_grade = 1.5;
        else if (subject_grade == "D0") number_subject_grade = 1.0;
        else if (subject_grade == "F") number_subject_grade = 0.0;
        
        gradesXsubjectgrade_sum += std::stoi(grade) * number_subject_grade;
        if (subject_grade != "P") grade_sum += std::stoi(grade);
    }

    std::cout << gradesXsubjectgrade_sum / grade_sum;

    return 0;
}