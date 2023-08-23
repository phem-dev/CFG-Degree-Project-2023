import pygame


def draw_rounded_rect(surface, color, rect, corner_radius):
    """Draws a rounded rectangle on the given surface."""
    pygame.draw.rect(surface, color, (rect.x, rect.y + corner_radius, rect.width, rect.height - 2 * corner_radius))
    pygame.draw.rect(surface, color, (rect.x + corner_radius, rect.y, rect.width - 2 * corner_radius, rect.height))

    pygame.draw.circle(surface, color, (rect.left + corner_radius, rect.top + corner_radius), corner_radius)  # top-left
    pygame.draw.circle(surface, color, (rect.right - corner_radius, rect.top + corner_radius),
                       corner_radius)  # top-right
    pygame.draw.circle(surface, color, (rect.left + corner_radius, rect.bottom - corner_radius),
                       corner_radius)  # bottom-left
    pygame.draw.circle(surface, color, (rect.right - corner_radius, rect.bottom - corner_radius),
                       corner_radius)  # bottom-right
