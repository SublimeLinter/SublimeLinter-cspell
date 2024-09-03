from SublimeLinter.lint import Linter, STREAM_STDOUT


class CSpell(Linter):
    cmd = 'cspell ${temp_file}'
    defaults = {'selector': 'source'}
    regex = r'^(?P<filename>(\S:)?[^:]*):(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)$'
    tempfile_suffix = '.'
    error_stream = STREAM_STDOUT
