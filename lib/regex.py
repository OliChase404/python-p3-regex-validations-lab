import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^(?!.*\d)[A-Z]{0,}\S{1,}\W[A-Z]{1,}\S{0,}"
name_regex = re.compile(name)

phone_number = r"^\(?([0-9]{3})\)?[- ]?([0-9]{3})[- ]?([0-9]{4})$"
phone_regex = re.compile(phone_number)

email_address = r"\b(?![0-9])\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*\b"
email_regex = re.compile(email_address)
