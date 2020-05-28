import pygame


class Assets:
    """Przechowuje zasoby."""

    @staticmethod
    def load():
        """Wczytuje zasoby z dysku."""
        Assets.FLAGA_OBRAZ = pygame.image.load('img/flaga.png')
        Assets.PYTAJNIK_OBRAZ = pygame.image.load('img/pytajnik.png')
        Assets.RESET_OBRAZ = pygame.image.load('img/retry.png')

