import logger
import FileRender
try:
  FileRender.register_substitution('libname', 'testLib')
  FileRender.register_substitution('username', 'fuleco')
  FileRender.renderFile('./test.h', 'lib.h')

  FileRender.clear_substitutions()

  FileRender.register_substitution('libname', 'testLib')
  FileRender.renderFile('./fail_test.h/', 'lib.h')

except FileRender.FileRenderError as fre:
  logger.error(fre)
  exit(1)