def test_function():

    def inner_function():
        print("Я в бласти видимой функции test_function")

    inner_function()

# inner_function() - Не может быть вызвана, т.к. она локальная и ее область видимости ограничена test_function
test_function()


