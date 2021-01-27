import re
import datetime
from os import remove, path as Path

import logger

_substitutions = {}

class FileRenderError(Exception):
  pass

def register_substitution(name: str, value: any):
  """Register a substitution keys to be used in rendering

  Args:
      name (str): Substitution key.
      value (any): Value to substitute when key appers in template.
  """
  _substitutions[name] = value

def clear_substitutions():
  """Clears all substitution keys. Defaults are recreated.
  """
  _substitutions.clear()

def renderFile(path: str, templateName: str):
  """Gets the template and renders the substitutions to a new file

  Args:
      path (str): path to where the rendered file will be saves.
      templateName (str): template name.

  Default substitution keys:
      'now' (str): ISO Date and time of rendering.
      'fileName' (str): Filename automatically detected from 'path'.

  Raises:
      NameError: Raises if template has a substitution key that has no value defined.
  """
  # Define constants
  _substitutions['now'] = datetime.datetime.now().isoformat()
  fileNameResul = re.search(r'/?([a-zA-Z_\-\d ]+)$', path)

  # File checks
  if Path.isfile(path):
    raise FileRenderError(f'File {path} already exists.')
  if fileNameResul == None:
    raise FileRenderError(f'"path=[{path}]" is not a valid path.')
  fileName = fileNameResul.groups()[0]
  _substitutions['fileName'] = fileName

  # Start rendering file
  logger.info(f'Started rendering files...')
  with open(f'file_templates/{templateName}') as template:
    with open(path, 'wt') as output:
      lineNum = 0
      for line in template:
        lineNum += 1

        for name in _substitutions:
          line = re.sub(f'<%{name}%>', _substitutions[name], line)

        # Check if there was a missed substitution key
        has_left = re.search(r'<%([a-zA-Z\d]*)%>', line)
        if has_left != None:
          key = has_left.groups()[0]
          start = has_left.span()[0]
          end = has_left.span()[1]
          output.close()
          remove(path)
          raise FileRenderError(f'Key "{key}" appeared in template but was not given a substitution value [@line {lineNum}: cols {start} -> {end}]')

        output.write(line)
        print('Rendering' + ('.' * (lineNum%4) + (' ' * (3 - lineNum%4))), f'{lineNum} lines rendered', end='\r\033[K')

  logger.success(f'File rendered!')