import pytest

from cv.settings import CV_DATA_FILEPATH
from cv.utils import get_cv_data, read_cv_data_from_file


class TestUtils:
    def test_read_cv_data(self):
        data = read_cv_data_from_file(CV_DATA_FILEPATH)
        assert "personal" in data
        assert "experience" in data
        assert "education" in data

    def test_read_cv_data_from_invalid_file(self):
        with pytest.raises(ValueError, match=r"Invalid file path provided:.*"):
            read_cv_data_from_file("non_existent_file.json")

    def test_get_cv_data(self):
        invalid_section_name = "invalid_section"

        # Test a valid section
        response = get_cv_data("personal")
        assert "name" in response

        # Test the "full" section
        full_response = get_cv_data()
        assert "personal" in full_response
        assert "experience" in full_response
        assert "education" in full_response

        # Test an invalid section
        error_response = get_cv_data(invalid_section_name)
        assert (
            error_response["error"]
            == f"No data found for section: {invalid_section_name}"
        )
