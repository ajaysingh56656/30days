class Template:
    data = 'data'
    another_data = 'another_data'
    print(f'data: {data} : {id(data)}')
    print(f'another_data: {another_data} : {id(another_data)}')

    def __init__(self, data='a', another_data='a'):
        self.data = data
        self.my = another_data
        print(f'self.data: {self.data} {id(self.data)}')
        print(f'self.my: {self.my} {id(self.my)}')
        print(f'self.another_data: {self.another_data} {id(self.another_data)}')
        print(f'Template.another_data: {Template.another_data} {id(Template.another_data)}')
        print(f'Template.template: {Template.data} {id(Template.data)}')
        print('*' * 20)


x = Template.data
print(f'Template.data: {x} : {id(x)}')
a = Template()
y = a.data
z = a.another_data
print(f'Template().data: {y} : {id(y)}')
print(f'Template().another_data: {z} : {id(z)}')
