from django.core import validators

KEY_REGEX_RAW = r'[\w-]+\.[A-Za-z]{2,4}'
KEY_REGEX = rf'^{KEY_REGEX_RAW}$'

key_validator = validators.RegexValidator(
    KEY_REGEX,
    'enter a valid key',
    'invalid'
)