import FileRender
FileRender.register_substitution('libname', 'testLib')
FileRender.register_substitution('username', 'fuleco')
FileRender.renderFile('./test.h', 'lib.h')

FileRender.clear_substitutions()

FileRender.register_substitution('libname', 'testLib')
FileRender.renderFile('./fail_test.h', 'lib.h')