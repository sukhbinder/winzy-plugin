import winzy


def create_parser(subparser):
    parser = subparser.add_parser("{{cookiecutter.entry_name}}", description="{{ cookiecutter.description or "" }}")
    # Add subprser arguments here.
    parser.add_argument("-test", "--test", type=str, help="Example argument")
    return parser


class WinzyPlugin:
    """ {{ cookiecutter.description or "" }} """
    __name__ = "{{cookiecutter.entry_name}}"

    @winzy.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # add actual call here
        pass
    
    def hello(self, args):
        # this routine will be called when 'winzy {{cookiecutter.entry_name}}' is called.
        print("Hello! This is an example ``winzy`` plugin.")

{{cookiecutter.entry_name}}_plugin = WinzyPlugin()
