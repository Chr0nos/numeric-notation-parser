# Installation
## With poetry
```shell
poetry add numeric_notation_parser
```

## With pip
```shell
pip install numeric_notation_parser
```


## Supported formats
Input is marked as a string, output as a list of int
| Input         | Output as list                                              |
|---------------|-------------------------------------------------------------|
| 10,11,22      | [10, 11, 22]                                                |
| 0-10          | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                          |
| 0-10/2        | [0, 2, 4, 6, 8, 10]                                         |
| 10--10/3      | [10, 7, 4, 1, -2, -5, -8]                                   |

## Example
```python
from numeric_notation_parser import notation_to_integer_generator

for number in notation_to_integer_generator("4,100-120/2,-10--20/2"):
    print(number)
```

You can also pass `raise_errors` if you want to raise a `ValueError` in case of an invalid format.
By default the parser will ignore any invalid tokens, so "1,foo,2,bar,3" will output `[1, 2, 3]`
