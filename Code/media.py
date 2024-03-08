from pynput.keyboard import Controller, KeyCode, Key
import time

#each key pressed is a special windows macro key for windows

class media:
    def __init__(self):
        self.keyboard = Controller()
    def pause(self):
        self.keyboard.press(KeyCode.from_vk(0xB3))
    def previous(self):
        self.keyboard.press(KeyCode.from_vk(0xB1))
    def next(self):
        self.keyboard.press(KeyCode.from_vk(0xB0))
    def mute(self):
        self.keyboard.press(KeyCode.from_vk(0xAD))
    def volUp(self, nr = None):
        if nr == None:
            self.keyboard.press(KeyCode.from_vk(0xAF))
        else:
            for _ in range(int(nr/2)):
                self.keyboard.press(KeyCode.from_vk(0xAF))
                time.sleep(0.05)
    def volDw(self, nr = None):
        if nr == None:
            self.keyboard.press(KeyCode.from_vk(0xAE))
        else:
            for _ in range(int(nr/2)):
                self.keyboard.press(KeyCode.from_vk(0xAE))
                time.sleep(0.05)

if __name__ == "__main__":
    media().volDw(25)

