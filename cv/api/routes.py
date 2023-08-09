from flask import Blueprint
from flask_restx import Api

from cv.api.base import BaseResource

api_bp = Blueprint("api", __name__)
api = Api(
    api_bp,
    version="1.0",
    title="Cegeka assignment - CV API Service",
    description="API documentation for getting data from a CV",
)

ns_personal = api.namespace("personal", description="Personal data operations")
ns_experience = api.namespace("experience", description="Experience operations")
ns_education = api.namespace("education", description="Education operations")


@ns_personal.route("/")
class PersonalDataResource(BaseResource):
    """
    Resource representing the personal data section of the CV.

    This class extends the BaseResource to specifically cater to
    the personal data section of the CV.
    """

    def get(self, **kwargs):
        """
        Retrieve the personal data section of the CV.
        """

        return super().get("personal")


@ns_experience.route("/")
class ExperienceResource(BaseResource):
    """
    Resource representing the experience section of the CV.

    This class extends the BaseResource to specifically cater to
    the experience section of the CV.
    """

    def get(self, **kwargs):
        """
        Retrieve the experience section of the CV.
        """

        return super().get("experience")


@ns_education.route("/")
class EducationResource(BaseResource):
    """
    Resource representing the education section of the CV.

    This class extends the BaseResource to specifically cater to
    the education section of the CV.
    """

    def get(self, **kwargs):
        """
        Retrieve the education section of the CV.
        """

        return super().get("education")
