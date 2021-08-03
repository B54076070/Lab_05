import pygame
import os


pygame.init()
UpgradeMenu_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
Upgrade_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
Sell_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(UpgradeMenu_IMAGE, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__upgrademenu = []
        self.__expedition = []
        #self.botton = Button()
        self.__buttons = [pygame.transform.scale(Upgrade_IMAGE, (30, 60)),
                          pygame.transform.scale(Sell_IMAGE, (30, 30))]  # (Q2) Add buttons here
        pass


    def draw(self, win):
        # draw menu
        win.blit(self.image, (180, 300))
        win.blit(self.image, (340, 320))
        win.blit(self.image, (520, 310))

        # draw button
        #self.botton.draw(self.win)

        pygame.display.update()
        pygame.event.get()

        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        # draw button
        # (Q2) Draw buttons here
        # for um in self.__expedition:
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name




    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        pass





