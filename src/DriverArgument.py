

class DriverArgument:

  def __init__(self) -> None:
    self.action: str = None

    self.pl_project: dict = None
    self.pl_projects: list = None
    self.pl_field: str = None

    self.o_lim: bool = None
    self.o_quit: bool = None

     

  def parse():
    """"""

  def get_payload():
    """ Returns a proper Payload dictionary """

  def set_payload():
    """ Creates a proper Payload dictionary """

  def get_options():
    """ Returns a proper Options dictionary """

  def set_options():
    """ Creates a proper Options dictionary """

  def get_action(self) -> str:
    """ Returns the action this DriverArgument holds """
    return self.action

  def get_project(self) -> dict:
    """"""
    return self.pl_project

  def get_projects(self) -> dict:
    """"""
    return self.pl_projects

  def make_start(self, project: dict, limited: bool, quit: bool):
    """ Creates a proper DriverArgument configured for driver start """
    self.action = "START"
    self.pl_project = project
    self.o_lim = False if limited == None else limited
    self.o_quit  = False if limited == None else limited

  def make_add(self, project: dict, projects: list):
    """ Creates a proper DriverArgument configured for driver add """
    self.action = "ADD"
    self.pl_project = project
    self.pl_projects = projects

  def make_rm(self, project: dict, projects: list):
    """ Creates a proper DriverArgument configured for driver remove """
    self.action = "RM"
    self.pl_project = project
    self.pl_projects = projects

  def make_edit(self, project: dict, projects: list, field: str):
    """ Creates a proper DriverArgument configured for driver edit """
    self.action = "EDIT"
    self.pl_project = project
    self.pl_projects = projects
    self.pl_field = field