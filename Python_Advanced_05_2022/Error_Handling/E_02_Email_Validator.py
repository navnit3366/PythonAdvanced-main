class NameTooShortError(Exception):
    """
    Raised, when the name in the email is less than or equal to 4
    ("peter" will be the name in the email "peter@gmail.com")
    """
    pass


class MustContainAtSymbolError(Exception):
    """
    Raised when there is no "@" in the email.
    """
    pass


class InvalidDomainError(Exception):
    """
    Raised when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
    """
    pass


while True:
    input_string = input()
    if "@" not in input_string:
        raise MustContainAtSymbolError("Email must contain @")
    email_input = input_string.split("@")
    name = email_input[0]
    host = email_input[1]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    domain = host.split('.')[1]
    if domain not in ["com", "bg", "org"]:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
