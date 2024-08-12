import pytest
from calculator import add

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1
    assert add("1000") == 1000

def test_two_numbers():
    assert add("1,5") == 6
    assert add("999,1000") == 1999

def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_new_line_delimiters():
    assert add("1\n2,3") == 6
    assert add("1\n2\n3") == 6

def test_custom_single_char_delimiter():
    assert add("//;\n1;2") == 3
    assert add("//,\n2,3,4") == 9

def test_custom_multiple_char_delimiter():
    assert add("//[***]\n1***2***3") == 6
    assert add("//[##]\n4##5##6") == 15

def test_custom_multiple_delimiters():
    assert add("//[*][%]\n1*2%3") == 6
    assert add("//[+][;]\n10+20;30") == 60

def test_custom_mixed_length_delimiters():
    assert add("//[*][%%]\n1*2%%3") == 6
    assert add("//[##][%%%]\n7##8%%%9") == 24

def test_ignore_large_numbers():
    assert add("2,1001") == 2
    assert add("1000,1001") == 1000
    assert add("1001,1002,1003") == 0

def test_ignore_large_numbers_within_custom_delimiters():
    assert add("//;\n2;1001") == 2
    assert add("//[***]\n1000***1001***1002") == 1000

def test_negative_numbers():
    with pytest.raises(ValueError) as excinfo:
        add("1,-2,3")
    assert str(excinfo.value) == "negative numbers not allowed: -2"

def test_multiple_negative_numbers():
    with pytest.raises(ValueError) as excinfo:
        add("1,-2,-3,4")
    assert str(excinfo.value) == "negative numbers not allowed: -2, -3"

def test_negative_numbers_with_custom_delimiters():
    with pytest.raises(ValueError) as excinfo:
        add("//;\n1;-2;3")
    assert str(excinfo.value) == "negative numbers not allowed: -2"

    with pytest.raises(ValueError) as excinfo:
        add("//[***]\n1***-2***-3")
    assert str(excinfo.value) == "negative numbers not allowed: -2, -3"

def test_empty_custom_delimiter():
    assert add("//\n1\n2,3") == 6  # Falls back to default delimiters

def test_multiple_empty_custom_delimiters():
    assert add("//[]\n1,2\n3") == 6  # Falls back to default delimiters

def test_custom_delimiter_with_special_characters():
    assert add("//[$$]\n1$$2$$3") == 6
    assert add("//[@@][##]\n1@@2##3") == 6

def test_custom_delimiter_with_whitespace():
    assert add("//[ ]\n1 2 3") == 6  # Delimiter is a space

def test_large_input_with_various_delimiters():
    assert add("1,2,3\n4,5\n6,7,8\n9") == 45
    assert add("//[***][%%]\n1***2%%3***4%%5***6%%7") == 28

def test_very_large_numbers_and_negative_numbers():
    with pytest.raises(ValueError) as excinfo:
        add("//[***]\n-1000***-1002***1001***2")
    assert str(excinfo.value) == "negative numbers not allowed: -1000, -1002"
