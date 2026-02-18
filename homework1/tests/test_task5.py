import pytest
from src import task5

def test_output(capsys):
    # Populate list and print first 3 books
    book_list = task5.populate_list()
    print(book_list[0:3])
    captured = capsys.readouterr()

    # Check for expected output of first 3 books
    list_string = ("[['Dungeon Crawler Carl', 'Matt Dinniman'], " +
        "['The Lord of the Rings', 'JRR Tolkien'], " +
        "['Leviathan Wakes', 'James SA Corey']]\n")
    assert captured.out == list_string

    # Populate the dictionary and check 3 randomly selected
    # student IDs match
    students = task5.populate_dict()
    assert students["STU-816742"] == {'first_name': 'Kofi', 
        'last_name': 'Asante'}
    assert students["STU-265839"] == {'first_name': 'Fatima', 
        'last_name': 'Al-Rashid'}
    assert students["STU-450927"] == {'first_name': 'Liam', 
        'last_name': 'Callahan'}