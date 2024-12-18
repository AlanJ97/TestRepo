print ("My APP 1")

# Test case for the print statement
def test_print_output(capsys):
    print("My APP 1")
    captured = capsys.readouterr()
    assert captured.out == "My APP 1\n"
