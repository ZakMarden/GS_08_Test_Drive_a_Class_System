"""
1
Create instaices of entries with entry Class
Add them to instance of diary class
Check that diary.all returns entries

"""

from lib.diary import *
from lib.diary_entry import *

def test_create_and_add_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry('Test title 1', 'Contents string 1')
    diary.add(entry_1)
    assert diary.all() == [entry_1]

def test_find_best_entry():
    diary = Diary()
    entry_1 = DiaryEntry('Test title 1', '1 2')
    entry_2 = DiaryEntry('Test title 2', '1 2 3 4')
    entry_3 = DiaryEntry('Test title 3', '1 2 3 4 5 6')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(5, 1).title == "Test title 2"