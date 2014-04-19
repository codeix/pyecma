class EcmaException(Exception):
    pass


class ReferenceError(EcmaException):
    pass


class ArgumentError(EcmaException):
    pass


class TypeError(EcmaException):
    pass