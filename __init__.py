from mycroft import MycroftSkill, intent_file_handler


class CryptoTicker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ticker.crypto.intent')
    def handle_ticker_crypto(self, message):
        self.speak_dialog('ticker.crypto')


def create_skill():
    return CryptoTicker()

