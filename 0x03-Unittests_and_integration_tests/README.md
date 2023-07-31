![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)


![tests](../assets/unittest.gif)

## About
Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests
```
$ python -m unittest path/to/test_file.py
```

## Resources
__Read or watch__:

1. [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
2. [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
3. [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
4. [parameterized](https://pypi.org/project/parameterized/)
5. [Memoization](https://en.wikipedia.org/wiki/Memoization)
