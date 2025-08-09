#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        if name is not None:
            if (
                not isinstance(name, str)
                or name == ""
                or (isinstance(name, str) and len(name) > 25)
            ):
                print("Name must be string between 1 and 25 characters.")
                self.name = name
            else:
                self.name = name.title()
        else:
            self.name = name
        if job is not None and job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        self.job = job
