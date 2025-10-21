def validar_email_simple(e):
    return '@' in e and '.' in e.split('@')[-1]

print(validar_email_simple('a@b.com'))
