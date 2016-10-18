"""
This file contains a mapping from NLP job names to functions.
"""

registry = {}

"""
Adds a job to the registry
name <String>
fn <Function>
"""
def register(name, fn):
    registry[name] = fn


"""
Runs a job
name <String>
payload <Dict>
"""
def run(name, payload):
    if name in registry:
        return registry[name](payload)
