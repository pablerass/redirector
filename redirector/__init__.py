# -*- coding: utf-8 -*-
"""Module to managed standard output redirection.

All clases are designed to be used in ``with`` modules.
"""
import functools
import sys
from io import StringIO

class StandardOutputRedirector(object):
    """Redirects standard output to a *stream* object.

    :param input_stream:
    """
    def __init__(self, input_stream):
        self.__input_stream = input_stream
        self.__old_stdout = None

    def __enter__(self):
        # Stores current stdout stream
        self.__old_stdout = sys.stdout
        # Redirect output to input_stream
        sys.stdout = self.__input_stream
        return self.__input_stream

    def __exit__(self, type_, value, traceback):
        # Revert stdout modification
        self.__input_stream.close()
        sys.stdout = self.__old_stdout

    def _get_input_stream(self):
        return self.__input_stream


class NullOutputRedirector(StandardOutputRedirector):
    """Redirects stdout to a null stream.

    Usage:

    .. code-block:: python

        with NullOutputRedirector():
            print "Non printed text"
    """
    def __init__(self):
        StandardOutputRedirector.__init__(self, self.__DevNull())

    class __DevNull(object):
        def write(self, lines):
            pass

        def close(self):
            pass


class FileOutputRedirector(StandardOutputRedirector):
    """Redirects stdout to a file.

    Usage:

    .. code-block:: python

        with FileOutputRedirector("redirected_file.txt"):
            print "Text redirected to file."

    :param str file_name: File to redirect de output.
    :param str mode: Access mode to file.
    """
    def __init__(self, file_name, mode = "a"):
        StandardOutputRedirector.__init__(self, open(file_name, mode))


class VariableOutputRedirector(StandardOutputRedirector):
    """Redirect stdout to an ``StringIO`` object that can be used to retrieve
    the content as an string using ``getvalue()`` method.

    Usage:

    .. code-block:: python

        >>> with VariableOutputRedirector() as out:
        >>>     print("texto de prueba")
        >>>     print("otro texto de prueba")
        >>>     value = out.getvalue()

        >>> print value
        texto de prueba
        otro texto de prueba
    """
    def __init__(self):
        StandardOutputRedirector.__init__(self, StringIO())


class FunctionOutputRedirector(StandardOutputRedirector):
    """Uses the stout as a parameter for a function.

    Usage:

    .. code-block:: python

        def alt_print(line):
            print("[alt] " + line)

        with FunctionOutputRedorector(alt_print):
            print "Text redirected to function."

    :param func function: Functino to execute the input.
    """
    def __init__(self, function):
        StandardOutputRedirector.__init__(self, self.__FunctionStream(function))

    class __FunctionStream(object):
        def __init__(self, function)
            self.__function = function

        def write(self, lines):
            for line in lines:
                self.__function(line)

        def close(self):
            pass


class LoggerOutputRedirector(FunctionOutputRedirector):
    """Redirects stdout to a ``logger`` using the specific log level.

    Usage:

    .. code-block:: python

        import logging

        logger = logging.getLogger("request")
        with LoggeLoggeLoggeLoggerileOutputRedirector(logger, logging.INFO):
            print "Text registered as info in logger."

    :param logger logger: Logger to register the output.
    :param int level: Logger register level.
    """
    def __init__(self, logger, level):
        FunctionOutputRedirector.__init__(self, lambda line: logger.log(level, line))
        FunctionOutputRedirector.__init__(self, functools.partial(logger.log, lvl = level))
        #StandardOutputRedirector.__init__(self, self.__LoggerStream(logger, level))


class GeneratorOutputRedirector(StandardOutputRedirector):
    def __init__(self, logger, level):
        StandardOutputRedirector.__init__(self, self.__GeneratorStream())

    class __GeneratorStream(object):
        def write(self, lines):
            for line in lines:
                yield line

        def close(self):
            pass

