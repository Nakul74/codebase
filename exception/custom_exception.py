import sys

def error_details():
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    function_name = exc_tb.tb_frame.f_code.co_name
    line_number = exc_tb.tb_lineno
    return file_name, function_name, line_number

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message
        self.file_name, self.function_name, self.line_number = error_details()

    def __str__(self):
        return "Error occurred in file '{0}', function '{1}', at line {2}: {3}".format(
            self.file_name, self.function_name, self.line_number, self.error_message
        )