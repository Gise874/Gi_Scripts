#include <iostream>
#include <vector>
#include <string>
 
class EmployeeManager {
public:
    void addEmployee(const std::string& name) {
        employees.push_back(name);
    }
 
    void listEmployees() {
        for (const auto& employee : employees) {
            std::cout << employee << std::endl;
        }
    }
 
private:
    std::vector<std::string> employees;
};
 
int main() {
 
    EmployeeManager manager;
 
    manager.addEmployee("John Smith");
    manager.addEmployee("Jane Doe");
    manager.addEmployee("Mike Johnson");
 
    manager.listEmployees();
 
    return 0;
}
