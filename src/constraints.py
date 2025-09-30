def no_clash(timetable, faculty, time_slot):
    return all(entry["faculty"] != faculty or entry["time"] != time_slot 
               for entry in timetable)

def classroom_available(timetable, classroom, time_slot):
    return all(entry["classroom"] != classroom or entry["time"] != time_slot 
               for entry in timetable)
