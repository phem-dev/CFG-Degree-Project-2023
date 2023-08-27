import pygame


def draw_rounded_rect(surface, color, rect, corner_radius):
    """
    Draws a rounded rectangle on a given pygame surface.

    This function draws a rectangle with rounded corners by combining straight rectangle shapes
    and circular shapes for the corners on the given surface.

    Parameters:
    - surface (pygame.Surface): The surface on which the rounded rectangle is drawn.
    - color (Tuple[int, int, int]): An RGB tuple representing the color of the rounded rectangle.
    - rect (pygame.Rect): A rectangle object that defines the position and size of the rounded rectangle.
                          It contains x, y, width, and height attributes.
    - corner_radius (int): The radius of the rounded corners.

    Note:
    If the corner_radius is too large for the given rect dimensions, the behavior might be unpredictable.

    Example:
    draw_rounded_rect(screen, (255, 0, 0), pygame.Rect(50, 50, 200, 100), 20)
    This will draw a red rounded rectangle at (50, 50) of width 200 and height 100 with corners of radius 20.

    """
    pygame.draw.rect(surface, color, (rect.x, rect.y + corner_radius, rect.width, rect.height - 2 * corner_radius))
    pygame.draw.rect(surface, color, (rect.x + corner_radius, rect.y, rect.width - 2 * corner_radius, rect.height))

    pygame.draw.circle(surface, color, (rect.left + corner_radius, rect.top + corner_radius), corner_radius)  # top-left
    pygame.draw.circle(surface, color, (rect.right - corner_radius, rect.top + corner_radius),
                       corner_radius)  # top-right
    pygame.draw.circle(surface, color, (rect.left + corner_radius, rect.bottom - corner_radius),
                       corner_radius)  # bottom-left
    pygame.draw.circle(surface, color, (rect.right - corner_radius, rect.bottom - corner_radius),
                       corner_radius)  # bottom-right
