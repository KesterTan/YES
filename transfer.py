import pandas as pd

# This is your nodeDataArray structure, repeated for clarity.
nodeDataArray = [
    {
        "key": "Student",
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
    },
    {
        "key": "Program",
        "items": [
            {"name": "Program_ID", "iskey": True, "figure": "Decision", "color": "purple"},
            {"name": "Program_Name", "iskey": False, "figure": "Hexagon", "color": "blue"},
        ],
    },
    {
        "key": "Student_Program_Enrollment",
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
        "items": [
            {"name": "Award Name", "isKey": True, "figure": "Decision", "color": "purple"}
        ],
    },
    {
        "key": "People",
        "items": [
            {"name": "Relationship to Youth", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Email Contact", "iskey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Phone Contact", "iskey": False, "figure": "Circle", "color": "green"},
        ],
    },
    {
        "key": "Home Profile",
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
        "key": "School Profile",
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
        "items": [
            {"name": "What problem(s) do you hope to solve?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "What are your favorite things about your community?", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "What is missing in your community", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Safe in your community?", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    },
    {
        "key": "Court Appearance",
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
        "items": [
            {"name": "Symposium", "isKey": False, "figure": "Hexagon", "color": "blue"},
            {"name": "Location", "isKey": False, "figure": "Hexagon", "color": "blue"},
        ]
    }
]

def create_csvs_from_node_data_array(
        input_csv_path: str, 
        node_data: list, 
        output_dir: str = "."
    ):
    """
    Creates a CSV file for each 'key' in nodeDataArray.
    Each new CSV will have columns corresponding to the 'name' of each 'item'.
    If a column is missing from the source CSV, fill with None.
    """
    # Read the original CSV
    df = pd.read_csv(input_csv_path)
    
    # Go through each table definition in node_data
    for node in node_data:
        table_name = node["key"]
        items = node.get("items", [])
        
        # Create an empty DataFrame; we will fill columns one by one
        new_df = pd.DataFrame()
        
        for item in items:
            col_name = item["name"]
            
            # If the column exists in the original CSV, copy it
            if col_name in df.columns:
                new_df[col_name] = df[col_name]
            else:
                # Fill with None if not present
                new_df[col_name] = None
        
        # Write out to a new CSV named <key>.csv in the desired output directory
        output_path = f"{output_dir}/{table_name}.csv"
        new_df.to_csv(output_path, index=False)
        print(f"Created CSV for table '{table_name}' -> {output_path}")

if __name__ == "__main__":
    create_csvs_from_node_data_array(
        input_csv_path="CMU IS 2025 Sample Roster Information - Reference (1).csv",
        node_data=nodeDataArray,
        output_dir="."
    )
