#!/usr/bin/env python3

"""

DLP Test File — Source Code Policy Validation

Author: ISMS Security Team

Purpose: Test file to validate Endpoint DLP enforcement on .py files

"""
 
import os

import re

import json

import hashlib

import logging

import datetime

from typing import Optional, List, Dict
 
# Configure logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

logger = logging.getLogger(__name__)
 
 
# --- Constants ---

API_BASE_URL = "https://internal.avanade.com/api/v1"

SECRET_KEY = "dlp-test-secret-do-not-share"

DB_CONNECTION_STRING = "Server=sql-prod-01;Database=CorpData;User Id=svc_account;Password=P@ssw0rd123;"
 
 
# --- Data Models ---

class Employee:

    def __init__(self, employee_id: str, name: str, email: str, department: str):

        self.employee_id = employee_id

        self.name = name

        self.email = email

        self.department = department

        self.salary: Optional[float] = None

        self.ssn: Optional[str] = None  # Sensitive field
 
    def to_dict(self) -> Dict:

        return {

            "employee_id": self.employee_id,

            "name": self.name,

            "email": self.email,

            "department": self.department,

        }
 
    def __repr__(self):

        return f"<Employee {self.employee_id}: {self.name}>"
 
 
class DataProcessor:

    """Handles processing of sensitive employee data."""
 
    def __init__(self, encryption_key: str):

        self.encryption_key = encryption_key

        self.processed_records: List[Dict] = []
 
    def hash_sensitive_field(self, value: str) -> str:

        """Hash a sensitive value using SHA-256."""

        return hashlib.sha256(f"{self.encryption_key}{value}".encode()).hexdigest()
 
    def process_employee(self, employee: Employee) -> Dict:

        """Process and anonymize employee record."""

        record = employee.to_dict()

        if employee.ssn:

            record["ssn_hash"] = self.hash_sensitive_field(employee.ssn)

        if employee.salary:

            record["salary_band"] = self._get_salary_band(employee.salary)

        self.processed_records.append(record)

        logger.info(f"Processed record for employee {employee.employee_id}")

        return record
 
    def _get_salary_band(self, salary: float) -> str:

        if salary < 50000:

            return "Band A"

        elif salary < 100000:

            return "Band B"

        elif salary < 150000:

            return "Band C"

        else:

            return "Band D"
 
    def export_to_json(self, output_path: str) -> None:

        """Export processed records to JSON file."""

        with open(output_path, "w") as f:

            json.dump(self.processed_records, f, indent=2)

        logger.info(f"Exported {len(self.processed_records)} records to {output_path}")
 
 
# --- Utility Functions ---

def validate_email(email: str) -> bool:

    """Validate email format using regex."""

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"

    return bool(re.match(pattern, email))
 
 
def load_config(config_path: str) -> Dict:

    """Load configuration from a JSON file."""

    if not os.path.exists(config_path):

        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r") as f:

        return json.load(f)
 
 
def generate_report(records: List[Dict], report_date: datetime.date) -> str:

    """Generate a summary report from processed records."""

    lines = [

        f"=== Employee Data Report — {report_date} ===",

        f"Total records processed: {len(records)}",

        "",

    ]

    department_counts: Dict[str, int] = {}

    for record in records:

        dept = record.get("department", "Unknown")

        department_counts[dept] = department_counts.get(dept, 0) + 1
 
    lines.append("Records by department:")

    for dept, count in sorted(department_counts.items()):

        lines.append(f"  {dept}: {count}")
 
    return "\n".join(lines)
 
 
# --- Main Execution ---

def main():

    logger.info("Starting DLP test script execution")
 
    # Sample data

    employees = [

        Employee("E001", "David Moore", "david.moore@avanade.com", "Engineering"),

        Employee("E002", "Sarah Chen", "sarah.chen@avanade.com", "Finance"),

        Employee("E003", "James Patel", "james.patel@avanade.com", "Engineering"),

    ]
 
    employees[0].salary = 120000

    employees[0].ssn = "987-65-4321"

    employees[1].salary = 85000

    employees[2].salary = 135000
 
    # Validate emails

    for emp in employees:

        if not validate_email(emp.email):

            logger.warning(f"Invalid email for employee {emp.employee_id}: {emp.email}")
 
    # Process records

    processor = DataProcessor(encryption_key=SECRET_KEY)

    for emp in employees:

        processor.process_employee(emp)
 
    # Generate report

    report = generate_report(processor.processed_records, datetime.date.today())

    print(report)
 
    # Export

    processor.export_to_json("output_records.json")

    logger.info("DLP test script completed successfully")
 
 
if __name__ == "__main__":

    main()
 