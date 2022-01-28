import pygame
import pygame_gui
from pygame_gui import UIManager
from pygame_gui.core import IncrementalThreadedResourceLoader, ObjectID
from pygame_gui.elements import UIWindow
from src.names import first_name

from src.creatures import *

pygame.init()
pygame.display.set_caption('Arcana 4x')
screen_size = (1820, 880)
screen = pygame.display.set_mode(screen_size)

loader = IncrementalThreadedResourceLoader()

world_map = pygame.image.load('assets/textures/TestMap.png')

ui_manager = UIManager(screen_size, 'assets/textures/themes/theme_1.json', resource_loader=loader)

# UI Top panel

characters_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (125, 50)),
                                                 text='Characters',
                                                 manager=ui_manager)

components_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((125, 0), (125, 50)),
                                                 text='Components',
                                                 manager=ui_manager)

economy_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 0), (125, 50)),
                                              text='Economy',
                                              manager=ui_manager)

magic_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((375, 0), (125, 50)),
                                            text='Magic',
                                            manager=ui_manager)

religion_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 0), (125, 50)),
                                               text='Religion',
                                               manager=ui_manager)

military_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((625, 0), (125, 50)),
                                               text='Military',
                                               manager=ui_manager)

# UI Menus

character_window = UIWindow(rect=pygame.Rect((520, 190), (500, 500)),
                            manager=ui_manager,
                            object_id=ObjectID('#charater_window'),
                            window_display_title='Characters',
                            visible=False,)

TestKnight = Knight()
print("My name is: " + first_name())
print("My race is: " + str(Knight.character_race))
print("My Strength is: " + str(Knight.strength))
print("My Reflex is: " + str(Knight.reflex))
print("My Intellect is: " + str(Knight.intellect))
print("My Cunning is: " + str(Knight.cunning))
print("Am I magical: " + str(Knight.is_magical))
print("Am I divine: " + str(Knight.is_divine))
print("")

TestCleric = Cleric()
print("My name is: " + first_name())
print("My race is: " + str(Cleric.character_race))
print("My Strength is: " + str(Cleric.strength))
print("My Reflex is: " + str(Cleric.reflex))
print("My Intellect is: " + str(Cleric.intellect))
print("My Cunning is: " + str(Cleric.cunning))
print("Am I magical: " + str(Cleric.is_magical))
print("Am I divine: " + str(Cleric.is_divine))
print("")

TestGovernor = Governor()
print("My name is: " + first_name())
print("My race is: " + str(Governor.character_race))
print("My Strength is: " + str(Governor.strength))
print("My Reflex is: " + str(Governor.reflex))
print("My Intellect is: " + str(Governor.intellect))
print("My Cunning is: " + str(Governor.cunning))
print("Am I magical: " + str(Governor.is_magical))
print("Am I divine: " + str(Governor.is_divine))
print("")

TestMage = Mage()
print("My name is: " + first_name())
print("My race is: " + str(Mage.character_race))
print("My Strength is: " + str(Mage.strength))
print("My Reflex is: " + str(Mage.reflex))
print("My Intellect is: " + str(Mage.intellect))
print("My Cunning is: " + str(Mage.cunning))
print("Am I magical: " + str(Mage.is_magical))
print("Am I divine: " + str(Mage.is_divine))

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == characters_button:
                character_window.show()

    ui_manager.process_events(event)

    ui_manager.update(time_delta)

    screen.blit(world_map, (0, 0))
    ui_manager.draw_ui(screen)

    ui_manager.update(0)
    pygame.display.update()

# Icons by Zhatelier
# civilization_icon = pygame.image.load('graphics/buttons/civilization.png').convert_alpha()
# components_icon = pygame.image.load('graphics/buttons/component.png').convert_alpha()
# magic_icon = pygame.image.load('graphics/buttons/ritual_circle.png').convert_alpha()
# economy_icon = pygame.image.load('graphics/buttons/economy.png').convert_alpha()
# military_icon = pygame.image.load('graphics/buttons/military.png').convert_alpha()
# religion_icon = pygame.image.load('graphics/buttons/religion.png').convert_alpha()
