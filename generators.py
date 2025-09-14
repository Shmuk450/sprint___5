import random
import string

def gen_email(first="test", last="student", cohort="1999", domain="yandex.ru"):
    """Логин = email в формате имя_фамилия_номерКогорты_3цифры@домен"""
    tail = random.randint(100, 999)
    return f"{first}{last}{cohort}_{tail}@{domain}"

def gen_password(length=8):
    """Минимум 6 символов"""
    length = max(6, length)
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))