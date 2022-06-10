import g2d
import time
import datetime
from random import randint
from navicella import Navicella
from proiettile import Proiettile
from buca import Buca
from roccia import Roccia
from rover import Rover
from sfondo import Sfondo


def update() :
    esito = 0
    esitoTotali = [6]
    esitoTotali = ['0','0','0','0','0','0']
    esitoFinale = 0
    xM, yM = roverGioco.posizione()
    xB, yB = buca1.posizione()
    xB1, yB1 = buca2.posizione()
    xR,yR = roccia1.posizione()
    xR1, yR1 = roccia2.posizione()
    xP, yP = proiettileRover1.posizione()
    xP1, yP1 = proiettileRover2.posizione()
    xP2, yP2 = proiettileNavicella1.posizione()
    xP3, yP3 = proiettileNavicella2.posizione()

    #---------------- collide -----------------------------
    # for i in range(30):
    #  if (xM == xP2 + i or xM == xP2 - i) or (xM == xP3 + i or xM == xP3 - i) :
    #          if (yM == yP2 + i or yM == yP2 - i) or (yM == yP3 + i or yM == yP3 - i) :
    #              esito = 1
    #
    #  for i in range(30):
    #      if (xM == xP3 + i or xM == xP3 - i):
    #          if (yM == yP3 + i or yM == yP3 - i):
    #              esito = 1
    #
    # for i in range(200) :
    #      if (xM == xB + i or xM == xB - i) or (xM == xB1 + i or xM == xB1 - i) :
    #          if (yM == yB + i or yM == yB - i) or (yM == yB1 + i or yM == yB1 - i) :
    #              esito = 1
    #
    # for i in range(70) :
    #     if (xM == xR + i or xM == xR - i) or (xM == xR1 + i or xM == xR1 - i) :
    #        if (yM == yR + i or yM == yR - i) or (yM == yR1 + i or yM == yR1 - i) :
    #           esito = 1

    esitoTotali[0] = roverGioco.collide(xP2, yP2,30)
    esitoTotali[1] = roverGioco.collide(xP3, yP3, 30)
    esitoTotali[2] = roverGioco.collide(xB, yB, 90)
    esitoTotali[3] = roverGioco.collide(xB1, yB1, 90)
    esitoTotali[4] = roverGioco.collide(xR, yR, 85)
    esitoTotali[5] = roverGioco.collide(xR1, yR1, 85)

    for i in esitoTotali :
        if i == 1 :
            esitoFinale = 1

    # -----------------------------------------------------------

    if esitoFinale == 0 :
        g2d.clear_canvas()

        #-------------------- Gestione punteggio ----------------
        punteggio = roverGioco.punteggio() + 0.5
        roverGioco.setPunteggio(punteggio)

        #--------------------- Gestione salto -----------------------
        jump = roverGioco.getJump()

        if jump == 1:
            roverGioco.setPosizione(xM, yM - 5)

        if jump == -1:
            roverGioco.setPosizione(xM, yM + 5)

        if yM <= 320:
            roverGioco.go_down()

        if yM == 440 and jump == -1:
            roverGioco.setJump(0)

        # ---------------------- Comandi tastiera --------------------------
        if g2d.key_pressed("ArrowRight"):
            proiettileRover1.setPosizione(40, 445)
            proiettileRover2.setPosizione(40, 445)

        if g2d.key_pressed("ArrowUp"):
            roverGioco.go_up()

        # ------------ movimento sfondo ----------------
        sfondoGioco.move()
        sfondoGioco.go_left()

        # ------------ movimento proiettili del rover  ----------------
        proiettileRover1.move(1)
        proiettileRover2.move(2)

        # ------------ movimento buche ----------------
        buca1.move()
        buca2.move()

        # ------------ movimento rocce --------------
        roccia1.move(xP, yP)
        roccia2.move(xP,yP)

        # ------------ movimento navicelle e dei loro proiettili ---------------
        navicella1.move(xP1, yP1)
        navicella2.move(xP1, yP1)

        xN1, yN1 = navicella1.posizione()
        xN2, yN2 = navicella2.posizione()

        if yN1 > 700 :
            proiettileNavicella1.setPosizione(800, 800)
        if yN2 > 700 :
            proiettileNavicella2.setPosizione(800, 800)

        proiettileNavicella1.move(3)
        proiettileNavicella2.move(3)

        for i in range(30) :
             if yP2 == 445 + i :
                 buca1.setPosizione(xP2, 470)
                 proiettileNavicella1.setPosizione(xN1,yN1)
             if yP3 == 445 + i :
                 buca2.setPosizione(xP3, 470)
                 proiettileNavicella2.setPosizione(xN2, yN2)

        # -------------------- disegno tutti i personaggi -------------
        g2d.draw_image(sfondo, (sfondoGioco.posizione()))
        g2d.draw_image(buca, (buca1.posizione()))
        g2d.draw_image(buca, (buca2.posizione()))
        g2d.draw_image(proiettile, (proiettileRover2.posizione()))
        g2d.draw_image(proiettile, (proiettileRover1.posizione()))
        g2d.draw_image(macchina, (roverGioco.posizione()))
        g2d.draw_image(navicella, (navicella1.posizione()))
        g2d.draw_image(navicella, (navicella2.posizione()))
        g2d.draw_image(proiettile, (proiettileNavicella1.posizione()))
        g2d.draw_image(proiettile, (proiettileNavicella2.posizione()))
        g2d.draw_image(roccia, (roccia1.posizione()))
        g2d.draw_image(roccia, (roccia2.posizione()))
        g2d.play_audio(audioGioco)
        g2d.draw_text("Punteggio : " + str(roverGioco.punteggio()),(450,2),30)


    else :
        gameOver = g2d.load_image("Immagini/gameOver1.png")
        g2d.draw_image(gameOver, (0,0))
        g2d.pause_audio(audioGioco)
        g2d.play_audio(audioGameOver)


ARENA_W = 700
ARENA_H = 500

posizioneX = randint(200,ARENA_W) # posizione casuale buca 1
posizione1X = randint(200,ARENA_W) # posizione casuale buca 2
posizione2X = randint(200,ARENA_W) # posizione casuale roccia 1
posizione3X = randint(200,ARENA_W) # posizione casuale roccia 2


sfondoGioco = Sfondo(2, 2) #sfondo
proiettileRover1 = Proiettile(40, 430)
proiettileRover2 = Proiettile(40, 430)
roverGioco = Rover(40, 440) #rover
buca1 = Buca(posizioneX, 540) #buca 1
buca2 = Buca(posizione1X, 540) #buca 2
roccia1 = Roccia(posizione2X, 430)#roccia 1
roccia2 = Roccia(posizione3X, 430)#roccia 2
navicella1 = Navicella(210, 70)#Navicella 1
navicella2 = Navicella(250, 65)#Navicella 2

xN,yN = navicella1.posizione()
xN1,yN1 = navicella2.posizione()
proiettileNavicella1 = Proiettile(xN, 70)
proiettileNavicella2 = Proiettile(xN1, 65)

audioGioco = g2d.load_audio("Audio/game.mp3")
audioGameOver = g2d.load_audio("Audio/gameover.wav")
sfondo = g2d.load_image("Immagini/sfondo3.jpg")
macchina = g2d.load_image("Immagini/macchina2.png")
buca = g2d.load_image("Immagini/buca1.jpg")
roccia = g2d.load_image("Immagini/roccia.jpg")
proiettile = g2d.load_image("Immagini/proiettile.jpg")
navicella = g2d.load_image("Immagini/navicella1.jpg")


def main():

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(update, 1000 // 30)
    #-------------------------- Scrittura file con punteggio ---------------------
    now = datetime.datetime.now()
    with open("punteggi.txt", "a") as myFile:
        myFile.write(
            "\nPunteggio : " + str(roverGioco.punteggio()) + " data e ora : " + now.strftime("%Y-%m-%d %H:%M:%S"))

main()
