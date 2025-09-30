# File: /timetable-scheduler/timetable-scheduler/tests/test_scheduler.py

import unittest
from src.scheduler.scheduler import Scheduler

class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def test_schedule_creation(self):
        # Test the creation of a schedule
        self.scheduler.create_schedule()
        self.assertIsNotNone(self.scheduler.schedule)

    def test_add_course(self):
        # Test adding a course to the schedule
        course = "Math 101"
        self.scheduler.add_course(course)
        self.assertIn(course, self.scheduler.courses)

    def test_remove_course(self):
        # Test removing a course from the schedule
        course = "Math 101"
        self.scheduler.add_course(course)
        self.scheduler.remove_course(course)
        self.assertNotIn(course, self.scheduler.courses)

    def test_schedule_conflict(self):
        # Test for schedule conflicts
        course1 = "Math 101"
        course2 = "Physics 101"
        self.scheduler.add_course(course1)
        self.scheduler.add_course(course2)
        conflict = self.scheduler.check_conflict(course1, course2)
        self.assertFalse(conflict)

if __name__ == '__main__':
    unittest.main()