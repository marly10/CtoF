def main():
    # Initialize dictionaries
    rooms = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755,
             'NT110': 1244, 'CM241': 1411}

    instructors = {'CS101': 'Haynes', 'CS102': 'Alvarado',
                   'CS103': 'Randy', 'NT110': 'Burke',
                   'CM241': 'Lee'}

    times = {'CS101': '8:00 am', 'CS102': '9:00 am',
             'CS103': '10:00 am', 'NT110': '11:00 am',
             'CM241': '1:00 pm'}

    grades = {'CS101': 'Pass:70%', 'CS102': 'Pass:70%',
              'CS103': 'Pass:70%', 'NT110': 'Pass:70%',
              'CM241': 'Pass:70%'}

    tool = {'CS101': 'Pen', 'CS102': 'Ruler',
            'CS103': 'Pants', 'NT110': 'Afro',
            'CM241': 'Gas'}

    course = input('Enter a class name:')

    if course not in rooms:
        print(course, 'is an invalid course number.')
    else:
        print('--------------------------------------------')
        print('Room:', rooms[course])
        print('Instructor:', instructors[course])
        print('Time: ', times[course])
        print('Grades: ', grades[course])
        print('Tools Needed: ', tool[course])
        print('--------------------------------------------')


# Call the main function.
main()


def lower():

    division = {
        'CSC1043': ' Introduction to Computer Programming', 'CSC1043L': 'Introduction to Computer Programming Lab', 'CSC1054 ': ' Objects and Elementary Data Structure'
    }
