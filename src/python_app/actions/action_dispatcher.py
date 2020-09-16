from argparse import ArgumentParser

from python_app.actions.example_action.example_action import ExampleAction


class ActionDispatcher:
    ACTION_HANDLERS = [ExampleAction]

    def __init__(self):
        self.parser = ArgumentParser()
        subparsers = self.parser.add_subparsers()
        self.action_handlers = {action_handler.ACTION: action_handler(subparsers) for action_handler in
                                self.ACTION_HANDLERS}

    def process_application(self):
        configuration = self.parser.parse_args()
        try:
            self.action_handlers[configuration.ACTION].process_action(configuration)
        except AttributeError:
            print("Hello world!")
