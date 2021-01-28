import os
from FileRender import renderFile

class ProjectParsingError(Exception):
    pass


__actionQueue = []


class __Action:
    def __init__(self, action: str, name: str):
        self.action = action
        self.name = name

    def __repr__(self):
        return f'Create folder({self.name}/)' if self.action == 'folder' else f'Create file({self.name}:{self.action})'


def __pushFolder(name: str):
    __actionQueue.append(__Action('folder', name))


def __pushFile(name: str, file_template: str):
    __actionQueue.append(__Action(file_template, name))


def __parseList(parseList: list, path_till_now: str):
    for item in parseList:
        if isinstance(item, str):
            __pushFolder(path_till_now + item)
        elif isinstance(item, dict):
            key, value = item.popitem()
            if isinstance(value, str):
                __pushFile(path_till_now + key, value)
            elif isinstance(value, list):
                __pushFolder(path_till_now + key)
                __parseList(value, path_till_now + key + '/')
            else:
                raise ProjectParsingError(
                    f'Template has an error: {key} is atributed to a {type(value)} but should be str or list')
        else:
            raise ProjectParsingError(
                f'Template has an error: {item} is of type {type(item)} but should be str or dict')


def parseProject(project: list):
    __actionQueue.clear()
    __parseList(project, '')
    return __actionQueue.copy()

def generateFolder(actions: list, rootPath: str):
  for action in actions:
    if action.action == 'folder':
      os.mkdir(rootPath + action.name)
    else:
      renderFile(rootPath + action.name, action.action)
