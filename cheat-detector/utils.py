import json


def read_data_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


def range_attendance(attendance):
    ranges = [(0, 25), (26, 50), (51, 75), (76, 100)]

    attendance = round(attendance)
    for lower, upper in ranges:
        if lower <= attendance <= upper:
            return lower, upper


def range_cgpa(cgpa):
    ranges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    for lower, upper in ranges:
        if lower <= cgpa < upper:
            return lower, upper


def range_grade(grade):
    ranges = [(0, 25), (26, 50), (51, 75), (76, 100)]

    grade = round(grade)
    for lower, upper in ranges:
        if lower <= grade <= upper:
            return lower, upper


def cheat_probability(cheat, hw, pov):
    cheat_val = list(cheat.values())[0]
    hw_val = list(hw.values())[0]
    pov_val = list(pov.values())[0]

    return {"cheat": [list(cheat.keys())[0], cheat_val], "hw": [list(hw.keys())[0], hw_val],
            "pov": [list(pov.keys())[0], pov_val],
            "output": str(round(cheat_val * hw_val * pov_val * 100, 3)) + "%"}
