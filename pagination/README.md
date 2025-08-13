<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%"/>
</p>

# Pagination Project

## Project Overview
This project focuses on implementing various pagination techniques in Python. By the end of this project, you will be able to:

- Paginate a dataset using simple `page` and `page_size` parameters.
- Paginate a dataset with hypermedia metadata.
- Implement deletion-resilient pagination.

All implementations are done in Python 3.9 on Ubuntu 20.04 LTS, following the `pycodestyle` guidelines.

---

## Requirements
- Python 3.9
- All files must end with a new line.
- All files must start with `#!/usr/bin/env python3`.
- Use `pycodestyle` (version 2.5.*) for code style.
- All modules and functions must have proper documentation.
- All functions and coroutines must be type-annotated.

---

## File Overview

| File | Description |
|------|-------------|
| `0-main.py` | Example script demonstrating the usage of the simple helper function. |
| `0-simple_helper_function.py` | Contains a simple helper function to fetch data from the CSV dataset. |
| `1-main.py` | Test script for simple pagination implementation. |
| `1-simple_pagination.py` | Implements basic pagination using `page` and `page_size` parameters. |
| `2-main.py` | Test script for hypermedia pagination implementation. |
| `2-hypermedia_pagination.py` | Implements hypermedia pagination with additional metadata for navigation. |
| `3-main.py` | Test script for deletion-resilient hypermedia pagination. |
| `3-hypermedia_del_pagination.py` | Implements deletion-resilient pagination, ensuring consistent results despite dataset changes. |
| `Popular_Baby_Names.csv` | Dataset containing popular baby names used for pagination exercises. |
| `README.md` | This file, providing an overview of the project, requirements, and file structure. |

---

## Style and Documentation
- All modules include descriptive docstrings.
- All functions include docstrings explaining their purpose and usage.
- Type annotations are used consistently across all functions and coroutines.

---

## Usage
To test each pagination method, run the corresponding `*-main.py` file. For example:

```bash
python3 1-main.py
```
This will demonstrate the functionality of simple pagination using the provided CSV dataset.

---

## Author

**P-Y74**  
🔗 [GitHub Profile](https://github.com/P-Y74)

---

## About

This project is part of the Full Stack Web Development curriculum at Holberton School

