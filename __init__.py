from mycroft import MycroftSkill, intent_file_handler


class VolumioController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('controller.volumio.intent')
    def handle_controller_volumio(self, message):
        self.speak_dialog('controller.volumio')


def create_skill():
    return VolumioController()

