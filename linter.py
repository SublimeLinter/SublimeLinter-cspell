from SublimeLinter.lint import Linter, STREAM_STDOUT


class CSpell(Linter):
    cmd = 'cspell stdin://${file}'
    defaults = {'selector': 'source'}
    regex = r'^(?P<filename>(\S:)?[^:]*):(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)$'
    error_stream = STREAM_STDOUT
