import re
import numpy as np


# Function to generate email based on the student's name
def generate_email(student_name):
    # Remove special characters from the names
    student_name = re.sub(r"[^a-zA-Z\s]", "", student_name)
    # Split the name into individual components
    name_parts = student_name.split()

    # If the name has more than two parts, take the first initial and last name
    if len(name_parts) >= 2:
        first_initial = name_parts[0][0].lower()
        last_name = name_parts[-1].lower()
        email = f"{first_initial}{last_name}@gmail.com"
    else:
        # For single names, use the entire name as is
        email = f"{name_parts[0].lower()}@gmail.com"

    return email


# Vectorized function for email generation
def generate_email_vectorized(student_names):
    return np.vectorize(generate_email)(student_names)

# Function to filter male and female students
def separate_by_gender(df, gender_column='Gender'):
    male_students = df[df[gender_column] == 'M']
    female_students = df[df[gender_column] == 'F']
    return male_students, female_students

# Function to find names with special characters using regex
def find_names_with_special_chars(names):
    special_char_names = [name for name in names if re.search(r"[^a-zA-Z\s]", name)]
    return special_char_names