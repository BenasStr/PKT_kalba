import beanplusminus

while True:
    text = input('beanshell > ')
    result, error = beanplusminus.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
