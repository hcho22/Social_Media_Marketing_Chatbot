#!/usr/bin/env python
import sys
from instagram.crew import InstagramCrew
import datetime

def run():
    """
    Run the crew.
    """
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'instagram_description': input('Enter the page description here: '),
        'topic_of_the_week': input('Enter the topic of the week here: '),
    }
    InstagramCrew().crew().kickoff(inputs=inputs)

