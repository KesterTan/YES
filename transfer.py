import pandas as pd

# This is your nodeDataArray structure, repeated for clarity.
nodeDataArray = [
    {
        "key": "Student",
        "items": [
            {"name": "Full Name", "iskey": True},
            {"name": "Middle Initial", "iskey": False},
            {"name": "First Name", "iskey": False},
            {"name": "Last Name", "iskey": False},
            {"name": "Suffix", "iskey": False},
            {"name": "PID Link", "iskey": False},
            {"name": "DOB", "iskey": False},
            {"name": "SS#", "iskey": False},
            {"name": "Citizenship Status", "iskey": False},
            {"name": "City/County Residence", "iskey": False},
            {"name": "Address Line 1", "iskey": False},
            {"name": "Address Line 2", "iskey": False},
            {"name": "Zipcode", "iskey": False},
            {"name": "Alternate Address", "iskey": False},
            {"name": "Race", "iskey": False},
            {"name": "Additional Race (if applicable)", "iskey": False},
            {"name": "Ethnicity", "iskey": False},
            {"name": "Gender at Birth", "iskey": False},
            {"name": "Gender Identity", "iskey": False},
            {"name": "Student Email", "iskey": False},
            {"name": "Primary Phone #", "iskey": False},
            {"name": "Secondary Phone Number", "iskey": False},
            {"name": "School Name", "iskey": False},
            {"name": "Current Grade", "iskey": False},
            {"name": "YES ID", "iskey": False},
            {"name": "Program Status", "iskey": False},
            {"name": "Level of Service", "iskey": False},
            {"name": "Intervention Specialist", "isKey": False},
            {"name": "Call Type", "isKey": False},
            {"name": "MP Program Involvement?", "isKey": False},
            {"name": "Client Notes", "isKey": False},
            {"name": "Divergent", "isKey": False},
        ],
    },
    {
        "key": "Program",
        "items": [
            {"name": "Program_ID", "iskey": True},
            {"name": "Program_Name", "iskey": False},
        ],
    },
    {
        "key": "Student_Program_Enrollment",
        "items": [
            {"name": "Enrollment_ID", "iskey": True},
            {"name": "Student_ID", "iskey": False},
            {"name": "Program_ID", "iskey": False},
            {"name": "Enrollment_Date", "iskey": False},
            {"name": "Enrollment_Status", "iskey": False},
        ],
    },
    {
        "key": "Course",
        "items": [
            {"name": "Course_ID", "iskey": True},
            {"name": "Course_Name", "iskey": False},
            {"name": "Program_ID", "iskey": False},
            {"name": "Instructor_Name", "iskey": False},
            {"name": "Instructor_Phone", "iskey": False},
            {"name": "Instructor_Email", "iskey": False},
            {"name": "Meeting_Day", "iskey": False},
            {"name": "Meeting_Time", "iskey": False},
            {"name": "Meeting_Location", "iskey": False},
        ],
    },
    {
        "key": "Award",
        "items": [
            {"name": "Award Name", "isKey": True}
        ],
    },
    {
        "key": "People",
        "items": [
            {"name": "Relationship to Youth", "iskey": False},
            {"name": "Email Contact", "iskey": False},
            {"name": "Phone Contact", "iskey": False},
        ],
    },
    {
        "key": "Home Profile",
        "items": [
            {"name": "How often do you hang out with your family?", "isKey": False},
            {"name": "How often are you in your room when you are at home?", "isKey": False},
            {"name": "How often do you get into arguments with others in your home?", "isKey": False},
            {"name": "How many siblings do you have?", "isKey": False},
            {"name": "Do you live in a home, apartment, or townhome?", "isKey": False},
            {"name": "Do you have your own room?", "isKey": False},
            {"name": "How many adults live in your house?", "isKey": False},
            {"name": "What are your interactions like with other adults in your house?", "isKey": False},
            {"name": "How often do you have contact with adults in your house?", "isKey": False},
            {"name": "Who is Working", "isKey": False},
            {"name": "Supportive Adults at Home?", "isKey": False},
            {"name": "Any new or transient adults in house?", "isKey": False},
            {"name": "Additional Note:", "isKey": False},
        ]
    },
    {
        "key": "Home Visit",
        "items": [
            {"name": "Date", "isKye": False, "figure": "Hexagon", "color": "yellow"},
            {"name": "Location", "isKey": False},
            {"name": "Attendees", "isKey": False},
            {"name": "Structural Safety", "isKey": False},
            {"name": "Resident Updates", "isKey": False},
            {"name": "Food Security", "isKey": False},
            {"name": "Curfew Compliance", "isKey": False},
            {"name": "Critical Incidences", "isKey": False},
            {"name": "Additional Notes", "isKey": False},
        ]
    },
    {
        "key": "School Profile",
        "items": [
            {"name": "IEP?", "isKey": False},
            {"name": "Learning Disability?", "isKey": False},
            {"name": "Testing Anxiety?", "isKey": False},
            {"name": "Held Back?", "isKey": False},
            {"name": "Behavioral Diagnosis?", "isKey": False},
            {"name": "Traumatic Events?", "isKey": False},
            {"name": "Harmful Behavior?", "isKey": False},
            {"name": "Running Away?", "isKey": False},
            {"name": "Healthy Peer Relationship?", "isKey": False},
            {"name": "Healthy Adult Relationship?", "isKey": False},
            {"name": "Support System?", "isKey": False},
            {"name": "Safe at School?", "isKey": False},
            {"name": "Additional Notes", "isKey": False},
        ]
    },
    {
        "key": "School Visit",
        "items": [
            {"name": "Date", "isKey": False},
            {"name": "Location", "isKey": False},
            {"name": "Attendees", "isKey": False},
            {"name": "Attendance Rate", "isKey": False},
            {"name": "Barriers to Student Success", "isKey": False},
            {"name": "Successful Classes", "isKey": False},
            {"name": "Classes in Need of Assistance", "isKey": False},
            {"name": "Critical Incidences", "isKey": False},
            {"name": "Additional Note", "isKey": False},
        ]
    },
    {
        "key": "Community Profile",
        "items": [
            {"name": "What problem(s) do you hope to solve?", "isKey": False},
            {"name": "What are your favorite things about your community?", "isKey": False},
            {"name": "What is missing in your community", "isKey": False},
            {"name": "Safe in your community?", "isKey": False},
        ]
    },
    {
        "key": "Court Appearance",
        "items": [
            {"name": "Date", "isKey": False},
            {"name": "Location", "isKey": False},
            {"name": "Officer/Judge", "isKey": False},
            {"name": "Attendees", "isKey": False},
            {"name": "Notes", "isKey": False},
            {"name": "Disposition(s)", "isKey": False},
            {"name": "Next Scheduled Hearing (if applicable)", "isKey": False},
        ]
    },
    {
        "key": "Service Provision",
        "items": [
            {"name": "School Goal", "isKey": False},
            {"name": "School Intervention Category", "isKey": False},
            {"name": "School Intervention Description", "isKey": False},
            {"name": "School Frequency Intervention Staff", "isKey": False},
            {"name": "School Frequency Intervention Student", "isKey": False},
            {"name": "School Developed Skills", "isKey": False},
            {"name": "School Developed Status", "isKey": False},
            {"name": "Community Outcome", "isKey": False},
            {"name": "Community Goal", "isKey": False},
            {"name": "Community Intervention Category", "isKey": False},
            {"name": "Community Intervention Description", "isKey": False},
            {"name": "Community Frequency Intervention Staff", "isKey": False},
            {"name": "Community Frequency Intervention Student", "isKey": False},
            {"name": "Community Developed Skills", "isKey": False},
            {"name": "Community Developed Status", "isKey": False},
            {"name": "Community Outcome", "isKey": False},
            {"name": "Personal Goal", "isKey": False},
            {"name": "Personal Intervention Category", "isKey": False},
            {"name": "Personal Intervention Description", "isKey": False},
            {"name": "Personal Frequency Intervention Staff", "isKey": False},
            {"name": "Personal Frequency Intervention Student", "isKey": False},
            {"name": "Personal Developed Skills", "isKey": False},
            {"name": "Personal Developed Status", "isKey": False},
            {"name": "Personal Outcome", "isKey": False},
        ]
    },
    {
        "key": "Medical",
        "items": [
            {"name": "Medical Concerns", "iskey": False},
            {"name": "Medical Concerns", "iskey": False},
            {"name": "Medical Concerns", "iskey": False},
            {"name": "Medications", "isKey": False},
            {"name": "Permission to Transport?", "isKey": False},
            {"name": "Notes", "isKey": False},
        ]
    },
    {
        "key": "Outing",
        "items": [
            {"name": "Symposium", "isKey": False},
            {"name": "Location", "isKey": False},
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
