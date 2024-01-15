from st2common.runners.base_action import Action

class HelloStackStorm(Action):
    def run(self):
        print("Hello Stackstorm")
        return True, "Got Alert from nagios"
