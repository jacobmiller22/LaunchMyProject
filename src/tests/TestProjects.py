import unittest
import projects

class TestProjects(unittest.TestCase):
  ###
  # Tests selecting a project from a list of projects 
  ###
  def test_select_project(self):
    projects_list = [
      {
      "title": "Project 1",
      },
      {
      "title": "Project 2",
      },
      {
      "title": "Project 3",
      },
      {
      "title": "Project 4",
      },
      {
      "title": "Project 5",
      },
    ]
    self.assertEqual(projects.select_project(title="Project 2", project_list=projects_list), {
      "title": "Project 2",
      }, "Should be a dict with a single title of 'Project 2'")
if __name__ == '__main__':
  unittest.main()