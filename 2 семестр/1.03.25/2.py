from string import digits, ascii_lowercase


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return '\n'.join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    chars = "абвгдеёжзийклмнопрстуфхцчшщьъэюя" + ascii_lowercase
    chars_correct = chars + chars.upper() + digits

    def __init__(self, name_, size_):
        self.check_name(name_)
        self.name = name_
        self.size = size_

    def get_html(self):
        return f"<p class='login'><{self.name}>: <input type='text' size=<{self.size}> />"

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 15:
            raise ValueError("Некорректное поле name")
        for i in name:
            if i not in cls.chars_correct:
                raise ValueError("Некорректное поле name")


class PasswordInput:
    chars = "абвгдеёжзийклмнопрстуфхцчшщьъэюя" + ascii_lowercase
    chars_correct = chars + chars.upper() + digits

    def __init__(self, name_, size_):
        self.check_name(name_)
        self.name = name_
        self.size = size_

    def get_html(self):
        return f"<p class='password'><{self.name}>: <input type='text' size=<{self.size}> />"

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 15:
            raise ValueError("Некорректное поле name")
        for i in name:
            if i not in cls.chars_correct:
                raise ValueError("Некорректное поле name")


login = FormLogin(TextInput('AWUhuh90', 10), PasswordInput('Password', 15))
html = login.render_template()
print(html)
