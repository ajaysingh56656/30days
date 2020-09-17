import fire

def hello(name='world'):
    return f'hello {name}'

if __name__ == "__main__":
    fire.Fire(hello)
