import winzy


# An example plugin implementation.

class HelloWorld:
    __name__ = "{{cookiecutter.entry_name}}"

    @winzy.hookimpl
    def register_commands(self, subparser):
        parser = subparser.add_parser("{{cookiecutter.entry_name}}", description="{{ cookiecutter.description or "" }}")
        # Add subprser arguments here.
        parser.set_defaults(func=self.hello)
    
    def hello(self, args):
        # this routine will be called when "winzy "{{cookiecutter.entry_name}} is called."
        print("Hello! This is an example ``winzy`` plugin.")

{{cookiecutter.entry_name}}_plugin = HelloWorld()
