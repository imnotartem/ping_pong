from function import *

window = pygame.display.set_mode((setting_win['WIDTH'], setting_win['HEIGHT']))
pygame.display.set_caption("Пінг Понг")

def run():
    game = True

    player_left = Board(10,
                        setting_win['HEIGHT'] // 2 - setting_board['HEIGHT'] // 2,
                        setting_board['WIDTH'],
                        setting_board['HEIGHT'],
                        )

    clock = pygame.time.Clock()

    while game:
        events = pygame.event.get()

        window.fill((50,190,0))
        pygame.draw.line(window, (255,255,255),
                          (setting_win['WIDTH'] // 2 - 1, 0),
                          (setting_win['WIDTH'] // 2 - 1, setting_win['HEIGHT']),
                          2)
        player_left.move(window)

        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_left.MOVE['UP'] = True
                if event.key == pygame.K_s:
                    player_left.MOVE['DOWN'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player_left.MOVE['UP'] = False  
                if event.key == pygame.K_s:
                    player_left.MOVE['DOWN'] = False

        clock.tick(setting_win['FPS'])
        pygame.display.flip()

run()




