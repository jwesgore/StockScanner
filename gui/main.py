
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget


class Toolbar(Widget):

    def homepage(self):
        return Homepage()

    def news(self):
        return News()

    def login(self):
        return Login().show_login()

    def profile(self):
        return Profile()

    def tools(self):
        return Tools()

    def settings(self):
        return Settings()

    def search(self):
        return Search()


class Homepage(Widget):
    pass


class News(Widget):
    pass


class Login(Popup):
    def show_login(self):
        return self.open()

    def submit(self):
        # get username and password text
        username = self.ids.username.text
        password = self.ids.password.text
        dict = {'username': username, 'password': password}

        # check if username and password exists in system

    def fail_login(self):
        pass

    def create_login(self):
        self.dismiss()
        return CreateLogin().show_create_login()


class CreateLogin(Popup):
    def show_create_login(self):
        return self.open()

    def submit(self):
        # get username and password text
        username = self.ids.username.text
        password1 = self.ids.password1.text
        password2 = self.ids.password2.text

        # check if username exists in system already and return true or false
        exists = False
        if exists:
            return Error.errorCode(self, 0)

        # check if passwords match
        if password1 != password2:
            return Error.errorCode(self, 1)

        else:
            dict = {'username': username, 'password': password1}

        return


class Error(Popup):

    # layout = FloatLayout
    # label = Label
    # button = Button(text="okay")

    def username_taken(self):
        pass

    def password_match(self):
        text1 = "Error 1: Passwords do not match"
        Error.show_error(self)

    def show_error(self):
        self.open()

    def dismiss_error(self, instance):
        self.dismiss()

    def errorCode(self, code):

        error = {
            0: Error.username_taken,  # error 0: username already taken
            1: Error.password_match   # error 1: passwords don't match
        }

        return error[code](self)






class Profile(Widget):
    pass


class Tools(Widget):
    pass


class Settings(Widget):
    pass


class Search(Widget):
    pass


class Home(App):
    def build(self):
        return Homepage()


if __name__ == '__main__':
    Home().run()
