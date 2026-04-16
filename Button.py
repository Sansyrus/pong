import pygame

class Button:
    def __init__(self, x, y, width, height, text, color=(90,90,100), 
                 hover_color=(140,140,150), text_color=(255,255,255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.SysFont('Arial', 28)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            couleur = self.hover_color
        else : 
            couleur = self.color
        pygame.draw.rect(screen, couleur, self.rect, border_radius=8)
        pygame.draw.rect(screen, (255,255,255), self.rect, width=1, border_radius=8)

        surf_text = self.font.render(self.text, True, self.text_color)
        screen.blit(surf_text, surf_text.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
        return False