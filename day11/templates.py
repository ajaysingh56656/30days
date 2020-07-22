import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIRS = os.path.join(BASE_DIR, 'templates')
os.makedirs(TEMPLATE_DIRS, exist_ok=True)


class Template:

    def __init__(self, template_name='', context=None, *args, **kwargs):
        self.template_name = template_name
        self.context = context

    def get_template(self):
        template_path = os.path.join(TEMPLATE_DIRS, self.template_name)
        if not self.template_name:
            raise Exception('File name is not given.')
        if not os.path.exists(template_path):
            raise Exception('This path does not exist.')
        with open(template_path, 'r') as f:
            template_string = f.read()
        return template_string

    def render(self, context=None):
        render_ctx = context
        if self.context:
            render_ctx = self.context
        if not isinstance(render_ctx, dict):
            render_ctx = {'name': 'User'}
        template_string = self.get_template()
        return template_string.format(**render_ctx)


# if __name__ == '__main__':
#     a = Template('hello.txt', {'name': 'ajay'})
#     print(a.render())
