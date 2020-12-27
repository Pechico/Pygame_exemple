#CHAINE Bayard WITHOF Maximilien
import pygame
import random
pygame.mixer.init()

H = 0
V = 1

music = pygame.mixer.music.load('sons/theme.mp3')
bouteille = pygame.mixer.Sound('sons/bouteille.mp3')
shark = pygame.mixer.Sound('sons/requin.mp3')
cado = pygame.mixer.Sound('sons/cadeau.mp3')
boule = pygame.mixer.Sound('sons/boulet.mp3')


FENETRE_LARGEUR = 1000
FENETRE_HAUTEUR = 600

fenetre_taille = (FENETRE_LARGEUR, FENETRE_HAUTEUR)
fenetre = pygame.display.set_mode(fenetre_taille)

BLEU  = (9, 132, 227)
EMERAULD  = (46, 204, 113)
EAU = (44, 62, 80)
BRIQUE = (181, 23, 76)
ROUGE = (214, 0, 0)
BRUN = (153, 102, 51)
BRUNF = (127, 66, 5)
JAUNE = (241, 196, 15)
NOIR = (45, 52, 54)
DNOIR = (0,0,0)

MARK1 = EMERAULD
MARK2 = NOIR

BOAT_LARGEUR = 120
BOAT_HAUTEUR = 120
BOAT_DEPLACEMENT = 10

NAGE_COTE = 40
MINE_COTE = NAGE_COTE
LIFE_COTE = 35
BALLE_COTE = 20
EMOTE_COTE = 65

TOUCHE_HAUT = pygame.K_UP
TOUCHE_BAS = pygame.K_DOWN
TOUCHE_A = pygame.K_a
TOUCHE_B = pygame.K_b
ENTER = pygame.K_RETURN
TOUCHE_ESPACE = pygame.K_SPACE

EN_HAUT = -1
EN_BAS = 1

MUR_EPAISSEUR = 10

CENTRE         = 0
GAUCHE         = 1
DROITE         = 2
DESSUS         = 4
HAUT_GAUCHE    = 5
HAUT_DROITE    = 6
DESSOUS        = 8
DESSOUS_GAUCHE = 9
DESSOUS_DROITE = 10

DEMS = 2 * FENETRE_LARGEUR // 8

boat_position = [60, 250]
boulet_position = [130, 330]
danger_position = [1100, 270]
pirate_position = [1100,250]
pointer_position = [375,269]

VITESSE_MINE = 5
VITESSE_NAGE = 5
VITESSE_OBJETS = 5
VITESSE_PIRATE = 5
VITESSE_PIRATE_V = 4
VITESSE_BOULET = 5
VITESSE_CADO = 5

score = 0
high_score = 0
up_meter = 0
meter = 10
vies = 3
change = 0
pointer = 1
vies_pirates = 1
adder = False
adder2 = False
adder3 = False
charger = 1000
power_count = 0

vies3_position = 95
vies2_position = 55
vies1_position = 15

bot_touch = False
top_touch = False
pir_dep = False
att_dep = False
vers_haut = False
vers_bas = False
tir_ami = False
on_boss = False
tir_ennemi = False
enjeu = False
BEP = False
golded = False
power1 = False
power2 = False
power3 = False

IMAGE_BOAT = pygame.image.load('images/ship2.png').convert_alpha(fenetre)
IMAGE_BOAT = pygame.transform.scale(IMAGE_BOAT, (BOAT_LARGEUR, BOAT_HAUTEUR))
IMAGE_NAGE = pygame.image.load('images/bottle.png').convert_alpha(fenetre)
IMAGE_NAGE = pygame.transform.scale(IMAGE_NAGE, (NAGE_COTE, NAGE_COTE))
IMAGE_MINE = pygame.image.load('images/shark.png').convert_alpha(fenetre)
IMAGE_MINE = pygame.transform.scale(IMAGE_MINE, (MINE_COTE, MINE_COTE))
IMAGE_LIFE = pygame.image.load('images/heart.png').convert_alpha(fenetre)
IMAGE_LIFE = pygame.transform.scale(IMAGE_LIFE, (LIFE_COTE, LIFE_COTE))
IMAGE_BLIFE = pygame.image.load('images/bonuslife.png').convert_alpha(fenetre)
IMAGE_BLIFE = pygame.transform.scale(IMAGE_BLIFE, (LIFE_COTE, LIFE_COTE))
IMAGE_PIRATE = pygame.image.load('images/pirate2.png').convert_alpha(fenetre)
IMAGE_PIRATE = pygame.transform.scale(IMAGE_PIRATE, (BOAT_LARGEUR, BOAT_HAUTEUR))
IMAGE_BALLE = pygame.image.load('images/balle.png').convert_alpha(fenetre)
IMAGE_BALLE = pygame.transform.scale(IMAGE_BALLE, (BALLE_COTE, BALLE_COTE))
IMAGE_FOND = pygame.image.load('images/fond.png').convert_alpha(fenetre)
IMAGE_FOND = pygame.transform.scale(IMAGE_FOND, (FENETRE_LARGEUR, FENETRE_HAUTEUR))
IMAGE_FOND1 = pygame.image.load('images/fond1.png').convert_alpha(fenetre)
IMAGE_FOND1 = pygame.transform.scale(IMAGE_FOND1, (FENETRE_LARGEUR, FENETRE_HAUTEUR))
IMAGE_FOND2 = pygame.image.load('images/fond2.png').convert_alpha(fenetre)
IMAGE_FOND2 = pygame.transform.scale(IMAGE_FOND2, (FENETRE_LARGEUR, FENETRE_HAUTEUR))
IMAGE_MAP = pygame.image.load('images/map.png').convert_alpha(fenetre)
IMAGE_MAP = pygame.transform.scale(IMAGE_MAP, (40, 40))
IMAGE_FAST = pygame.image.load('images/bonusfast.png').convert_alpha(fenetre)
IMAGE_FAST = pygame.transform.scale(IMAGE_FAST, (LIFE_COTE, LIFE_COTE))
IMAGE_INGOTS = pygame.image.load('images/ingots.png').convert_alpha(fenetre)
IMAGE_INGOTS = pygame.transform.scale(IMAGE_INGOTS, (LIFE_COTE, LIFE_COTE))
IMAGE_CADO = pygame.image.load('images/cadeau.png').convert_alpha(fenetre)
IMAGE_CADO = pygame.transform.scale(IMAGE_CADO, (MINE_COTE, MINE_COTE))
IMAGE_EXPLO = pygame.image.load('images/explosion.png').convert_alpha(fenetre)
IMAGE_EXPLO = pygame.transform.scale(IMAGE_EXPLO, (200, 200))
IMAGE_ARROWU = pygame.image.load('images/up.png').convert_alpha(fenetre)
IMAGE_ARROWU = pygame.transform.scale(IMAGE_ARROWU, (EMOTE_COTE, EMOTE_COTE))
IMAGE_ARROWD = pygame.image.load('images/down.png').convert_alpha(fenetre)
IMAGE_ARROWD = pygame.transform.scale(IMAGE_ARROWD, (EMOTE_COTE, EMOTE_COTE+5))
IMAGE_ENTER = pygame.image.load('images/return.png').convert_alpha(fenetre)
IMAGE_ENTER = pygame.transform.scale(IMAGE_ENTER, (EMOTE_COTE, EMOTE_COTE))
IMAGE_SPACE = pygame.image.load('images/space.png').convert_alpha(fenetre)
IMAGE_SPACE = pygame.transform.scale(IMAGE_SPACE, (EMOTE_COTE, EMOTE_COTE))




NAGE_X = random.randint(FENETRE_LARGEUR, FENETRE_LARGEUR*2)
NAGE_Y = random.randint(40, FENETRE_HAUTEUR-40)

MINE_X = random.randint(FENETRE_LARGEUR, FENETRE_LARGEUR*2)
MINE_Y = random.randint(40, FENETRE_HAUTEUR-40)

CADO_X = 10000
CADO_Y = random.randint(40, FENETRE_HAUTEUR-40)

cado_position = [CADO_X,CADO_Y]
nage_position = [NAGE_X,NAGE_Y]
mine_position = [MINE_X, MINE_Y]
moving_rect = pygame.Rect(boat_position[H],boat_position[V],BOAT_LARGEUR,BOAT_HAUTEUR)
boulet_rect = pygame.Rect(boulet_position[H],boulet_position[V],20,20)
danger_rect = pygame.Rect(danger_position[H],danger_position[V],20,20)


# /!\ IMPORTANT : fonction de contrôle du jeu -----------------------------------------

def traite_entrees():
    global fini, top_touch, bot_touch, tir_ami, enjeu
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            enjeu = False
            Restart()
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == TOUCHE_HAUT:
                if top_touch == False:
                    moove_boat(EN_HAUT)
                    bot_touch = False
            elif evenement.key == TOUCHE_BAS:
                if bot_touch == False:
                    moove_boat(EN_BAS)
                    top_touch = False
            elif evenement.key == TOUCHE_A:
                boss_event()
            elif evenement.key == TOUCHE_ESPACE:
                if att_dep == True:
                    tir_ami = True

# Fonction de test pratique -----------------------------------------

def test():
    print("Ca fonctionne !")

# Fonction qui gère les tires de notre bateau -----------------------------------------

def tir_boat():
    global tir_ami
    if tir_ami == True:
        boulet_rect.x += VITESSE_BOULET
        boulet_position[H] += VITESSE_BOULET
    if boulet_rect.x >= FENETRE_LARGEUR:
        reint_boulet()
    if tir_ami == False:
        boulet_rect.y = boulet_position[V] = boat_position[V] + 85

# Fonction qui réinitialise la postion de notre boulet -----------------------------------------

def reint_boulet():
    global tir_ami
    boulet_rect.y = moving_rect.y + 85
    boulet_position[V] = boat_position[V] + 85
    boulet_rect.x = 130
    boulet_position[H] = 130
    tir_ami = False

# Fonction de collision entre le boss et notre boulet -----------------------------------------

def touche():
    if boulet_rect.colliderect(pirate_rect):
        global tir_ami, vies_pirates, IMAGE_PIRATE
        boulet_rect.y = moving_rect.y + 85
        boulet_position[V] = boat_position[V] + 85
        boulet_rect.x = 130
        boulet_position[H] = 130
        tir_ami = False
        vies_pirates -= 1
        boule.play()
        if vies_pirates == 2:
            IMAGE_PIRATE = pygame.image.load('images/pirateB1.png').convert_alpha(fenetre)
            IMAGE_PIRATE = pygame.transform.scale(IMAGE_PIRATE, (BOAT_LARGEUR, BOAT_HAUTEUR))
        elif vies_pirates == 1:
            IMAGE_PIRATE = pygame.image.load('images/piarteB2.png').convert_alpha(fenetre)
            IMAGE_PIRATE = pygame.transform.scale(IMAGE_PIRATE, (BOAT_LARGEUR, BOAT_HAUTEUR))
        elif vies_pirates ==0:
            fenetre.blit(IMAGE_EXPLO, (pirate_position[H], pirate_position[V]))

# Fonction de collision entre notre bateau et le boulet du boss  -----------------------------------------

def touche_ennemie():
    global vies, enjeu
    if danger_rect.colliderect(moving_rect):
        danger_position[V] = danger_rect.y = pirate_rect.y + 85
        danger_position[H] = danger_rect.x = pirate_rect.x
        vies -= 1
        boule.play()
        if vies == 0:
            enjeu = False
            Restart()

# Fonction effectuée lorsque le boss est mort -----------------------------------------

def mort_pirate():
    global att_dep, pirate_position, vies_pirates, tir_ennemi,VITESSE_PIRATE_V,VITESSE_MINE,VITESSE_NAGE,VITESSE_CADO,danger_rect,danger_position,IMAGE_PIRATE,meter
    if vies_pirates == 0:
        att_dep = False
        pirate_position = [1100,250]
        pirate_rect.y = 250
        pirate_rect.x = 1100
        danger_position[H] = danger_rect.x = 1100
        VITESSE_MINE = VITESSE_NAGE = VITESSE_CADO = VITESSE_OBJETS
        tir_ennemi = False
        IMAGE_PIRATE = pygame.image.load('images/pirate2.png').convert_alpha(fenetre)
        IMAGE_PIRATE = pygame.transform.scale(IMAGE_PIRATE, (BOAT_LARGEUR, BOAT_HAUTEUR))

# Fonction effectuée lors d'un Restart (Cf. fonction au dessus) -----------------------------------------

def forcer_mort_pirate():
    global att_dep, pirate_position, vies_pirates, tir_ennemi, VITESSE_PIRATE_V,VITESSE_MINE,VITESSE_NAGE,VITESSE_CADO,danger_rect,IMAGE_PIRATE,meter
    if 1 > 0:
        att_dep = False
        pirate_position = [1100,250]
        pirate_rect.y = 250
        pirate_rect.x = 1100
        danger_position[H] = danger_rect.x = 1100
        VITESSE_MINE = 5
        VITESSE_NAGE = 5
        VITESSE_CADO = 5
        tir_ennemi = False
        IMAGE_PIRATE = pygame.image.load('images/pirate2.png').convert_alpha(fenetre)
        IMAGE_PIRATE = pygame.transform.scale(IMAGE_PIRATE, (BOAT_LARGEUR, BOAT_HAUTEUR))

# Fonction d'automatisation de l'appariton du boss -----------------------------------------

def app_boss():
    global meter, score, att_dep, pir_dep
    if meter % 20 == 0 and score >= 1:
        if att_dep == False and pir_dep == False:
            boss_event()

# Foncion initialisée au démarage du jeu -----------------------------------------

def dessine_court():
    global up_meter, meter, vies, VITESSE_MINE, VITESSE_NAGE, DEMS,IMAGE_BOAT,VITESSE_CADO,VITESSE_OBJETS
    fenetre.fill(BLEU)
    pygame.draw.rect(fenetre,BLEU,top_rect)
    if att_dep == False:
        up_meter += 1
        if up_meter % 300 == 0 and meter < 99:
            meter += 1
        if up_meter % 1500 == 0:
            VITESSE_MINE += 1
            VITESSE_NAGE += 1
            VITESSE_CADO += 1
            VITESSE_OBJETS += 1

people_rect = pygame.Rect(NAGE_X,NAGE_Y,NAGE_COTE,NAGE_COTE)
mine_rect = pygame.Rect(MINE_X,MINE_Y,MINE_COTE,MINE_COTE)
cado_rect = pygame.Rect(CADO_X,CADO_Y,MINE_COTE,MINE_COTE)
top_rect = pygame.Rect(0,0,FENETRE_LARGEUR,7*MUR_EPAISSEUR + 2)
bottom_rect = pygame.Rect(0,FENETRE_HAUTEUR,FENETRE_LARGEUR,MUR_EPAISSEUR)
pirate_rect = pygame.Rect(pirate_position[H],pirate_position[V],BOAT_LARGEUR,BOAT_HAUTEUR)

# Fonction qui gère les déplacements de notre bateau -----------------------------------------

def moove_boat(sens):
    moving_rect.y += BOAT_DEPLACEMENT * sens
    boat_position[V] += BOAT_DEPLACEMENT * sens


# Fonction qui gère les déplacements de haut en bas du boss ◊(2) -----------------------------------------

def move_attack_pirate():
    global vers_haut, vers_bas, vies_pirates
    VITESSE_PIRATE_V = 4
    if vers_haut == True and vies_pirates > 0:
        pirate_position[V] -= VITESSE_PIRATE_V
        pirate_rect.y -= VITESSE_PIRATE_V
    if vers_bas == True and vies_pirates > 0:
        pirate_position[V] += VITESSE_PIRATE_V
        pirate_rect.y += VITESSE_PIRATE_V

# Fonction qui gère l'apparition du boss -----------------------------------------

def move_pirate():
    global pir_dep,att_dep,tir_ennemi,danger_position
    if pir_dep == True:
        pirate_rect.x -= VITESSE_PIRATE
        pirate_position[H] -= VITESSE_PIRATE
        pirate_position[V] = pirate_rect.y = 250
        danger_position[H] = danger_rect.x = pirate_rect.x + 70
        danger_position[V] = danger_rect.y = pirate_rect.y + 75
    if pirate_position[H] == 700:
        pir_dep = False
        att_dep = True
        tir_ennemi = True

# Fonction qui gère les déplacements de haut en bas du boss ◊(1) -----------------------------------------

def attack_pirate():
    global att_dep, vers_haut, vers_bas, change, danger_position
    if att_dep == True and vies_pirates > 0:
        rand = random.randint(1, 20)
        if rand == 3 and change == 0:
            vers_haut = True
            vers_bas = False
            change = 30
        elif rand == 5 and change == 0:
            vers_bas = True
            vers_haut = False
            change = 30
        elif pirate_position[V] <= 7*MUR_EPAISSEUR:
            vers_haut = False
            vers_bas = True
            change = 20
        elif pirate_position[V] >= FENETRE_HAUTEUR - MUR_EPAISSEUR - BOAT_HAUTEUR:
            vers_bas = False
            vers_haut = True
            change = 20
        if change > 0:
            change -= 1
        if tir_ennemi == False:
            danger_rect.y = pirate_rect.y + 85
            danger_rect.x = pirate_rect.x
            danger_position[V] = pirate_rect.y + 85
            danger_position[H] = pirate_rect.x

# Fonction qui gère les tires du boss -----------------------------------------

def tir_pirate():
    global tir_ennemi, boulet_position, danger_rect
    if tir_ennemi == True:
        danger_rect.x -= VITESSE_BOULET
        danger_position[H] -= VITESSE_BOULET
    if danger_rect.x <= 0:
        danger_position[V] = danger_rect.y = pirate_rect.y + 85
        danger_position[H] = danger_rect.x = pirate_rect.x

# /!\ IMPORTANT : fonction effectuée lorsque le jeu est fini -----------------------------------------

def Restart():
    global meter,up_meter,score,vies,vies1_position,vies2_position,vies3_position,BEP,adder,adder2,pir_dep,charger,power1,power2,power3,power_count,VITESSE_CADO,VITESSE_MINE,VITESSE_OBJETS,VITESSE_NAGE,BALLE_COTE,IMAGE_NAGE,DEMS,BOAT_DEPLACEMENT
    vies = 3
    up_meter = 0
    meter = 10
    score = 0
    people_rect.x = nage_position[H] = random.randint(FENETRE_LARGEUR, FENETRE_LARGEUR*2)
    mine_rect.x = mine_position[H] = random.randint(FENETRE_LARGEUR, FENETRE_LARGEUR*2)
    IMAGE_NAGE = pygame.image.load('images/bottle.png').convert_alpha(fenetre)
    IMAGE_NAGE = pygame.transform.scale(IMAGE_NAGE, (NAGE_COTE, NAGE_COTE))
    cado_rect.x = cado_position[H] = 10000
    vies3_position = 95
    vies2_position = 55
    vies1_position = 15
    VITESSE_CADO = 5
    VITESSE_MINE = 5
    VITESSE_NAGE = 5
    VITESSE_OBJETS = 5
    moving_rect.y = boat_position[V] = 250
    BEP = False
    adder2 = False
    adder = False
    pir_dep = False
    charger = 500
    power1 = False
    power2 = False
    power3 = False
    power_count = 0
    DEMS = 2 * FENETRE_LARGEUR // 8
    BOAT_DEPLACEMENT = 10
    forcer_mort_pirate()
    reint_boulet()
    pygame.mixer.music.play()

# Fonction qui gère la pluspart des collisions -----------------------------------------

def bouncing_rect():
    global score, vies, game, top_touch, bot_touch, enjeu,power_count,power3
    people_rect.x -= VITESSE_NAGE
    nage_position[H] -= VITESSE_NAGE
    mine_rect.x -=  VITESSE_MINE
    mine_position[H] -= VITESSE_MINE
    cado_rect.x -=  VITESSE_CADO
    cado_position[H] -= VITESSE_CADO

    if people_rect.x <= -100:
        people_rect.y = nage_position[V] = random.randint(100, FENETRE_HAUTEUR-100)
        people_rect.x = nage_position[H] = random.randint(FENETRE_LARGEUR, FENETRE_LARGEUR*2)

    if moving_rect.colliderect(people_rect):
        people_rect.y = nage_position[V] = random.randint(100, FENETRE_HAUTEUR-100)
        people_rect.x = nage_position[H] = random.randint(FENETRE_LARGEUR, FENETRE_LARGEUR*2)
        score += 1
        bouteille.play()
        if power3 == True:
            score += 1

    if mine_rect.x <= -100:
        mine_rect.y = mine_position[V] = random.randint(100, FENETRE_HAUTEUR-100)
        mine_rect.x = mine_position[H] = random.randint(FENETRE_LARGEUR, FENETRE_LARGEUR*2)

    if moving_rect.colliderect(mine_rect):
        mine_rect.y = mine_position[V] = random.randint(100, FENETRE_HAUTEUR-100)
        mine_rect.x = mine_position[H] = random.randint(FENETRE_LARGEUR, FENETRE_LARGEUR*2)
        vies -= 1
        shark.play()
        if vies == 0:
            enjeu = False
            Restart()

    if cado_rect.x <= -100:
        cado_rect.y = cado_position[V] = random.randint(100, FENETRE_HAUTEUR-100)
        cado_rect.x = cado_position[H] = 5000

    if moving_rect.colliderect(cado_rect):
        cado_rect.y = cado_position[V] = random.randint(100, FENETRE_HAUTEUR-100)
        cado_rect.x = cado_position[H] = 10000
        power_count += 1
        cado.play()


    if moving_rect.colliderect(top_rect):
        top_touch = True
        moving_rect.y += MUR_EPAISSEUR
        boat_position[V] += MUR_EPAISSEUR
    if moving_rect.colliderect(bottom_rect):
        bot_touch = True
        moving_rect.y -= MUR_EPAISSEUR
        boat_position[V] -= MUR_EPAISSEUR

# Fonction qui dessine quasiment tous les objets -----------------------------------------

def dessiner_objets():
    global DEMS,power1,power2,power3
    pygame.draw.rect(fenetre,BLEU,moving_rect)
    pygame.draw.rect(fenetre,BLEU,people_rect)
    pygame.draw.rect(fenetre,BLEU,mine_rect)
    pygame.draw.rect(fenetre,BRUNF,bottom_rect)
    pygame.draw.rect(fenetre,BLEU,danger_rect)
    pygame.draw.rect(fenetre,BLEU,pirate_rect)
    pygame.draw.rect(fenetre,BLEU,boulet_rect)
    #fenetre.blit(IMAGE_FOND2, (-30, 0))
    fenetre.blit(IMAGE_BALLE, (boulet_position[H], boulet_position[V]))
    fenetre.blit(IMAGE_BALLE, (danger_position[H], danger_position[V]))
    fenetre.blit(IMAGE_MINE, (mine_position[H], mine_position[V]))
    fenetre.blit(IMAGE_BOAT, (boat_position[H], boat_position[V]))
    fenetre.blit(IMAGE_NAGE, (nage_position[H], nage_position[V]))
    fenetre.blit(IMAGE_CADO, (cado_position[H], cado_position[V]))
    fenetre.blit(IMAGE_PIRATE, (pirate_position[H], pirate_position[V]))
    fenetre.blit(IMAGE_FOND, (0, 0))
    fenetre.blit(IMAGE_LIFE, (vies3_position, 15))
    fenetre.blit(IMAGE_LIFE, (vies2_position, 15))
    fenetre.blit(IMAGE_LIFE, (vies1_position, 15))
    if power1 == True:
        fenetre.blit(IMAGE_BLIFE, (645, 12))
    if power2 == True:
        fenetre.blit(IMAGE_FAST, (712, 12))
    if power3 == True:
        fenetre.blit(IMAGE_INGOTS, (775, 12))
    fenetre.blit(IMAGE_MAP, (315, 5))
    marquoir2 = police3.render(str(meter), True, NOIR)
    fenetre.blit(marquoir2, (FENETRE_LARGEUR // 2 - 35 , 5))
    marquoir = police.render(str(score), True, EMERAULD)
    fenetre.blit(marquoir, (DEMS, 0))
    if score == 10:
        DEMS = 2 * FENETRE_LARGEUR // 8 - 35
    marquoirX = police2.render(str("x"), True, EMERAULD)
    fenetre.blit(marquoirX, (2 * FENETRE_LARGEUR // 7, 7))
    #fenetre.blit(IMAGE_INDIC, (FENETRE_LARGEUR // 2 - 30, 10))

# Fonction qui engendre la série d'événements liés au boss -----------------------------------------

def boss_event():
    global BEP,meter
    BEP = True
    meter += 1

def boss_event_plus():
    global VITESSE_MINE,VITESSE_NAGE,VITESSE_CADO,pirate_position,pir_dep, vies_pirates,BEP,adder,adder2,adder3
    if BEP == True:
        if mine_position[H] >= FENETRE_LARGEUR:
            adder = True
            VITESSE_MINE = 0
        if nage_position[H] >= FENETRE_LARGEUR:
            adder2 = True
            VITESSE_NAGE = 0
        if cado_position[H] >= FENETRE_LARGEUR:
            adder3 = True
            VITESSE_CADO = 0
        if adder == True and adder2 == True and adder3 == True:
            BEP = False
            adder2 = False
            adder = False
            pir_dep = True
            vies_pirates = 3

# Fonction qui gère le visuel des vies -----------------------------------------

def manage_life():
    global vies, vies1_position, vies2_position, vies3_position
    if vies < 3:
        vies3_position = -100
    if vies < 2:
        vies2_position = -100
    if vies < 1:
        vies1_position = -100

# Fonction de musique

if enjeu == False:
    pygame.mixer.music.play()


# Fonction qui permet de gérer le H.S. -----------------------------------------

def best_score():
    global score, high_score
    if score > high_score:
        high_score = score
    if high_score < 10:
        marquoirHS = police.render(str(high_score), True, JAUNE)
        fenetre.blit(marquoirHS, (FENETRE_LARGEUR - 130, 4))
    if high_score >= 10:
        marquoirHS = police.render(str(high_score), True, JAUNE)
        fenetre.blit(marquoirHS, (FENETRE_LARGEUR - 153, 4))

# Fonction qui gère le power up life -----------------------------------------

def powerup_life():
    global charger, vies, power1, charger,vies2_position, vies3_position
    if power1 == True:
        if charger == 0 and vies < 3:
            test()
            charger = 500
            if vies == 2:
                vies3_position = 95
                vies += 1
            elif vies == 1:
                vies3_position = 95
                vies2_position = 55
                vies += 1
        if charger > 0 and vies < 3:
            charger -= 1

# Fonction qui gère le power up faster -----------------------------------------

def powerup_faster():
    global power2, BOAT_DEPLACEMENT
    if power2 == True:
        BOAT_DEPLACEMENT = 20

# Fonction qui gère le power up baller -----------------------------------------

def powerup_baller():
    global power1
    if power1 == True:
        BALLE_COTE = 30


# Fonction qui gère le power up golder -----------------------------------------

def powerup_golder():
    global power3, IMAGE_NAGE,score
    if power3 == True:
        IMAGE_NAGE = pygame.image.load('images/golded.png').convert_alpha(fenetre)
        IMAGE_NAGE = pygame.transform.scale(IMAGE_NAGE, (NAGE_COTE, NAGE_COTE))


# Fonction qui gère les powerup -----------------------------------------

def manage_up():
    global power_count,power1,power2,power3,VITESSE_CADO
    if power_count == 1:
        power1 = True
    if power_count == 2:
        power2 = True
    if power_count == 3:
        power3 = True
        VITESSE_CADO = 0



# Fonction qui permet d'afficher le menu -----------------------------------------

def dessine_menu():
    global pointer
    if enjeu == False:
        fenetre.fill(BLEU)
        if pointer == 1:
            fenetre.blit(IMAGE_FOND1, (0, 0))
        if pointer == 2:
            fenetre.blit(IMAGE_FOND2, (0, 0))
        marquoir = police1.render(str("JOUER"), True, MARK1)
        fenetre.blit(marquoir, (FENETRE_LARGEUR//2-40, FENETRE_HAUTEUR//2-FENETRE_HAUTEUR//7-10))
        marquoir2 = police1.render(str("QUITTER"), True, MARK2)
        fenetre.blit(marquoir2, (FENETRE_LARGEUR//2-60, FENETRE_HAUTEUR//2+15))
        pygame.draw.circle(fenetre, EMERAULD, pointer_position, 0)
        fenetre.blit(IMAGE_ARROWD, (705, 496))
        fenetre.blit(IMAGE_ARROWU, (771, 500))
        fenetre.blit(IMAGE_SPACE, (835, 500))
        fenetre.blit(IMAGE_ENTER, (900, 500))



# Fonction qui permet d'intéragir avec le menu -----------------------------------------

def traite_entrees_menu():
    global fini, pointer, enjeu,MARK1,MARK2
    if enjeu == False:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                fini = True
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == TOUCHE_HAUT:
                    if pointer_position[V] >= 270:
                        pointer_position[V] -= 60
                        pointer = 1
                        MARK1 = EMERAULD
                        MARK2 = NOIR
                elif evenement.key == TOUCHE_BAS:
                    if pointer_position[V] <= 300:
                        pointer_position[V] += 60
                        pointer = 2
                        MARK1 = NOIR
                        MARK2 = EMERAULD
                elif evenement.key == ENTER:
                    if pointer == 1:
                        enjeu = True
                        pygame.mixer.music.stop()
                    elif pointer == 2:
                        fini = True

# /!\ IMPORTANT : Initialisation et autres -----------------------------------------


pygame.init()
pygame.key.set_repeat(200, 25)

pygame.display.set_caption("Boat");

fenetre.fill(BLEU)

police = pygame.font.SysFont('courier', FENETRE_HAUTEUR//12, True)
police1 = pygame.font.SysFont('courier', FENETRE_HAUTEUR//14, True)
police2 = pygame.font.SysFont('arial', FENETRE_HAUTEUR//20, True)
police3 = pygame.font.SysFont('arial', FENETRE_HAUTEUR//9, True)

fini = False
game = False
temps = pygame.time.Clock()

while not fini:

    dessine_menu()

    traite_entrees_menu()

    pygame.display.flip()
    temps.tick(50)

    while enjeu == True:

        traite_entrees()

        dessine_court()

        bouncing_rect()

        manage_life()

        move_pirate()

        attack_pirate()

        move_attack_pirate()

        tir_boat()

        touche()

        mort_pirate()

        app_boss()

        tir_pirate()

        dessiner_objets()

        touche_ennemie()

        boss_event_plus()

        best_score()

        powerup_life()

        powerup_faster()

        manage_up()

        powerup_baller()

        powerup_golder()

        pygame.display.flip()
        temps.tick(50)

pygame.display.quit()
pygame.quit()
