import pandas as pd

def load_courses(path="data/courses.csv"):
    return pd.read_csv(path)

def load_faculty(path="data/faculty.csv"):
    return pd.read_csv(path)

def load_classrooms(path="data/classrooms.csv"):
    return pd.read_csv(path)
