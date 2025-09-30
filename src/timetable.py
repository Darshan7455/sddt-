import pandas as pd

def save_timetable(timetable, path="output/timetable.xlsx"):
    df = pd.DataFrame(timetable)
    df.to_excel(path, index=False)
    print(f"Timetable saved at {path}")
