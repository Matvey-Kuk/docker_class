from django import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        label="Логин",
        error_messages={'required': 'Это поле необходимо заполнить.'}
    )

    password = forms.CharField(
        label="Пароль",
        error_messages={'required': 'Это поле необходимо заполнить.'},
        widget=forms.PasswordInput()
    )

    error_messages = {
        'invalid_login': "Пожалуйста, проверьте логин и пароль. "
                         "Обратите внимание, что логин и пароль чувствительны к регистру.",
        'inactive': "Аккаунт деактивирован.",
    }


class CustomSetPasswordForm(SetPasswordForm):
    minimal_password_length = 6

    error_messages = {
        'password_mismatch': "Введенные пароли не совпадают",
        'password_length_not_enough': "Пароль должен иметь минимальную длинну: " + str(minimal_password_length),
    }

    new_password1 = forms.CharField(label="Новый пароль",
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Подтверждение нового пароля",
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < self.minimal_password_length:
                raise forms.ValidationError(
                    self.error_messages['password_length_not_enough'],
                    code='password_length_not_enough',
                )
        return super(CustomSetPasswordForm, self).clean_new_password2()
