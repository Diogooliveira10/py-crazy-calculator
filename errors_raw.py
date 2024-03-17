class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print('')
    raise HttpUnprocessableEntityError('')
except Exception as exception:
    print('')
    print(exception.name)
    print(exception.status_code)
    print(exception.message)