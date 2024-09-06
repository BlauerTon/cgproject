import pandas as pd
from functions import generate_email_vectorized, separate_by_gender, find_names_with_special_chars
from constraints import log_computation, ensure_unique_emails

# Load the Excel file
file_path = 'TestFiles.xlsx'
xls = pd.ExcelFile(file_path)

# Load the first sheet ('File_A')
df_file_a = pd.read_excel(xls, sheet_name='File_A')

# Apply the email generation
student_names = df_file_a['Student Name'].values
df_file_a['Generated Email'] = generate_email_vectorized(student_names)

# Separate lists of male and female students
male_students, female_students = separate_by_gender(df_file_a)

# Log the number of male and female students
log_computation(f"Total male students: {len(male_students)}")
log_computation(f"Total female students: {len(female_students)}")

# Identify students with special characters in their names
special_char_names = find_names_with_special_chars(df_file_a['Student Name'])

# Log the names with special characters
log_computation(f"Students with special characters in their names: {special_char_names}")

# Ensure the emails are unique
try:
    ensure_unique_emails(df_file_a['Generated Email'].tolist())
    log_computation("All emails are unique.")
except ValueError as e:
    log_computation(str(e))

# Save the separate lists to CSV and TSV files
male_students.to_csv('male_students.csv', index=False)
female_students.to_csv('female_students.csv', index=False)

male_students.to_csv('male_students.tsv', sep='\t', index=False)
female_students.to_csv('female_students.tsv', sep='\t', index=False)

# Save the original DataFrame with emails
df_file_a.to_csv('output_emails.csv', index=False)
df_file_a.to_csv('output_emails.tsv', sep='\t', index=False)

# Log the saving of files
log_computation("Saved separate lists of male and female students.")
log_computation("Saved output as CSV and TSV files.")