import logger
import TemplateParser
import ProjectBuilder

metadata, defs, project = TemplateParser.readTemplate('basic')
first = ProjectBuilder.parseProject(project)
second = ProjectBuilder.parseProject(['a', 'b', 'c'])
try:
  failed = ProjectBuilder.parseProject([1,2,3])
except ProjectBuilder.ProjectParsingError as e:
  logger.error(e)
  exit(1)

print(first)
print(second)