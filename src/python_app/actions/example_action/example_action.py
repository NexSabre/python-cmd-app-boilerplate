from python_app.actions.action import Action


class ExampleAction(Action):
    ACTION = "version"

    def fill_parser_arguments(self):
        pass

    def process_action(self, configuration):
        print("Example action")
