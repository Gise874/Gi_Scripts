using System;
using System.Collections.Generic;
 
namespace TestingSample
{
    class Program
    {
        static void Main(string[] args)
        {
            string employeeName = "John Smith";
            int employeeId = 1001;
            double salary = 75000.50;
 
            Console.WriteLine($"Employee: {employeeName}");
            Console.WriteLine($"ID: {employeeId}");
            Console.WriteLine($"Salary: ${salary}");
 
            List<string> departments = new List<string>
            {
                "IT",
                "Finance",
                "HR"
            };
 
            foreach (string department in departments)
            {
                Console.WriteLine($"Department: {department}");
            }
        }
    }
}