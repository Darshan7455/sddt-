# Timetable Scheduler

This project is a timetable scheduling application designed to help educational institutions efficiently allocate courses, teachers, and rooms to time slots. The application uses a backtracking algorithm with heuristics to generate optimal timetables while adhering to various constraints.

## Project Structure

```
timetable-scheduler
├── src
│   ├── __init__.py
│   ├── scheduler.py
│   ├── timetable.py
│   └── utils.py
├── tests
│   ├── __init__.py
│   ├── test_scheduler.py
│   └── test_timetable.py
├── data
│   └── sample_data.csv
├── requirements.txt
├── setup.py
└── README.md
```

## Features

- Load data from CSV files for courses, teachers, rooms, and time slots.
- Check constraints to ensure teachers are available, rooms are suitable, and sections are free.
- Implement a backtracking algorithm to generate class and exam timetables.
- Save generated timetables to a database and export them to CSV files.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd timetable-scheduler
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the timetable scheduler, execute the following command:
```
python src/scheduler.py
```

## Testing

To run the tests, use:
```
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.