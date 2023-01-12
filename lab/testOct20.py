import oct20

def test_get_fields():
    expected = ["Name","Gender","Birthdate","Address"]
    assert oct20.get_fields() == expected

def test_store_info():
    info = ["Kate", "F", "01/01/1990", "123 abc"]
    oct20.store_info(info)
    last_line = open(oct20.FILENAME, 'r').readlines()[-2]
    assert last_line == "Kate,F,01/01/1990,123 abc\n"
    # can store other lines and over-write the file

# YOUR CODE HERE
def test_validate():
    assert oct20.validate("Birthdate", "01/01/2020") == True
    assert oct20.validate("Birthdate", "01,01,2020") == False

def test_validate_name():
    assert oct20.validate_name("") == False
    assert oct20.validate_name("Jane, Doe") == False
    assert oct20.validate_name("Jane") == False
    assert oct20.validate_name("Jane Doe") == True

def test_validate_gender():
    assert oct20.validate_gender("") == False
    assert oct20.validate_gender("K") == False
    assert oct20.validate_gender("F") == True

def main():
    test_get_fields()
    test_store_info()
    test_validate()
    test_validate_name()
    test_validate_gender()
    print("All tests passed!")

if __name__ == "__main__":
    main()

