from .base import PyMe


class Project(PyMe):

    def get_user_projects(self):
        """ Get all applications associated to a project """

        endpoint = f"/projects"
        return self._call_api('get', endpoint)

    def create_project(self, json_data):
        """ Create a new project """

        endpoint = f"/projects"
        return self._call_api('post', endpoint, json_data)

    def update_project(self, json_data):
        """ Update a project """

        endpoint = f"/projects"
        return self._call_api('put', endpoint, json_data)

    def remove_project(self):
        """ Remove a project """

        endpoint = f"/projects"
        return self._call_api('delete', endpoint)

    def create_application_under_project(self, project_id, json_data):
        """ Save an application under your project """

        endpoint = f"/projects/{project_id}/applications"
        return self._call_api('post', endpoint, json_data)

    def remove_application_under_project(self, project_id):
        """ Remove an application from your project """

        endpoint = f"/projects/{project_id}/applications"
        return self._call_api('delete', endpoint)
