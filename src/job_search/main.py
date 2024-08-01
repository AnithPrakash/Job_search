#!/usr/bin/env python
import sys
from src.job_search.crew import JobSearchCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'job_type': input('Enter your dream job')
    }
    JobSearchCrew().crew().kickoff(inputs=inputs)

    



