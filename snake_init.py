from defines import defines

def main():
    defines.pygame.init()
    
    ventana = defines.pygame.display.set_mode((
        defines.VENTANA_HORIZONTAL, defines.VENTANA_VERTICAL))
    defines.pygame.display.set_caption(defines.TITULO_JUEGO)
    
    jugando = True

    while jugando:
        ventana.fill(defines.COLOR_FONDO)

        ##eventos
        for event in defines.pygame.event.get():
            if event.type == defines.pygame.QUIT:
                jugando = False
        
        defines.pygame.draw.rect(ventana, defines.COLOR_SNAKE, [defines.MITAD_HORIZONTAL , defines.MITAD_VERTICAL , defines.SIZE_SNAKE, defines.SIZE_SNAKE])
        defines.pygame.display.flip()
        defines.pygame.time.Clock().tick(defines.FPS)

if __name__ == "__main__":
    main()