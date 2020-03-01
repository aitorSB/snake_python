from defines import defines
import sys


def update_snake(snake, ventana):
    for x in snake:
        defines.pygame.draw.rect(ventana, defines.COLOR_SNAKE, [x[0] , x[1] , defines.SIZE_SNAKE, defines.SIZE_SNAKE])

def main():
    defines.pygame.init()

    fuente = defines.pygame.font.Font(None, 60)
    
    ventana = defines.pygame.display.set_mode((
        defines.VENTANA_HORIZONTAL, defines.VENTANA_VERTICAL))
    defines.pygame.display.set_caption(defines.TITULO_JUEGO)
    
    jugando = True
    isPaused = False

    eje_x = defines.MITAD_HORIZONTAL
    eje_y = defines.MITAD_VERTICAL

    move_x = 0
    move_y = 0

    points_x = round(defines.random.randrange(0, defines.VENTANA_HORIZONTAL - defines.SIZE_SNAKE) / defines.SIZE_SNAKE) * defines.SIZE_SNAKE
    points_y = round(defines.random.randrange(0, defines.VENTANA_VERTICAL - defines.SIZE_SNAKE) / defines.SIZE_SNAKE) * defines.SIZE_SNAKE

    snake = []
    Longitud_snake = 1

    while jugando:
        
        ventana.fill(defines.COLOR_FONDO)
            
        #eventos -----------------------------------
        for event in defines.pygame.event.get():
            if event.type == defines.pygame.QUIT:
                jugando = False
            if event.type == defines.pygame.KEYDOWN:
                if event.key == defines.pygame.K_p:
                    isPaused = not isPaused
                if event.key == defines.pygame.K_LEFT:
                    move_x = - defines.MOVIMIENTO_SNAKE
                    move_y = 0
                elif event.key == defines.pygame.K_RIGHT:
                    move_x = defines.MOVIMIENTO_SNAKE
                    move_y = 0
                elif event.key == defines.pygame.K_UP:
                    move_y = - defines.MOVIMIENTO_SNAKE
                    move_x = 0
                elif event.key == defines.pygame.K_DOWN:
                    move_y = defines.MOVIMIENTO_SNAKE
                    move_x = 0
    
        #--------------render-------------------------
        
        #points
        defines.pygame.draw.rect(ventana, defines.COLOR_POINTS, [points_x , points_y , defines.SIZE_SNAKE, defines.SIZE_SNAKE])
        #--------------------------------------------

        if isPaused:
            textoPausa = f"{defines.TEXTO_PAUSA}"
            letreroPausa = (fuente.render(textoPausa, False, defines.COLOR_TEXTO))
            ventana.blit(letreroPausa, ((defines.MITAD_HORIZONTAL - int(fuente.size(textoPausa)[0] / 2)), defines.MITAD_VERTICAL))
        else:
            #movimiento constante
            eje_x += move_x
            eje_y += move_y

            if eje_x > defines.VENTANA_HORIZONTAL:
                eje_x = 0
            elif eje_x < 0:
                eje_x = defines.VENTANA_HORIZONTAL
            elif eje_y > defines.VENTANA_VERTICAL:
                eje_y = 0
            elif eje_y < 0:
                eje_y = defines.VENTANA_VERTICAL        

            snake_point = []
            snake_point.append(eje_x)
            snake_point.append(eje_y)
            snake.append(snake_point)
            
            if len(snake) > Longitud_snake:
                del snake[0]

            for x in snake[:-1]:
                if x == snake_point:
                    Longitud_snake -= 1

            update_snake(snake, ventana)
            defines.pygame.display.update()
            
            if eje_x == points_x and eje_y == points_y:
    
                points_x = round(defines.random.randrange(0, defines.VENTANA_HORIZONTAL - defines.SIZE_SNAKE) / defines.SIZE_SNAKE) * defines.SIZE_SNAKE
                points_y = round(defines.random.randrange(0, defines.VENTANA_VERTICAL - defines.SIZE_SNAKE) / defines.SIZE_SNAKE) * defines.SIZE_SNAKE
                Longitud_snake += 1
 
        #--------------------------------------------
        defines.pygame.display.flip()
        defines.pygame.time.Clock().tick(defines.FPS)

    defines.pygame.quit()

if __name__ == "__main__":
    main()