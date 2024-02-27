### Dont Forget

- pytest (tests every test_ or _test.py files)
  
- pytest -v (Shows each test Passed or Failed seperately)

- pytest path/of/test_file.py::test_specific_function_name
  
- pytest path/of/test_file.py

- pytest path/of/test_file.py -s to print captures to terminal.

- We can use **assert** statement to check the value.

- 2 types of testing (**Function based, Class Based**)

- To run test, we should cd to the file's directory and in terminal write
pytest. In convention pytest looks the files that begins with **test_** or
ends with **_test.py** than run this files if exist. And the functions in test
file should also begin with test_ otherwise no test will run by pytest.

- In class based testing there is a **setup_method** and **teardown_method** takes method as parameter. We can instantiate our test object in setup_method and delete it in teardown_method.

- In function based testings dont forget to use **@pytest.fixture** to instantiate the object once (not in every test function) in function and return it and use it in other comparison testing functions.

- Or we can create **_conftest.py_** file in test folder and we can **@pytest.fixture** the objects there so we can globally use it other testing modules without using @pytest.fixture and initialize function.(In a nutshell, we can seperate them for clean look of test module.)

- _Marking_: e.g. > **@pytest.mark.slow** and to only run the test on marked function > pytest -m slow.
  Another example of using marked function is **pytest.mark.skip(reason='why did you skip ?')** In the terminal as a result we can see Passed, Skipped numbers.
  **pytest.mark.xfail(reason='Write the reason)'** We can leave the some broken test especially to show. So, we mark them with xfail. In terminal marks: s > skip, ... > slow, xfail > xfail

- _Parametrize_ is useful where we want to test same piece of code under various conditions by running single test function multiple times with different sets of arguments.Syntax is like that: **pytest.mark.parametrize(test_input, expected,[(1,2), (2,3), (3,4)])** List of tuples[0] = test_input, list of tuples[1] = expected. To see example look at test_square.py file.
