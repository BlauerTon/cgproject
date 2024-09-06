import pandas as pd
import re


# Function to generate email from student name
def generate_email(full_name):
    names = full_name.split(', ')
    if len(names) == 2:
        first_name = names[0].split()[0]  # First name
        last_name = names[1].split()[-1]  # Last name or second name

        email = f"{first_name[0].lower()}{last_name.lower()}@gmail.com"

        # Remove special characters from email (except the @ and .)
        email = re.sub(r'[^a-zA-Z0-9@.]', '', email)
        return email
    else:
        return None


file_path = 'Testfiles.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

for index, row in df.iterrows():
    student_name = row['Student Name']
    email = generate_email(student_name)
    # print(f"Student Name: {student_name} - Email address: {email}")


df['Generated Email'] = df['Student Name'].apply(generate_email)
df.to_excel('students_with_emails.xlsx', index=False)
