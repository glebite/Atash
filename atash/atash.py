"""Atash

Subclassing Flask to Atash will allow for the retention
of state, etc...
"""
# import flask
from flask import Flask, request
from functools import wraps
from collections import defaultdict
import queue


def stats_wrapper(method):
    """stats_wrapper - cool things

    Parameters:
    method (function): - method to wrap

    Returns:
    _impl (function):
    """
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        method_output = method(self, *method_args, **method_kwargs)
        self.requests_counter[method.__name__] += 1
        return method_output
    return _impl


class Atash(Flask):
    """Atash - main class for the server
    """
    def __init__(self, app_name):
        """
        """
        super().__init__(app_name)
        self.build_stats()
        self.load_routes()
        self.queue = queue.Queue()

    def load_routes(self):
        """
        """
        self.route('/stats')(self.stats)
        self.route('/caller', methods=['POST', 'GET'])(self.caller)

    @stats_wrapper
    def stats(self):
        """
        """
        return "stats"

    @stats_wrapper
    def caller(self):
        """
        """
        if request.method == 'POST':
            print(f'posting... {request.form=}')
        elif request.method == 'GET':
            print('getting...')
        else:
            return f"{request.method} not supported", 405
        return str(self.requests_counter)

    def build_stats(self):
        """
        """
        self.requests_counter = defaultdict(lambda: 0)
        return


if __name__ == "__main__":
    Atash('atash').run(debug=True)
