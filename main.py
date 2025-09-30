from scheduler.data_loader import load_courses, load_faculty, load_classrooms
from scheduler.algorithm import generate_timetable
from scheduler.timetable import save_timetable

courses = load_courses()
faculty = load_faculty()
classrooms = load_classrooms()
time_slots = ["Mon 9-10", "Mon 10-11", "Tue 9-10", "Tue 10-11"]

timetable = generate_timetable(courses.to_dict("records"),
                               faculty.to_dict("records"),
                               classrooms["name"].tolist(),
                               time_slots)

save_timetable(timetable)
