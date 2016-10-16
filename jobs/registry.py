"""
This class registers NLP jobs by name.
"""

registry = {}

def register(name, fn):
    registry[name] = fn

def run(name, body):
    return registry[name](body)
