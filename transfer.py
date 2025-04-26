import pandas as pd

nodeDataArray = [
    {
        "key": "Student",
        "items": [
            {"name": "Full Name", "isKey": True},
            {"name": "Middle Initial", "isKey": False},
            {"name": "First Name", "isKey": False},
            {"name": "Last Name", "isKey": False},
            {"name": "Summer ID", "isKey": False},
            {"name": "Suffix", "isKey": False},
            {"name": "PID Link", "isKey": False},
            {"name": "DOB", "isKey": False},
            {"name": "Disability Status", "isKey": False},
            {"name": "Age", "isKey": False},
            {"name": "SS#", "isKey": False},
            {"name": "Citizenship Status", "isKey": False},
            {"name": "City/County Residence", "isKey": False},
            {"name": "Address", "isKey": False},
            {"name": "Address Line 2", "isKey": False},
            {"name": "Zipcode", "isKey": False},
            {"name": "Alternate Address", "isKey": False},
            {"name": "Race", "isKey": False},
            {"name": "Ethnicity", "isKey": False},
            {"name": "Gender", "isKey": False},
            {"name": "Gender Identity", "isKey": False},
            {"name": "Email", "isKey": False},
            {"name": "Phone Number", "isKey": False},
            {"name": "Secondary Phone Number", "isKey": False},
            {"name": "School", "isKey": False},
            {"name": "Current Grade", "isKey": False},
            {"name": "YES ID", "isKey": False},
            {"name": "Interview Link", "isKey": False},
            {"name": "Program Status", "isKey": False},
            {"name": "Program Completion Date", "isKey": False},
            {"name": "Court Appearance", "isKey": False},
            {"name": "Latest Court Appearance Date", "isKey": False},
            {"name": "Recidivated?", "isKey": False},
            {"name": "Level of Service", "isKey": False},
            {"name": "Intervention Specialist", "isKey": False},
            {"name": "Call Type", "isKey": False},
            {"name": "MP Program Involvement?", "isKey": False},
            {"name": "Client Notes", "isKey": False},
            {"name": "Divergent", "isKey": False},
            {"name": "Award", "isKey": False},
            {"name": "Outing", "isKey": False},
            {"name": "Medical", "isKey": False},
            {"name": "Service Provision", "isKey": False},
            {"name": "People", "isKey": False},
            {"name": "Program", "isKey": False},
            {"name": "Profile Picture", "isKey": False},
            {"name": "Goal", "isKey": False},
            {"name": "Photo Release", "isKey": False},
            {"name": "Incident Report", "isKey": False},
            {"name": "Work Visits", "isKey": False},
            {"name": "Community Profile", "isKey": False},
            {"name": "School Profile", "isKey": False},
            {"name": "Home Profile", "isKey": False},
            {"name": "Participation Status", "isKey": False},
            {"name": "Length of Program Involvement", "isKey": False},
            {"name": "Bank Account Status", "isKey": False},
            {"name": "Bank Account Institution", "isKey": False},
        ],
    },
    {
        "key": "Work Visit",
        "items": [
            {"name": "Worksite Location", "isKey": False},
            {"name": "Date Joined", "isKey": False},
            {"name": "Worksite Visit Day", "isKey": False},
            {"name": "Worksite Visit Time", "isKey": False},
            {"name": "Worksite Schedule", "isKey": False},
        ]
    },
    {
        "key": "Program",
        "items": [
            {"name": "Program Name", "isKey": True},
            {"name": "Program Type", "isKey": False},
            {"name": "Course", "isKey": False},
            {"name": "Outing", "isKey": False},
            {"name": "Student", "isKey": False},
            {"name": "Photo Release", "isKey": False},
            {"name": "Number of Students", "isKey": False},
        ],
    },
    {
        "key": "Student_Program_Enrollment",
        "items": [
            {"name": "Enrollment_ID", "isKey": True},
            {"name": "Student_ID", "isKey": False},
            {"name": "Program_ID", "isKey": False},
            {"name": "Enrollment_Date", "isKey": False},
            {"name": "Enrollment_Status", "isKey": False},
        ],
    },
    {
        "key": "Course",
        "items": [
            {"name": "Course_ID", "isKey": True},
            {"name": "Course Name", "isKey": False},
            {"name": "Course Instructor", "isKey": False},
            {"name": "Course Instructor Phone", "isKey": False},
            {"name": "Course Instructor Email", "isKey": False},
            {"name": "Course Meeting Day", "isKey": False},
            {"name": "Course Meeting Time", "isKey": False},
            {"name": "Course Meeting Location", "isKey": False},
            {"name": "Program_ID", "isKey": False},
            {"name": "Instructor_Name", "isKey": False},
            {"name": "Instructor_Phone", "isKey": False},
            {"name": "Instructor_Email", "isKey": False},
            {"name": "Meeting_Day", "isKey": False},
            {"name": "Meeting_Time", "isKey": False},
            {"name": "Meeting_Location", "isKey": False},
            {"name": "Program", "isKey": False}
        ],
    },
    {
        "key": "Award",
        "items": [
            {"name": "Award Name", "isKey": True},
            {"name": "Student", "isKey": False},
            {"name": "Character", "isKey": False},
            {"name": "Workplace Excellence", "isKey": False},
            {"name": "Superlative", "isKey": False},

        ],
    },
    {
        "key": "People",
        "items": [
            {"name": "Name", "isKey": True},
            {"name": "Parent/Guardian Contact #1", "isKey": False},
            {"name": "Parent/Guardian #1 Relationship to Youth", "isKey": False},
            {"name": "Parent/Guardian Email Contact #1", "isKey": False},
            {"name": "Parent/Guardian Phone Contact #1", "isKey": False},
            {"name": "Emergency Contact Name", "isKey": False},
            {"name": "Emergency Contact Relationship", "isKey": False},
            {"name": "Emergency Contact Email", "isKey": False},
            {"name": "Emergency Contact Phone", "isKey": False},
            {"name": "Relationship to Youth", "isKey": False},
            {"name": "Email Contact", "isKey": False},
            {"name": "Phone Contact", "isKey": False},
            {"name": "Student", "isKey": False},
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
            {"name": "Date", "isKey": False, "figure": "Hexagon", "color": "yellow"},
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
            {"name": "School_Profile_ID", "isKey": True},
            {"name": "IEP?", "isKey": False},
            {"name": "IEP Explanation", "isKey": False},
            {"name": "Learning Disability?", "isKey": False},
            {"name": "Disability Explanation", "isKey": False},
            {"name": "Testing Anxiety?", "isKey": False},
            {"name": "Testing Anxiety Explanation", "isKey": False},
            {"name": "Held Back?", "isKey": False},
            {"name": "Held Back Explanation", "isKey": False},
            {"name": "Behavioral Diagnosis?", "isKey": False},
            {"name": "Behavioral Diagnosis Explanation", "isKey": False},
            {"name": "Traumatic Events?", "isKey": False},
            {"name": "Traumatic Events Explanation", "isKey": False},
            {"name": "Harmful Behavior?", "isKey": False},
            {"name": "Harmful Behavior Explanation", "isKey": False},
            {"name": "Running Away?", "isKey": False},
            {"name": "Running Away Explanation", "isKey": False},
            {"name": "Healthy Peer Relationship?", "isKey": False},
            {"name": "Healthy Peer Relationship Explanation", "isKey": False},
            {"name": "Healthy Adult Relationship?", "isKey": False},
            {"name": "Healthy Adult Relationship Explanation", "isKey": False},
            {"name": "Support System?", "isKey": False},
            {"name": "Support System Explanation", "isKey": False},
            {"name": "Safe at School?", "isKey": False},
            {"name": "Safe at School Explanation", "isKey": False},
            {"name": "Additional Notes", "isKey": False},
            {"name": "Student", "isKey": False},
            {"name": "School Visit", "isKey": False},
        ]
    },
    {
        "key": "School Visit",
        "items": [
            {"name": "School_Visit_ID", "isKey": True},
            {"name": "Date", "isKey": False},
            {"name": "Location", "isKey": False},
            {"name": "Attendees", "isKey": False},
            {"name": "Attendance Rate", "isKey": False},
            {"name": "Attendance Rate Note", "isKey": False},
            {"name": "Barriers to Student Success", "isKey": False},
            {"name": "Successful Classes", "isKey": False},
            {"name": "Classes in Need of Assistance Note", "isKey": False},
            {"name": "Critical Incidences", "isKey": False},
            {"name": "Additional Note", "isKey": False},
            {"name": "School_Profile", "isKey": False},
        ]
    },
    {
        "key": "Community Profile",
        "items": [
            {"name": "Student", "isKey": False},
            {"name": "What problem(s) do you hope to solve?", "isKey": False},
            {"name": "What are your favorite things about your community?", "isKey": False},
            {"name": "What is missing in your community", "isKey": False},
            {"name": "Safe in your community?", "isKey": False},
            {"name": "Additional Note", "isKey": False},
        ]
    },
    {
        "key": "Court Appearance",
        "items": [
            {"name": "Court_Appearance_ID", "isKey": True},
            {"name": "Date", "isKey": False},
            {"name": "Location", "isKey": False},
            {"name": "Officer/Judge", "isKey": False},
            {"name": "Attendees", "isKey": False},
            {"name": "Notes", "isKey": False},
            {"name": "Disposition(s)", "isKey": False},
            {"name": "Next Scheduled Hearing (if applicable)", "isKey": False},
            {"name": "Student", "isKey": False},
        ]
    },
    {
        "key": "Service Provision",
        "items": [
            {"name": "Service_Provision_ID", "isKey": True},
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
            {"name": "Student", "isKey": False},
        ]
    },
    {
        "key": "Medical",
        "items": [
            {"name": "Medical_ID", "isKey": True},
            {"name": "Medical Concerns", "isKey": False},
            {"name": "Medications", "isKey": False},
            {"name": "Permission to Transport?", "isKey": False},
            {"name": "Notes", "isKey": False},
            {"name": "Student", "isKey": False},
            {"name": "People", "isKey": False},
        ]
    },
    {
        "key": "Outing",
        "items": [
            {"name": "Symposium", "isKey": False},
            {"name": "Location", "isKey": False},
            {"name": "Student", "isKey": False},
            {"name": "Program", "isKey": False},
            {"name": "Date", "isKey": False},
            {"name": "Status", "isKey": False},
        ]
    },
    {
        "key": "Worksite",
        "items": [
            {"name": "Worksite_ID", "isKey": True},
            {"name": "Worksite", "isKey": False},
            {"name": "Worksite Supervisor", "isKey": False},
            {"name": "Worksite Supervisor Phone", "isKey": False},
            {"name": "Worksite Supervisor Email", "isKey": False},
            {"name": "Worksite Supervisor Phone", "isKey": False},
            {"name": "Worksite Supervisor Email", "isKey": False},
            {"name": "Worksite Visit Day", "isKey": False},
            {"name": "Worksite Visit Time", "isKey": False},
            {"name": "Worksite Visit Location", "isKey": False},
            {"name": "Worksite Schedule", "isKey": False}, 
        ]
    },
    {
        "key": "Fiscal",
        "items": [
            {"name": "Fiscal_ID", "isKey": True},
            # len is supposed to be Last Name
            {"name": "len", "isKey": False},
            {"name": "First Name", "isKey": False},
            {"name": "Total Hours Worked", "isKey": False},
            {"name": "Total Hours Remaining", "isKey": False},
            {"name": "Work Experience Hours Worked", "isKey": False},
            {"name": "Work Experience Hours Remaining", "isKey": False},
            {"name": "Training Hours Worked", "isKey": False},
            {"name": "Training Hours Remaining", "isKey": False},
            {"name": "Pay 1", "isKey": False},
            {"name": "Pay 2", "isKey": False},
            {"name": "Pay 3", "isKey": False},
    
        ]
    },
    {
        "key": "Awards",
        "items": [
            {"name": "Award_ID", "isKey": True},
            {"name": "Youth Name", "isKey": False},
            {"name": "Character Awards", "isKey": False},
            {"name": "Workplace Excellence", "isKey": False},
            {"name": "Superlative", "isKey": False},
            {"name": "Worksite", "isKey": False},
            {"name": "Certificate of Completion", "isKey": False}
        ]
    },
]

all_dfs = {}

def create_csvs_from_node_data_array(
        input_csv_path: str, 
        node_data: list
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
            
            matching_indices = []
            
            # If the column exists in the original CSV, copy it
            if col_name in df.columns:
                if table_name == "Medical":
                    if col_name == "Medical Concerns":
                        # Find all column indices that match any "Medical Concerns" variant
                        matching_indices = [i for i, col in enumerate(df.columns) if col_name in col]
                        # Extract those columns
                        df_columns = df.iloc[:, matching_indices]
                        # Flatten them into a single column
                        exploded_values = df_columns.values.flatten()
                        # Repeat each row once per "Medical Concerns" column
                        repeat_count = len(matching_indices)
                        repeated_rows = df.loc[df.index.repeat(repeat_count)].reset_index(drop=True)
                        new_df[col_name] = exploded_values
                    else:
                        # Regular column – just repeat it to match the expanded row count
                        if col_name in df.columns:
                            repeated_col = df[col_name].loc[df.index.repeat(len(matching_indices))].reset_index(drop=True)
                            new_df[col_name] = repeated_col
                        else:
                            new_df[col_name] = None  # Fill with None if column doesn't exist
                else:
                    matching_indices = [i for i, col in enumerate(df.columns) if col_name == col]
                    df_columns = df.iloc[:, matching_indices]
                    new_df[col_name] = pd.DataFrame(df_columns.values.flatten(), columns=[col_name])
            else:
                # Fill with None if not present
                new_df[col_name] = None
        
        all_dfs[table_name] = new_df
        
def run_all_dfs(output_dir):
    student_df = all_dfs["Student"]
    number_of_students = len(student_df)
    
    for table_name, new_df in all_dfs.items():
        if table_name != "Medical":
            num_missing = number_of_students - len(new_df)
            if num_missing > 0:
                padding = pd.DataFrame([ [None]*len(new_df.columns) ] * num_missing, columns=new_df.columns)
                new_df = pd.concat([new_df, padding], ignore_index=True)

    for row_id in range(len(student_df)):
        student_df["People"] = all_dfs["People"]["Name"]
        for i in range(3):
            student_df["Medical"] = row_id + i
        student_df["Award"] = all_dfs["Award"]["Award Name"]
        student_df["Program"] = all_dfs["Program"]["Program Name"]
        student_df["School Profile"] = row_id
        student_df["Community Profile"] = row_id
        student_df["Home Profile"] = row_id
        
    for table_name, new_df in all_dfs.items():
        output_path = f"{output_dir}/{table_name}.csv"
        new_df.to_csv(output_path, index=False)
        print(f"Created CSV for table '{table_name}' -> {output_path}")

if __name__ == "__main__":
    create_csvs_from_node_data_array(
        input_csv_path="master.csv",
        node_data=nodeDataArray,
    )
    output_dir="./test"
    run_all_dfs(output_dir)
