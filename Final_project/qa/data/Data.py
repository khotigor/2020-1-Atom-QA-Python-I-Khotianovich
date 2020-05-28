"""
Valid and invalid data for tests
user names, passwords, emails
and some generators
"""

""" Registration invalid data UI"""
# bad user names to check registration page
USER_BAD1 = 'imnumb?erone'
USER_BAD2 = 'q'
USER_BAD3 = '123456789101112'

# bad emails to check registration page
EMAIL_BAD1 = '@bk.ru'
EMAIL_BAD2 = 'bad@.ru'
EMAIL_BAD3 = 'bad@bk.r'

# passwords
PASSWORD_BAD1 = 'q'
PASSWORD_BAD2 = 'qwerasdf'
PASSWORD_BAD3 = '12345678'

""" Registration invalid data API"""
# bad user names to check registration page
USER_BAD1_API = 'imnumb?eroneAPI'
USER_BAD2_API = 'p'
USER_BAD3_API = '12345678910'

# bad emails to check registration page
EMAIL_BAD1_API = '@mail.ru'
EMAIL_BAD2_API = 'badapi@.ru'
EMAIL_BAD3_API = 'badapi@bk.r'

# passwords
PASSWORD_BAD1_API = 'p'
PASSWORD_BAD2_API = 'pwerasdf'
PASSWORD_BAD3_API = '123456789'