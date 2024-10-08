import tkinter
from tkinter import *
from tkinter import ttk


#cores que vão ser usadas

co0= "#FFFFFF" #branca / white
co1= "#333333" #preta escura / dark black
co2= "#fcc058" #laranja
co3= "#38576b" #valor
co4= "#3297a8" #azul
co5= "#fff873" #amarelo
co6= "#e85151" #vermelho
co7= "green"   #verde
fundo= "#3b3b3b" #black

# criando janela principal

janela=Tk()
janela.title("")
janela.geometry("260x400")
janela.configure(bg=fundo)
janela.resizable(False, False)


# dividindo a janela em 2 frame

frame_cima= Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10,pady=10)

frame_baixo= Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# configurando frame de cima 

app_x= Label(frame_cima, text="X", height=1, relief="flat", anchor="center", font=("Ivy", 40, "bold"), bg=co1, fg=co6)
app_x.place(x=25, y=10)

app_x= Label(frame_cima, text="Playier 2", height=1, relief="flat", anchor="center", font=("Ivy", 7, "bold"), bg=co1, fg=co0)
app_x.place(x=21, y=70)

app_x_pontos1= Label(frame_cima, text="0", height=1, relief="flat", anchor="center", font=("Ivy", 40, "bold"), bg=co1, fg=co0)
app_x_pontos1.place(x=80, y=20)

app_separador= Label(frame_cima, text=":", height=1, relief="flat", anchor="center", font=("Ivy", 30, "bold"), bg=co1, fg=co0)
app_separador.place(x=110, y=20)

app_x= Label(frame_cima, text="O", height=1, relief="flat", anchor="center", font=("Ivy", 40, "bold"), bg=co1, fg=co4)
app_x.place(x=170, y=10)

app_x= Label(frame_cima, text="Player 2", height=1, relief="flat", anchor="center", font=("Ivy", 7, "bold"), bg=co1, fg=co0)
app_x.place(x=173, y=70)

app_x_pontos= Label(frame_cima, text="0", height=1, relief="flat", anchor="center", font=("Ivy", 40, "bold"), bg=co1, fg=co0)
app_x_pontos.place(x=130, y=20)


# Criando logica do app

jogador_1= "X"
jogador_2= "0"

score_1= 0
score_2= 0

tabela=[["1", "2", "3"], ["4","5","6"], ["7","8","9"]]

jogando= "X"
joga=""
contador=0
contador_de_rodada=0


def iniciar_jogo():
    b_jogar.destroy()
    def controlar(i):
        global jogando
        global contador
        global joga
        global cor
        
        #comparando valor recebido
        if i==str(1):
            
            
            #verificando se está vazio
            if b_0["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_0["fg"]=cor
                b_0["text"]=jogando
                tabela[0][0]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                 
        if i==str(2):
            
            
            #verificando se está vazio
            if b_1["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_1["fg"]=cor
                b_1["text"]=jogando
                tabela[0][1]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                
        if i==str(3):
            
            
            #verificando se está vazio
            if b_2["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_2["fg"]=cor
                b_2["text"]=jogando
                tabela[0][2]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                        
        if i==str(4):
            
            
            #verificando se está vazio
            if b_3["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_3["fg"]=cor
                b_3["text"]=jogando
                tabela[1][0]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                      
        if i==str(5):
            
            
            #verificando se está vazio
            if b_4["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_4["fg"]=cor
                b_4["text"]=jogando
                tabela[1][1]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                      
        if i==str(6):
            
            
            #verificando se está vazio
            if b_5["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_5["fg"]=cor
                b_5["text"]=jogando
                tabela[1][2]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                    
        if i==str(7):
            
            
            #verificando se está vazio
            if b_6["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_6["fg"]=cor
                b_6["text"]=jogando
                tabela[2][0]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                  
        if i==str(8):
            
            
            #verificando se está vazio
            if b_7["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_7["fg"]=cor
                b_7["text"]=jogando
                tabela[2][1]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                  
        if i==str(9):
            
            
            #verificando se está vazio
            if b_8["text"]=="":
                #verificando quem está jogando e definir a cor
                if jogando=="X":
                    cor=co6
                if jogando=="O":
                    cor=co4
                    
                #definindo a cor do text do botao
                #marca a posição da tabela com o valor do jogador
                
                b_8["fg"]=cor
                b_8["text"]=jogando
                tabela[2][2]=jogando
                
                #verificando quem esta a jogar, para trocar de jogador
                
                if jogando =="X":
                    jogando="O"
                    joga="Jogador 1"
                else:
                    jogando= "X"
                    joga="Jogador 2"
                    
                #incrementa0r o contador para a proxima rodada
                contador+=1
                       
        #se contador for maior 5, verifica se ouve algum vencedor        
        if contador>=5:
            # linhas
            if tabela[0][0]==tabela[0][1]==tabela[0][2]!='':
                        vencedor(jogando)
            elif tabela[1][0]==tabela[1][1]==tabela[1][2]!='':
                        vencedor(jogando)
            elif tabela[2][0]==tabela[2][1]==tabela[2][2]!='':
                        vencedor(jogando)
                        
            #colunas
            if tabela[0][0]==tabela[1][0]==tabela[2][0]!='':
                        vencedor(jogando)
            elif tabela[0][1]==tabela[1][1]==tabela[2][1]!='':
                        vencedor(jogando)
            elif tabela[0][2]==tabela[1][2]==tabela[2][2]!='':
                        vencedor(jogando)
                        
            #diagonais
            if tabela[0][0]==tabela[1][1]==tabela[2][2]!='':
                        vencedor(jogando)
            elif tabela[0][2]==tabela[1][1]==tabela[2][0]!='':
                        vencedor(jogando)
                        
            # empate
            if contador>=9:
                vencedor("foi empate")       
        
    def vencedor(i):
        global tabela
        global score_1
        global score_2
        global contador_de_rodada
        global contador

        
        
        #bloqueando botões
        b_0["state"]="disable"
        b_1["state"]="disable"
        b_2["state"]="disable"
        b_3["state"]="disable"
        b_4["state"]="disable"
        b_5["state"]="disable"
        b_6["state"]="disable"
        b_7["state"]="disable"
        b_8["state"]="disable"
        
        
        app_vencedor= Label(janela, text="", width=24, relief="flat", anchor="center", font=("Ivy 13 bold"), bg=co1, fg=co2)
        app_vencedor.place(x=10, y=360)
        
        
        
        

        if i == "X":
            score_2+=1
            app_vencedor["text"]= "player 2 won the match"
            app_x_pontos["text"]=score_2
                
        if i == "O":
            score_1+=1
            app_vencedor["text"]= "player 1 win the match"
            app_x_pontos1["text"]=score_1
            
        if i=="foi empate":
            app_vencedor["text"]="tied"
            
        
        
        
        def start():
            
            #Limpando os botões
            b_0["text"]=""
            b_1["text"]=""
            b_2["text"]=""
            b_3["text"]=""
            b_4["text"]=""
            b_5["text"]=""
            b_6["text"]=""
            b_7["text"]=""
            b_8["text"]=""
        
            
            b_0["state"]="normal"
            b_1["state"]="normal"
            b_2["state"]="normal"
            b_3["state"]="normal"
            b_4["state"]="normal"
            b_5["state"]="normal"
            b_6["state"]="normal"
            b_7["state"]="normal"
            b_8["state"]="normal"
            
            
            
            app_vencedor.destroy()
            b_proxima.destroy()
            
            # botão jogar
        b_proxima= Button(frame_baixo,command=start, text="Next round",height=1, font=("Ivy", 10, "bold"), overrelief=RIDGE,relief="raised", bg=fundo, fg=co0)
        b_proxima.place(x=84,y=197)
        
        def jogo_acabou():
            b_proxima.destroy()
            app_vencedor.destroy()
            
            termina()
            
        if  score_2 ==3 or score_1==3:
            jogo_acabou()
        else:
            contador_de_rodada+=1
            
            # reiniciando a tabela
            tabela=[["1", "2", "3"], ["4","5","6"], ["7","8","9"]]
            contador = 0    
            
            
                      
    def termina():
        global tabela
        global contador_de_rodada
        global score_1
        global score_2
        global contador
        global jogando
        
        tabela=[["1", "2", "3"], ["4","5","6"], ["7","8","9"]]
        contador_de_rodada=0
        score_1=0
        score_2=0

        
        #bloqueando botões
        b_0["state"]="disable"
        b_1["state"]="disable"
        b_2["state"]="disable"
        b_3["state"]="disable"
        b_4["state"]="disable"
        b_5["state"]="disable"
        b_6["state"]="disable"
        b_7["state"]="disable"
        b_8["state"]="disable"
        
        
        if jogando=="X":
            app_fim= Label(janela, text="Player 2 win", width=17, relief="flat", anchor="center", font=("Ivy 13 bold"), bg=co1, fg=co2)
            app_fim.place(x=40, y=360)
        elif jogando=="O":
            app_fim= Label(janela, text="Player 1 win", width=17, relief="flat", anchor="center", font=("Ivy 13 bold"), bg=co1, fg=co2)
            app_fim.place(x=40, y=360)
        
        
        # jogar de novo 
        
        def jogar_denovo():
            global contador
            app_x_pontos["text"]="0"
            app_x_pontos1["text"]="0"
            app_fim.destroy()
            joga_dnv.destroy()
            contador=0
        
            #chamando a função iniciar jogo
            iniciar_jogo()
         
        # botão proxima

        joga_dnv= Button(frame_baixo,command=jogar_denovo, text="Play again", width=10,height=1, font=("Ivy", 10, "bold"), overrelief=RIDGE,relief="raised", bg=fundo, fg=co0)
        joga_dnv.place(x=85,y=197)
    
    # botões
    #linha 1
    b_0= Button(frame_baixo,command=lambda:controlar("1"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_0.place(x=30,y=15)

    b_1= Button(frame_baixo,command=lambda:controlar("2"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_1.place(x=96,y=15)

    b_2= Button(frame_baixo,command=lambda:controlar("3"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_2.place(x=163,y=15)

    #linha 2
    b_3= Button(frame_baixo,command=lambda:controlar("4"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_3.place(x=30,y=75)

    b_4= Button(frame_baixo,command=lambda:controlar("5"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_4.place(x=96,y=75)

    b_5= Button(frame_baixo,command=lambda:controlar("6"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_5.place(x=163,y=75)

    #linha 3
    b_6= Button(frame_baixo,command=lambda:controlar("7"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_6.place(x=30,y=135)

    b_7= Button(frame_baixo,command=lambda:controlar("8"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_7.place(x=96,y=135)

    b_8= Button(frame_baixo,command=lambda:controlar("9"), text="", width=3,height=1, font=("Ivy",20, "bold"), overrelief=RIDGE,relief="flat", bg=fundo, fg=co6)
    b_8.place(x=163,y=135)
    
    # configurando framde de baixo

    #linhas verticais
    app_= Label(frame_baixo, text="", height=23, relief="flat",pady=5, anchor="center", font=("Ivy", 5, "bold"), bg=co0, fg=co0)
    app_.place(x=90, y=15)

    app_= Label(frame_baixo, text="", height=23, relief="flat",pady=5, anchor="center", font=("Ivy", 5, "bold"), bg=co0, fg=co0)
    app_.place(x=157, y=15)

    #linhas horizontais
    app_= Label(frame_baixo, text="  ", width=46, height=0, relief="flat",padx=2,pady=1, anchor="center", font=("Ivy", 5, "bold"), bg=co0, fg=co0)
    app_.place(x=30, y=63)

    app_= Label(frame_baixo, text=" ", width=46, height=0, relief="flat",padx=2,pady=1, anchor="center", font=("Ivy", 5, "bold"), bg=co0, fg=co0)
    app_.place(x=30, y=127)












# botão jogar

b_jogar= Button(frame_baixo,command=iniciar_jogo, text="Play", width=10,height=1, font=("Ivy", 10, "bold"), overrelief=RIDGE,relief="raised", bg=fundo, fg=co0)
b_jogar.place(x=85,y=197)














janela.mainloop()
