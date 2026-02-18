# This function populates a list with book titles and authors
def populate_list():
    book_list = []
    book_list.append(["Dungeon Crawler Carl", "Matt Dinniman"])
    book_list.append(["The Lord of the Rings", "JRR Tolkien"])
    book_list.append(["Leviathan Wakes", "James SA Corey"])
    book_list.append(["Dune", "Frank Herbert"])
    book_list.append(["Project Hail Mary", "Andy Weir"])
    book_list.append(["The Lightning Thief", "Rick Riodan"])
    book_list.append(["Fahrenheit 451", "Ray Bradbury"])
    book_list.append(["The Things They Carried", "Tim O'Brien"])
    book_list.append(["Paradise Lost", "John Milton"])
    book_list.append(["American Gods", "Neil Gaiman"])
    return book_list

# This function populates a dictionary with a database of students where
# the key is the student ID, and the value is the student's first and last name
def populate_dict():
    students = {
        "STU-482910": {"first_name": "Marcus", "last_name": "Delgado"},
        "STU-371654": {"first_name": "Priya", "last_name": "Nambiar"},
        "STU-209483": {"first_name": "Olivia", "last_name": "Hartwell"},
        "STU-816742": {"first_name": "Kofi", "last_name": "Asante"},
        "STU-534801": {"first_name": "Zoe", "last_name": "Pemberton"},
        "STU-127365": {"first_name": "Dmitri", "last_name": "Volkov"},
        "STU-693218": {"first_name": "Amara", "last_name": "Okonkwo"},
        "STU-450927": {"first_name": "Liam", "last_name": "Callahan"},
        "STU-784536": {"first_name": "Yuna", "last_name": "Ishikawa"},
        "STU-318064": {"first_name": "Sofia", "last_name": "Marchetti"},
        "STU-942187": {"first_name": "Elijah", "last_name": "Thornton"},
        "STU-265839": {"first_name": "Fatima", "last_name": "Al-Rashid"},
    }
    return students

# Main declared for debugging
def main():
    # Print the first 5 items of the list
    book_list = populate_list()
    print(book_list[0:5])
    
    # Print three random students from the dictionary
    # using their student IDs
    students = populate_dict()
    print(students["STU-534801"])
    print(students["STU-265839"])
    print(students["STU-127365"])
    

if __name__ == "__main__":
    main()