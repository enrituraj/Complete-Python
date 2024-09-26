
"""
match subject:
    case pattern1:
        # code block if pattern1 matches
    case pattern2:
        # code block if pattern2 matches
    case _:
        # code block if no other pattern matches (default case)
"""

def check_day(day):
    match day:
        case 'Monday':
            print("Start of the work week!")
        case 'Friday':
            print("Almost weekend!")
        case 'Saturday' | 'Sunday':
            print("It's the weekend!")
        case _:
            print("Just another weekday.")
            
check_day('Saturday')


def process_coordinates(coord):
    match coord:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"On the x-axis at {x}")
        case (0, y):
            print(f"On the y-axis at {y}")
        case (x, y):
            print(f"Point at ({x}, {y})")
        case _:
            print("Not a valid coordinate")

process_coordinates((3, 0))

day = "Monday"
match day:
        case 'Monday':
            print("Start of the work week!")
        case 'Friday':
            print("Almost weekend!")
        case 'Saturday' | 'Sunday':
            print("It's the weekend!")
        case _:
            print("Just another weekday.")