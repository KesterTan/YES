import csv
import random
import os
from faker import Faker

fake = Faker()

# Number of mock rows to generate per table
NUM_ROWS = 10

# Define your nodeDataArray exactly as in your specification
nodeDataArray = [
    {
        "key": "Student",
        "location": "go.Point(0, 0)",
        "items": [
            {"name": "Full Name", "iskey": True, "figure": "Decision", "color": "purple"},
            {"name": "Middle Initial", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "First Name", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Last Name", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Suffix", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "PID Link", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "DOB", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "SS#", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Citizenship Status", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "City/County Residence", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Address Line 1", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Address Line 2", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Zipcode", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Alternate Address", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Race", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Additional Race (if applicable)", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Ethnicity", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Gender at Birth", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Gender Identity", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Student Email", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Primary Phone #", "iskey": False, "figure": "Circle", "color": "green"},
            {"name": "Secondary Phone Number", "iskey": False, "figure": "Circle", "color": "green"},
            {"name": "School Name", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Current Grade", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "YES ID", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Program Status", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Level of Service", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Intervention Specialist", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Call Type", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "MP Program Involvement?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Client Notes", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Divergent", "isKey": False, "figure": "Hexagon", "color": "orange"},
        ],
        "inheritedItems": [],
    },
    {
        "key": "Program",
        "location": "go.Point(300, 300)",
        "items": [
            {"name": "Program_ID", "iskey": True, "figure": "Decision", "color": "purple"},
            {"name": "Program_Name", "iskey": False, "figure": "Hexagon", "color": "blue"},
        ],
    },
    {
        "key": "Student_Program_Enrollment",
        "location": "go.Point(100, 0)",
        "items": [
            {"name": "Enrollment_ID", "iskey": True, "figure": "Decision", "color": "purple"},
            {"name": "Student_ID", "iskey": False, "figure": "Decision", "color": "red"},
            {"name": "Program_ID", "iskey": False, "figure": "Decision", "color": "red"},
            {"name": "Enrollment_Date", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Enrollment_Status", "iskey": False, "figure": "Hexagon", "color": "blue"},
        ],
    },
    {
        "key": "Course",
        "location": "go.Point(200, 0)",
        "items": [
            {"name": "Course_ID", "iskey": True, "figure": "Decision", "color": "purple"},
            {"name": "Course_Name", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Program_ID", "iskey": False, "figure": "Decision", "color": "red"},
            {"name": "Instructor_Name", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Instructor_Phone", "iskey": False, "figure": "Circle", "color": "green"},
            {"name": "Instructor_Email", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Meeting_Day", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Meeting_Time", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Meeting_Location", "iskey": False, "figure": "Hexagon", "color": "blue"},
        ],
    },
    {
        "key": "Award",
        "location": "go.Point(250, 250)",
        "items": [
            {"name": "Award Name", "isKey": True, "figure": "Decision", "color": "purple"}
        ],
    },
    {
        "key": "People",
        "location": "go.Point(700, 250)",
        "items": [
            {"name": "Relationship to Youth", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Email Contact", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Phone Contact", "iskey": False, "figure": "Circle", "color": "green"},
        ],
    },
    {
        "key": "Home Profile",
        "location": "go.Point(1000, 1000)",
        "items": [
            {"name": "How often do you hang out with your family?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "How often are you in your room when you are at home?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "How often do you get into arguments with others in your home?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "How many siblings do you have?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Do you live in a home, apartment, or townhome?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Do you have your own room?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "How many adults live in your house?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "What are your interactions like with other adults in your house?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "How often do you have contact with adults in your house?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Who is Working", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Supportive Adults at Home?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Any new or transient adults in house?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Additional Note:", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "Home Visit",
        "location": "go.Point(1000, 1200)",
        "items": [
            {"name": "Date", "isKye": False, "figure": "Hexagon", "color": "yellow"},
            {"name": "Location", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Attendees", "isKey": False, "figure": "Circle", "color": "green"},
            {"name": "Structural Safety", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Resident Updates", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Food Security", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Curfew Compliance", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Critical Incidences", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Additional Notes", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "Work Visit",
        "location": "go.Point(1000, 1200)",
        "items": [
            {"name": "Worksite Location", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Date Joined", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Worksite Visit Day", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Worksite Visit Time", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Worksite Schedule", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "School Profile",
        "location": "go.Point(100, 5)",
        "items": [
            {"name": "IEP?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Learning Disability?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Testing Anxiety?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Held Back?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Behavioral Diagnosis?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Traumatic Events?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Harmful Behavior?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Running Away?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Healthy Peer Relationship?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Healthy Adult Relationship?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Support System?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Safe at School?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Additional Notes", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "School Visit",
        "location": "go.Point(200, 5)",
        "items": [
            {"name": "Date", "isKey": False, "figure": "Circle", "color": "yellow"},
            {"name": "Location", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Attendees", "isKey": False, "figure": "Circle", "color": "green"},
            {"name": "Attendance Rate", "isKey": False, "figure": "Circle", "color": "green"},
            {"name": "Barriers to Student Success", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Successful Classes", "isKey": False},
            {"name": "Classes in Need of Assistance", "isKey": False},
            {"name": "Critical Incidences", "isKey": False},
            {"name": "Additional Note", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "Community Profile",
        "location": "go.Point(500, 500)",
        "items": [
            {"name": "What problem(s) do you hope to solve?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "What are your favorite things about your community?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "What is missing in your community", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Safe in your community?", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "Court Appearance",
        "location": "go.Point(900, 500)",
        "items": [
            {"name": "Date", "isKey": False, "figure": "Circle", "color": "yellow"},
            {"name": "Location", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Officer/Judge", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Attendees", "isKey": False, "figure": "Circle", "color": "yellow"},
            {"name": "Notes", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Disposition(s)", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Next Scheduled Hearing (if applicable)", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "Service Provision",
        "location": "go.Point(1000, 600)",
        "items": [
            {"name": "School Goal", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "School Intervention Category", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "School Intervention Description", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "School Frequency Intervention Staff", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "School Frequency Intervention Student", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "School Developed Skills", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "School Developed Status", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Outcome", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Goal", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Intervention Category", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Intervention Description", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Frequency Intervention Staff", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Frequency Intervention Student", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Developed Skills", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Developed Status", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Community Outcome", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Personal Goal", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Personal Intervention Category", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Personal Intervention Description", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Personal Frequency Intervention Staff", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Personal Frequency Intervention Student", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Personal Developed Skills", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Personal Developed Status", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Personal Outcome", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "Medical",
        "location": "go.Point(1000, 800)",
        "items": [
            {"name": "Medical Concerns", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Medical Concerns", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Medical Concerns", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Medications", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Permission to Transport?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Notes", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "Outing",
        "location": "go.Point(100, 0)",
        "items": [
            {"name": "Symposium", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Location", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
]

def generate_mock_value(column_name: str) -> str:
    """
    Generate a mock value for a given column name.
    """
    lower_col = column_name.lower()

    if "name" in lower_col and not any(x in lower_col for x in ["program", "course", "award"]):
        return fake.name()
    if "program_name" in lower_col:
        return random.choice(["STEM Program", "Arts Program", "Sports Program", "Community Service Program"])
    if "course_name" in lower_col:
        return random.choice(["English 101", "Math Fundamentals", "Biology Basics", "Intro to Coding", "Economics 201"])
    if "instructor_name" in lower_col:
        return fake.name()
    if "instructor_phone" in lower_col:
        return fake.phone_number()
    if "instructor_email" in lower_col:
        return fake.email()
    if "meeting_day" in lower_col:
        return random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    if "meeting_time" in lower_col:
        return random.choice(["8:00 AM", "10:00 AM", "1:30 PM", "3:00 PM", "6:15 PM"])
    if "relationship to youth" in lower_col:
        return random.choice(["Parent", "Guardian", "Sibling", "Aunt/Uncle", "Cousin", "Family Friend", "Mentor"])
    if "award name" in lower_col:
        return random.choice(["Perfect Attendance", "Honor Roll", "Community Service", "Leadership Award"])

    if "first name" in lower_col:
        return fake.first_name()
    if "last name" in lower_col:
        return fake.last_name()
    if "email" in lower_col or "email contact" in lower_col:
        return fake.email()
    if "phone" in lower_col:
        return fake.phone_number()
    if "dob" in lower_col or "date" in lower_col:
        return str(fake.date_of_birth(minimum_age=10, maximum_age=50))
    if "address" in lower_col:
        return fake.street_address()
    if "city" in lower_col or "county" in lower_col or "location" in lower_col:
        return fake.city()
    if "zip" in lower_col:
        return fake.zipcode()
    if "middle" in lower_col:
        return random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
    if "suffix" in lower_col:
        return random.choice(["Jr.", "Sr.", "III", "PhD", ""])
    if "citizenship" in lower_col:
        return random.choice(["Citizen", "Permanent Resident", "Visa Holder", "Undocumented"])
    if "race" in lower_col:
        return random.choice(["White", "Black or African American", "Asian", "Native American", "Hispanic/Latino", "Multiracial"])
    if "ethnicity" in lower_col:
        return random.choice(["Hispanic or Latino", "Not Hispanic or Latino"])
    if "gender" in lower_col:
        return random.choice(["Male", "Female", "Non-binary", "Other"])
    if "yes id" in lower_col:
        return f"YES-{fake.random_number(digits=5)}"
    if "ss#" in lower_col or "ssn" in lower_col:
        return fake.ssn()
    if "pid link" in lower_col or "id" in lower_col:
        # Some random ID
        return str(fake.random_number(digits=6))
    if "grade" in lower_col:
        return random.choice(["9", "10", "11", "12"])
    if "program status" in lower_col or "program_status" in lower_col or "enrollment_status" in lower_col:
        return random.choice(["Active", "Completed", "Dropped"])
    if "notes" in lower_col or "note" in lower_col:
        return fake.sentence(nb_words=6)
    if "call type" in lower_col:
        return random.choice(["Emergency", "Check-in", "Update"])
    if "intervention" in lower_col or "outcome" in lower_col or "skills" in lower_col or "status" in lower_col or "goal" in lower_col:
        # General short text
        return fake.sentence(nb_words=3)
    if "frequency" in lower_col:
        return random.choice(["Daily", "Weekly", "Monthly"])
    if "attendees" in lower_col:
        return ", ".join(fake.name() for _ in range(random.randint(1, 3)))
    if "officer" in lower_col or "judge" in lower_col:
        return fake.name()
    if "disposition" in lower_col:
        return random.choice(["Deferred", "Adjudicated", "Continued"])
    if "hearing" in lower_col:
        return str(fake.date_this_year())
    if "permission to transport" in lower_col:
        return random.choice(["Yes", "No"])
    if "medical concerns" in lower_col:
        return random.choice(["Allergy", "Asthma", "Diabetes", "None"])
    if "medications" in lower_col:
        return random.choice(["None", "Ibuprofen", "Ritalin", "Insulin"])
    if "symposium" in lower_col:
        return random.choice(["Career Fair", "Science Expo", "Community Gathering"])

    # Fallback word if no rule matched
    return fake.word().capitalize()


def main():
    # Number of rows to generate per table
    NUM_ROWS = 5

    # Create an output directory, or just save in current dir
    output_dir = "mock_csvs"
    os.makedirs(output_dir, exist_ok=True)

    # Process each table
    for table in nodeDataArray:
        table_name = table["key"]  # e.g. "Program", "Course"
        columns = [item["name"] for item in table["items"]]

        # We'll add a special column "Row_ID" to store a unique ID for each row
        extra_id_column = "Row_ID"
        all_columns = [extra_id_column] + columns

        csv_filename = os.path.join(output_dir, f"{table_name}.csv")

        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=all_columns)
            writer.writeheader()

            for _ in range(NUM_ROWS):
                row_data = {}
                # Generate a random ID for each row
                row_data[extra_id_column] = str(fake.random_number(digits=7))

                for col in columns:
                    row_data[col] = generate_mock_value(col)
                writer.writerow(row_data)

        print(f"Generated {NUM_ROWS} rows in '{csv_filename}'")

if __name__ == "__main__":
    main()