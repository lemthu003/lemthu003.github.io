def main():
    # Define the grade point mapping
    grade_points = {
        "A+": 4.3, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0
    }

    # List of courses with grades and units
    courses_ug = [
        ("CHEM 31M", "B-", 5.00),
        ("CME 100", "A", 5.00),
        ("EMED 111A", "A", 5.00),
        ("PWR 1BRB", "A-", 4.00),

        ("BIO 84", "A", 4.00),
        ("COLLEGE 102", "A", 3.00),
        ("CS 103", "C-", 5.00),
        ("CS 106B", "A", 5.00),
        ("EMED 111B", "B+", 5.00),

        ("CHEM 33", "C", 5.00),
        ("COLLEGE 108", "A", 4.00),
        ("EMED 111C", "A-", 5.00),
        ("PATH 51", "A+", 4.00),

        ("CHEMENG 12SC", "A-", 2.00),

        ("CS 107", "B", 5.00),
        ("CS 109", "A-", 5.00),
        ("MATH 104", "C-", 4.00),
        ("PWR 2IY", "A-", 4.00),

        ("ARCHLGY 117", "A", 5.00),
        ("CS 161", "B", 5.00),
        
        ("CS 181W", "B", 4.00),
        ("CS 278", "B+", 4.00),
        ("ENGR 76", "A", 5.00),

        ("CS 147", "A", 5.00),
        ("CS 147L", "A-", 3.00),
        ("CS 177", "A", 4.00),
        ("VIETLANG 1", "A", 5.00),

        ("VIETLANG 2", "A-", 5.00),
        ("CS 347", "A-", 4.00),
        ("CS 111", "B", 5.00),

        ("VIETLANG 3", "A-", 5.00),
        ("CS 247G", "A", 4.00),
        ("CS 194", "A", 3.00),
        
        ("MUSIC 31N", "A-", 3.00),
        ("URBANST 103C", "A-", 3.00),

    ]
    courses_grad = [
        ("CS 224S", "A", 4.00),
        ("CS 205L", "A+", 3.00),
        ("CS 229", "B", 4.00),
        ("CS 148", "A+", 4.00),
        ("CS 152", "A", 3.00),
        ("CS 224N", "A-", 4.00),

        ("CS 399", "A", 18.00),

    ]

    courses_all = [
        ("CHEM 31M", "B-", 5.00),
        ("CME 100", "A", 5.00),
        ("EMED 111A", "A", 5.00),
        ("PWR 1BRB", "A-", 4.00),
        ("BIO 84", "A", 4.00),
        ("COLLEGE 102", "A", 3.00),
        ("CS 103", "C-", 5.00),
        ("CS 106B", "A", 5.00),
        ("EMED 111B", "B+", 5.00),
        ("CHEM 33", "C", 5.00),
        ("COLLEGE 108", "A", 4.00),
        ("EMED 111C", "A-", 5.00),
        ("PATH 51", "A+", 4.00),
        ("CHEMENG 12SC", "A-", 2.00),
        ("CS 107", "B", 5.00),
        ("CS 109", "A-", 5.00),
        ("MATH 104", "C-", 4.00),
        ("PWR 2IY", "A-", 4.00),
        ("ARCHLGY 117", "A", 5.00),
        ("CS 161", "B", 5.00),
        ("CS 224N", "A-", 4.00),
        ("CS 152", "A", 3.00),
        ("CS 181W", "B", 4.00),
        ("CS 278", "B+", 4.00),
        ("ENGR 76", "A", 5.00),
        ("CS 147", "A", 5.00),
        ("CS 147L", "A-", 3.00),
        ("CS 148", "A+", 4.00),
        ("CS 177", "A", 4.00),
        ("VIETLANG 1", "A", 5.00),

        ("VIETLANG 2", "A-", 5.00),
        ("CS 347", "A-", 4.00),
        ("CS 229", "B", 4.00),
        ("CS 205L", "A+", 3.00),
        ("CS 111", "B", 5.00),

        ("VIETLANG 3", "A-", 5.00),
        ("CS 247G", "A", 4.00),
        ("CS 194", "A", 3.00),
        ("CS 224S", "A", 4.00),
        ("MUSIC 31N", "A-", 3.00),
        ("URBANST 103C", "A-", 3.00)
    ]


    
    total_courses = [courses_ug, courses_grad, courses_all]

    for courses in total_courses:
        # Calculate total grade points and total units attempted
        total_grade_points = sum(grade_points[grade] * units for _, grade, units in courses)
        total_units_attempted = sum(units for _, _, units in courses)

        # Compute GPA
        gpa = total_grade_points / total_units_attempted
        print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()