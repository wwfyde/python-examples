from jinja2 import Template

my_template = "hello, {{ user }}!"


def render_template(template_str: str, context: dict) -> str:
    template = Template(template_str)
    return template.render(context)


output = render_template(
    template_str=my_template, context=dict(user="world")
)  # Output: hello, world

print(output)
