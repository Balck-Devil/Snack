import pygame
import random
pygame.init()

# Color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

screen_width=900
screen_height=600
gamewindow=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Catch The Food")
pygame.display.update()



clock=pygame.time.Clock()
font=pygame.font.SysFont(None,30)

def plot_snk(gamewindow,Color,snk_list,snack_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,Color,[x,y,snack_size,snack_size])



def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def gameloop():
    exit_game=False
    game_over=False
    snack_x=45
    snack_y=45
    valocity_x=0
    valocity_y=0
    init_valocity=5
    snack_size=10
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    fps=30
    score=0
    snk_list=[]
    snk_lenth=1
    while not exit_game:
        if game_over:
            gamewindow.fill(white)
            text_screen("Game Over! Enter To Start",red,screen_width/2,screen_height/2)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()


        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                        valocity_x=init_valocity
                        valocity_y=0
                    
                if event.key==pygame.K_LEFT:
                        valocity_x=-init_valocity
                        valocity_y=0
                    
                if event.key==pygame.K_UP:
                        valocity_y=-init_valocity
                        valocity_x=0
                    
                if event.key==pygame.K_DOWN:
                        valocity_y=init_valocity
                        valocity_x=0
                    
                    
            snack_x=snack_x+valocity_x
            snack_y=snack_y+valocity_y

            if abs(snack_x-food_x)<6 and abs(snack_y-food_y)<6:
                score+=1
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                # print("My Score Is :- ",score*10)
                snk_lenth+=4

            gamewindow.fill(white)
            text_screen("Score :"+str(score*10),red,5,5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snack_size,snack_size])
            
            head=[]
            head.append(snack_x)
            head.append(snack_y)
            snk_list.append(head)

            if len(snk_list)>snk_lenth:
                del snk_list[0]

            if snack_x<0 or snack_x>screen_width or snack_y<0 or snack_y>screen_height:
                game_over=True
                print("Game Over")


            # pygame.draw.rect(gamewindow,black,[snack_x,snack_y,snack_size,snack_size])
            plot_snk(gamewindow,black,snk_list,snack_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
                

gameloop()