<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width="40%" height="40%"/>
</p>

# NoSQL Project

## Project Overview
This project focuses on working with NoSQL databases, specifically MongoDB. By the end of this project, you will be able to:

- Understand what NoSQL is and the differences between SQL and NoSQL.
- Explain ACID properties and document storage.
- Identify the types and benefits of NoSQL databases.
- Query, insert, update, and delete information in a NoSQL database.
- Use MongoDB effectively with Python (PyMongo).

All MongoDB scripts are designed to run on Ubuntu 20.04 LTS with MongoDB 4.4. Python scripts use Python 3.9 with PyMongo 4.8.0, following `pycodestyle` guidelines.

---

## Requirements

### MongoDB Command Files
- All files interpreted/compiled on Ubuntu 20.04 LTS using MongoDB 4.4.
- Files must end with a new line.
- First line of all files: `// my comment`.

### Python Scripts
- Python 3.9 with PyMongo 4.8.0.
- Files must end with a new line.
- First line of all files: `#!/usr/bin/env python3`.
- Code must follow `pycodestyle` (v2.5.*).
- Modules and functions must have proper documentation.
- Scripts must not execute code when imported (use `if __name__ == "__main__":`).

---

## File Overview

| File | Description |
|------|-------------|
| `0-list_databases` | MongoDB command file to list all databases. |
| `1-use_or_create_database` | MongoDB command file to create or switch to a database. |
| `2-insert` | MongoDB command file to insert documents into a collection. |
| `3-all` | MongoDB command file to display all documents in a collection. |
| `4-match` | MongoDB command file to filter documents using match queries. |
| `5-count` | MongoDB command file to count documents in a collection. |
| `6-update` | MongoDB command file to update documents in a collection. |
| `7-delete` | MongoDB command file to delete documents from a collection. |
| `8-all.py` | Python script to retrieve all documents using PyMongo. |
| `8-main.py` | Test script for `8-all.py`. |
| `9-insert_school.py` | Python script to insert school documents into MongoDB. |
| `9-main.py` | Test script for `9-insert_school.py`. |
| `10-update_topics.py` | Python script to update topics in school documents. |
| `10-main.py` | Test script for `10-update_topics.py`. |
| `11-schools_by_topic.py` | Python script to find schools filtered by topic. |
| `11-main.py` | Test script for `11-schools_by_topic.py`. |
| `12-log_stats.py` | Python script to log database statistics. |
| `100-find` | **Advanced task:** MongoDB command file to find documents with specific criteria. |
| `101-students.py` | **Advanced task:** Python script to manage student documents in MongoDB. |
| `101-main.py` | Test script for `101-students.py`. |
| `102-log_stats.py` | **Advanced task:** Python script for advanced logging/statistics. |
| `README.md` | Project README file, providing overview, requirements, and file descriptions. |

---

## Style and Documentation
- All modules include descriptive docstrings.
- All functions include docstrings explaining their purpose and usage.
- Type annotations are used consistently in Python scripts.
- Python scripts are designed to be import-safe (`if __name__ == "__main__":`).

---

## Usage
To run a Python script, use:

```bash
python3 <script_name>.py
```

To run a MongoDB command file, use the mongo shell:

```bash
mongo <command_file>
```

---

## Author

**P-Y74**  
🔗 [GitHub Profile](https://github.com/P-Y74)

---

## About

This project is part of the Full Stack Web Development curriculum at Holberton School.
