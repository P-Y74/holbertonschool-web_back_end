#!/usr/bin/env python3
"""
Module to calculate and return the top students from a MongoDB collection.

This module provides a function to compute the average score for each student
and return a sorted list of students by their average score in
descending order.

Functions:
    top_students(mongo_collection): Returns a list of students sorted by
    average score.
"""


def top_students(mongo_collection):
    """
    Calculate the average score for each student and return a sorted list.

    Args:
        mongo_collection (pymongo.collection.Collection): A PyMongo collection
            containing student documents. Each student document must have a
            'name' field and a 'topics' list, where each topic has a 'score'.

    Returns:
        list of dict: A list of dictionaries, each containing:
            - '_id' (ObjectId): The MongoDB ID of the student.
            - 'name' (str): The name of the student.
            - 'averageScore' (float): The average score of the student.
        The list is sorted by 'averageScore' in descending order.
    """
    students = mongo_collection.find()

    student_avg = []
    for student in students:
        total_score = 0

        for topic in student["topics"]:
            total_score += topic["score"]

        avg_score = total_score / len(student["topics"])
        student_avg.append({
            "_id": student["_id"],
            "name": student["name"],
            "averageScore": avg_score
            })

    return sorted(student_avg, key=lambda x: x["averageScore"], reverse=True)
