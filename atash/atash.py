"""Atash

Subclassing Flask to Atash will allow for the retention
of state, etc...
"""
import flask


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

    def stats(self):
        """
        """
        self.requests_counter['stats'] += 1
        return "stats"

    def build_stats(self):
        """
        """
        self.requests_counter = dict()


if __name__ == "__main__":
    Atash('atash').run(debug=True)
