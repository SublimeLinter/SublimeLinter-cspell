from SublimeLinter.lint import Linter, STREAM_STDOUT


class CSpell(Linter):
    cmd = 'cspell stdin://${file}'
    defaults = {'selector': 'source'}
    regex = r'^(?P<filename>(stdin:(///)?)?(\S:)?[^:]*):(?P<line>\d+):(?P<col>\d+) - (?P<message>.*)$'
    error_stream = STREAM_STDOUT

    @staticmethod
    def is_stdin_filename(filename: str) -> bool:
        return True
