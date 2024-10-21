#include <stdio.h>
#include <stdbool.h>

// Function to check if a year is a leap year
bool isLeapYear(int year) {
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            if (year % 400 == 0)
                return true;
            else
                return false;
        } else {
            return true;
        }
    } else {
        return false;
    }
}

// Function to validate the date
bool isValidDate(int day, int month, int year) {
    // Check if the year is valid
    if (year < 1)
        return false;

    // Check if the month is valid
    if (month < 1 || month > 12)
        return false;

    // Days in each month
    int daysInMonth[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

    // Adjust for leap year in February
    if (isLeapYear(year)) {
        daysInMonth[1] = 29;
    }

    // Check if the day is valid
    if (day < 1 || day > daysInMonth[month - 1])
        return false;

    return true;
}

// Test cases for date validation
void testDateValidation() {
    // Test valid dates
    printf("Test 1: %s\n", isValidDate(15, 8, 2024) ? "Passed" : "Failed"); // Valid date
    printf("Test 2: %s\n", isValidDate(29, 2, 2024) ? "Passed" : "Failed"); // Valid leap year date
    printf("Test 3: %s\n", isValidDate(31, 12, 2024) ? "Passed" : "Failed"); // Valid date

    // Test invalid dates
    printf("Test 4: %s\n", isValidDate(0, 8, 2024) ? "Passed" : "Failed"); // Invalid day
    printf("Test 5: %s\n", isValidDate(15, 13, 2024) ? "Passed" : "Failed"); // Invalid month
    printf("Test 6: %s\n", isValidDate(29, 2, 2023) ? "Passed" : "Failed"); // Invalid leap year date (not a leap year)
    printf("Test 7: %s\n", isValidDate(32, 1, 2024) ? "Passed" : "Failed"); // Invalid day
}

// Main function to execute test cases
int main() {
    testDateValidation();
    return 0;
}