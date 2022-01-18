from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_toml = toml.loads(content)

        project_name = parsed_toml['tool']['poetry']['name']
        project_description = parsed_toml['tool']['poetry']['description']
        project_dependencies = list(parsed_toml['tool']['poetry']['dependencies'])
        project_dev_dependencies = list(parsed_toml['tool']['poetry']['dev-dependencies'])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(project_name, project_description, project_dependencies, project_dev_dependencies)
