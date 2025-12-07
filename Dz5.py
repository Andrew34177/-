import random

def generator_paroley(length, special_symbols, capital_letters, lower_letters, numbers):
    generator = ""
    char_pool = list(special_symbols + capital_letters + lower_letters + numbers)
    for _ in range(length):
        generator += random.choice(char_pool)
    def check_password(generator):
        if len(generator) < 8:
            print("Ваш пароль слишком короткий.")
        elif (not any(x in special_symbols for x in generator)
              and not any(x in capital_letters for x in generator)
              and not any(x in numbers for x in generator)):
            print("Очень слабый пароль! Добавьте специальные символы, заглавные буквы или цифры.")
        elif (not any(x in capital_letters for x in generator)
              and (any(x in numbers for x in generator) or any(x in special_symbols for x in generator))):
            print("Неплохо, но рекомендуется добавить заглавные буквы.")
        elif not any(x in special_symbols for x in generator):
            print("В пароле нет специальных символов — лучше их добавить.")
        elif not any(x in numbers for x in generator):
            print("Хороший пароль, но стоит добавить цифры.")
        else:
            print("Отличный пароль!")
    check_password(generator)
    return generator
generated = generator_paroley(9, "*!$", "AFV", "acbef", "124124")
print("Сгенерированный пароль:", generated)