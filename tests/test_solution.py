from solution import *

class Tests:

  def test_guess_number(self, monkeypatch):
    """
    Test that the method returns the correct values in a variety of cases.
    """
    # data to use in tests
    mock_data = {
      'num_attempts': [3, 4, 5, 3],
      'randint': [5, 10, 17, 5],
      'input': ['foo', '4', '5'] + ['6', 'foo', '10'] + ['foo', '4', '2', '9', '12'] + ['4', '2', '1'],
      'expected': [True, True, False, False]
    }

    # count how many times each mock function is called
    call_counter = {
      'input': 0,
      'randint': 0
    }

    # mock the random.randint function
    def mock_randint(low, high):
      call_counter['randint'] += 1
      return mock_data['randint'].pop(0)
    monkeypatch.setattr('random.randint', lambda x, y: mock_randint(x, y))
    
    # mock the input function
    def mock_input(message):
      call_counter['input'] += 1
      return mock_data['input'].pop(0)
    monkeypatch.setattr('builtins.input', lambda x: mock_input(x))

    # calculate how many times we expect each function to be called
    expected_input_calls = len(mock_data['input'])
    expected_randint_calls = len(mock_data['randint'])
    
    # run through the calls with various mock data
    num_calls = len(mock_data['randint']) # the number of mock runs of the function we're testing
    for i in range(num_calls):
      expected = mock_data['expected'][i]
      actual = guess_number(1, 100, mock_data['num_attempts'][i])
      assert actual == expected

    # check that each function was called the correct number of times
    assert call_counter['input'] == expected_input_calls
    assert call_counter['randint'] == expected_randint_calls