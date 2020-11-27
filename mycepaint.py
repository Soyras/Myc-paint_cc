import pygame

run = True

def main():
    pygame.init()
    
    taille = (800, 600)
    fenetre = pygame.display.set_mode(taille)

    jeu_en_cours = True
   
    while jeu_en_cours :
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_en_cours = False
      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    jeu_en_cours = False
    
    pygame.quit()
    
if __name__ == "__main__":
        main() 