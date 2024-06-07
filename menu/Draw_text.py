from menu import window


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.window.blit(img, (x, y))

