"""Atash

Subclassing Flask to Atash will allow for the retention
of state, etc...
"""
import flask
from functools import wraps
from collections import defaultdict


def stats_wrapper(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        method_output = method(self, *method_args, **method_kwargs)
        self.requests_counter[method.__name__] += 1
        return method_output
    return _impl


class Atash(flask.Flask):
    """
    """
    def __init__(self, app_name):
        """
        """
        super().__init__(app_name)
        self.build_stats()
        self.load_routes()

    def load_routes(self):
        """
        """
        self.route('/stats')(self.stats)
        self.route('/caller')(self.caller)

    @stats_wrapper
    def stats(self):
        """
        """
        return "stats"

    @stats_wrapper
    def caller(self):
        """
        """
        return str(self.requests_counter)

    def build_stats(self):
        """
        """
        self.requests_counter = defaultdict(lambda: 0)
        return


if __name__ == "__main__":
    Atash('atash').run(debug=True)
