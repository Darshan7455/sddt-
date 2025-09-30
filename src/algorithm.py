from .constraints import no_clash, classroom_available

def generate_timetable(courses, faculty, classrooms, time_slots):
    timetable = []
    for course in courses:
        for time_slot in time_slots:
            for classroom in classrooms:
                if no_clash(timetable, course["faculty"], time_slot) and \
                   classroom_available(timetable, classroom, time_slot):
                    timetable.append({
                        "course": course["name"],
                        "faculty": course["faculty"],
                        "classroom": classroom,
                        "time": time_slot
                    })
                    break
    return timetable
