import click

from cv.utils import get_cv_data


@click.command("cv")
@click.option("--personal", "section", flag_value="personal")
@click.option("--experience", "section", flag_value="experience")
@click.option("--education", "section", flag_value="education")
def cv(section=None):
    """
    Command to print CV data in JSON format.
    """

    print(get_cv_data(section))
