<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%"/>
</p>

# 📌 Python - Variable Annotations

This project focuses on mastering **type annotations** in Python 3. You’ll explore how to improve code clarity, safety, and maintainability by explicitly declaring variable and function types. The project includes a series of exercises that cover standard and advanced use cases, along with validation using `mypy`.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to:

- Understand **type annotations** in Python 3.
- Use annotations to define **function signatures** and **variable types**.
- Apply the concept of **duck typing** in Python.
- Validate Python code with **mypy**.
- Write clean, type-safe, and well-documented Python code.

---

## ✅ Requirements

- All code is written in **Python 3.9** and tested on **Ubuntu 20.04 LTS**
- Files must end with a **new line**
- The first line of each script must be:  
  `#!/usr/bin/env python3`
- Code must follow **pycodestyle** (version `2.5.*`)
- All files must be **executable**
- File lengths will be tested using `wc`
- All modules, classes, and functions must have proper **documentation**  
  (i.e., complete, meaningful docstrings)

---

## 📁 Project Structure

| File Name                    | Description                                |
|-----------------------------|--------------------------------------------|
| `0-add.py`                  | Adds two integers with type annotations    |
| `0-main.py`                 | Main file to test `0-add.py`               |
| `1-concat.py`               | Concatenates two strings                   |
| `1-main.py`                 | Main file to test `1-concat.py`            |
| `2-floor.py`                | Floors a float to the nearest lower int    |
| `2-main.py`                 | Main file to test `2-floor.py`             |
| `3-to_str.py`               | Converts a float to a string               |
| `3-main.py`                 | Main file to test `3-to_str.py`            |
| `4-define_variables.py`     | Defines variables with explicit types      |
| `4-main.py`                 | Main file to test `4-define_variables.py`  |
| `5-sum_list.py`             | Returns the sum of a list of floats        |
| `5-main.py`                 | Main file to test `5-sum_list.py`          |
| `6-sum_mixed_list.py`       | Sums a list with floats and integers       |
| `6-main.py`                 | Main file to test `6-sum_mixed_list.py`    |
| `7-to_kv.py`                | Converts a key and number to a tuple       |
| `7-main.py`                 | Main file to test `7-to_kv.py`             |
| `8-make_multiplier.py`      | Returns a function that multiplies floats  |
| `8-main.py`                 | Main file to test `8-make_multiplier.py`   |
| `9-element_length.py`       | Annotates function that returns list of tuples |
| `9-main.py`                 | Main file to test `9-element_length.py`    |
| `100-safe_first_element.py` | Advanced: safely returns the first element |
| `100-main.py`               | Main file to test advanced task 100        |
| `101-safely_get_value.py`   | Advanced: safely fetches a value from dict |
| `101-main.py`               | Main file to test advanced task 101        |
| `102-type_checking.py`      | Advanced: static type checking with `mypy` |
| `102-main.py`               | Main file to test advanced task 102        |
| `README.md`                 | Project documentation                      |

---

## ⚙️ How to Run

1. **Make sure you have Python 3.9 installed**:
   ```bash
   python3 --version
   ```
2. **(Optional): Install mypy to validate types**:
   ```bash
   pip install mypy
   ```
3. **Run a script**:
   ```bash
   python3 0-main.py
   ```
4. **Type check a module**:
   ```bash
   mypy 0-add.py
   ```

---

## 📌 Example Type Annotation

```python
def add(a: int, b: int) -> int:
    """Adds two integers and returns the sum."""
    return a + b
```

---

## ✍️ Author

**P-Y74**  
🔗 [GitHub Profile](https://github.com/P-Y74)

---

## 🏫 About

This project is part of the Full Stack Web Development curriculum at Holberton School.

It aims to give students a strong foundation in Python’s type system and writing robust, clean, and predictable code. Understanding variable annotations and using tools like mypy are essential skills for modern Python developers.

---
