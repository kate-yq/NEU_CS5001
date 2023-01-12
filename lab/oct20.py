# Quan Yuamn
# requests info from the user for a job application
# adds that info to applicant_info.csv

FILENAME = "applicant_info.csv"  # where the user's data gets stored


# returns the fields for which we need user input
# return them as a list of strings
def get_fields():
    header = open(FILENAME, 'r').readlines()[0].strip()
    return header.split(',')


# takes the list of fields for which we want user input
# asks the user to imput a value for each field
# return the user's answers for each field as aa list of strings
def ask_user(fields):
    answers = []
    answer = ""
    for field in fields:
        while not validate(field, answer):
            answer = input(field + ": ")
        answers.append(answer)
    return answers

# takes the name of the field and the user's answer
# returns true if the answer is valid for the field


def validate(field, answer):
    if field == "Name":
        return validate_name(answer)
    elif field == "Gender":
        return validate_gender(answer)
    else:
        return ',' not in answer


# YOUR CODE HERE:
# write 2 functions that validate name and gender
# return True or False for validation result
# and write tests for the 2 functions

# function 1: validate name
# takes in a string as user's answer and check if it is a name
# return True if it is, and False if not
def validate_name(answer):
    if answer == "":
        return False
    elif (',' in answer) or ('0' in answer) or ('1' in answer) or ('2' in answer) or ('3' in answer) or ('4' in answer) or ('5' in answer) or ('6' in answer) or ('7' in answer) or ('8' in answer) or ('9' in answer):
        return False
    names = answer.split(' ')
    if len(names) != 2:
        print("please include both your first name and last name")
        return False
    return True

# function 2: validate gender
# takes in a string as user's answer and check if it is a gender
# return True if it is, and False if not


def validate_gender(answer):
    GENDER = ['M', 'F']  # could amend if wants to define more gender in future
    if answer in GENDER:
        return True
    else:
        return False


# accepts the user's info as a list of strings
# adds the user's info as a row to FILENAME csv
def store_info(info):
    datafile = open(FILENAME, 'a')
    row = ','.join(info) + '\n'
    datafile.write(row)


def main():
    fields = get_fields()
    answers = ask_user(fields)
    store_info(answers)


if __name__ == "__main__":
    main()
