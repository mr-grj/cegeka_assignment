from flask import Response, jsonify
from flask_restx import Resource

from cv.utils import get_cv_data


class BaseResource(Resource):
    """
    A base resource for retrieving CV data sections.

    This class extends Flask-RESTx's `Resource` and is
    intended to serve as a foundational class for API
    endpoints that fetch specific sections of CV data.
    """

    def get(self, section_name: str) -> Response:
        """
        Fetch and return the specified section of CV data.
        """

        data = get_cv_data(section_name)
        return jsonify(data)
