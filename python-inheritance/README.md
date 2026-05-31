# Python Inheritance

This project covers Python inheritance concepts and includes minimal exercises for working with class inheritance, object attributes, and methods.

## Files

- `0-lookup.py`: Defines the `lookup(obj)` function that returns a list of available attributes and methods of an object.
- `1-my_list.py`: Defines the `MyList` class that inherits from `list` and adds a `print_sorted()` method.
- `tests/1-my_list.txt`: Doctest for `MyList` behavior.

## Usage

### `lookup`

```bash
python3 -c "lookup = __import__('0-lookup').lookup; print(lookup(int))"
```

### `MyList`

```bash
cat <<'PY' > /tmp/1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
PY

python3 /tmp/1-main.py
```

## Project Requirements

- Python 3.8.5 on Ubuntu 20.04 LTS
- Files must be executable and start with `#!/usr/bin/python3`
- No external modules are imported
- Doctest files located in `tests/`
- Modules, classes, and functions include documentation strings

## Notes

- `lookup(obj)` uses Python's built-in `dir()` function to return available attributes and methods.
- `MyList` inherits from built-in `list` and adds a `print_sorted()` method that displays the sorted list without modifying the original list.
