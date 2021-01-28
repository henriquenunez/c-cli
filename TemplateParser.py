import yaml

def readTemplate(name: str):
  with open(f'templates/{name}.yaml') as templateFile:
    template = yaml.safe_load(templateFile)

  return template['metadata'], template['defs'], template['project']
