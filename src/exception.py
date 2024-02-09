import sys
import logging

# Function to generate detailed error message
def error_message_detail(error, error_detail: sys):
    # Extracting information about the error
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Constructing the error message with file name, line number, and error description
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class that captures detailed error information
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent class's constructor to initialize the exception with a message
        super().__init__(error_message)
        # Generate detailed error message using the provided error message and error detail
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # Override the __str__ method to return the custom error message
    def __str__(self):
        return self.error_message





'''
The purpose of the provided Python file seems to be to create a custom exception class (CustomException) that captures detailed error information including the file name, line number, and error message. This can be particularly useful in scenarios where you want to raise exceptions with more context, aiding in debugging and error tracing.

Here's a breakdown of the main components and their purposes:

error_message_detail function: This function takes an error message and error detail (likely obtained from sys.exc_info()) and generates a detailed error message string including the file name, line number, and error description.

CustomException class: This class inherits from the built-in Exception class and serves as a custom exception type. When instantiated, it captures the provided error message and detail, then generates a detailed error message using the error_message_detail function. It overrides the __str__ method to return the custom error message.

The file may be used wherever custom exceptions with detailed error information are required. For example, in larger projects or frameworks where it's necessary to provide more context when handling exceptions.

Overall, the purpose of this file is to enhance error handling by providing custom exceptions with detailed error information, which can facilitate debugging and troubleshooting of Python programs.
'''
