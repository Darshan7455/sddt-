import pandas as pd

def export_timetable_csv(timetable, filename="output/timetable.csv"):
    rows = []
    for slot, data in timetable.items():
        for entry in data["entries"]:
            rows.append({
                "Course": entry["courseId"],
                "Section": entry["section"]["id"],
                "Teacher": entry["teacherId"],
                "Room": entry["room"]["id"],
                "Slot": slot
            })
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)
    print(f"Timetable exported to {filename}")
