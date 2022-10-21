"""
1º Entrar com os dados do artísta:
> nome real;
> nome artístico;
> data de nascimento;
> nacionalidade;
> naturalidade;
> data de falecimento;
> adicionar foto;

2º Contar um pouco da história/trajetória.

3º Inserir algumas músicas.

"""
import tkinter as tk
from turtle import right
from PIL import ImageTk, Image

nome = "Reginaldo Rodrigues dos Santos"
nome_art = "Reginaldo Rossi"
data_nasc = "14 de fevereiro de 1944"
data_fal = "20 de dezembro de 2013"
nacional = "Brasileiro"
natural = "Recife/PE"


class Tela:
    def __init__(self, master):
        self.nossaTela = master
        img = Image.open("C:\Projetos\star_stories\img\inaldo_rossi.png")
        self.minhaImagem = ImageTk.PhotoImage(img)
        self.lbl = tk.Label(self.nossaTela, image=self.minhaImagem,
                            compound=tk.LEFT, text=f"Nome completo: {nome}\n"
                                                  f"Nascimento: {data_nasc}\n"
                                                  f"Falecimento: {data_fal}\n"
                                                  f"Nacionalidade: {nacional}\n"
                                                  f"Naturalidade: {natural}\n"
        f"{nome_art} foi professor de matemática e estudou engenharia antes de iniciar sua carreira artística "
        f"no ano de 1964, \ncomo integrante do conjunto The Silver Jets. \nEmbora ele tenha sido conhecido como o"
        f" Rei do Brega, Reginaldo Rossi iniciou a sua carreira cantando Iê-Iê-Iê. \nSeu primeiro sucesso foi 'O Pão',"
        f" também nome do seu primeiro disco. \nNa década de 70 Reginaldo Rossi se afastou do estilo rock com o "
        f"trabalho 'À Procura de Você', onde deu início no gênero brega.\nSeu maior sucesso foi a música "
        f"'Mon Amour, Meu Bem, Ma Femme', regravada por vários outros artístas.\nNa década de 70 também houveram "
        f"outros hits como 'Desterro' e 'Pedaço de Mau Caminho'.\nNa década de 80 Reginaldo Rossi ganhou o seu primeiro "
        f"disco de ouro com o álbum 'A Volta' e também lançou um de seus maiores sucessos,"
        f"\na música 'Garçom', alcançando a marca de dois milhões de cópias vendidas e uma das primeiras músicas "
        f"cantadas por vários outros cantores.\nEm fins da década de 90 Reginaldo Rossi ressurgiu no sul do país, "
        f"relançando seus discos em CD.\nO cantor e compositor passou a ser visto como 'cult' e assinou contrato com "
        f"a gravadora Sony. Na política, Reginaldo Rossi foi candidato a vereador \nno município "
        f"de Jaboatão dos Guararapes em 2008 e deputado estadual em 2010, não obtendo êxito em nenhuma delas."
        f"\nNo dia 09 de dezembro de 2013, Reginaldo Rossi passou por um procedimento médico retirando "
        f"dois litros de líquido acumulados entre a pleura e o pulmão.\nO resultado da biópsia confirmou o diagnóstico "
        f"de câncer de pulmão, doença que causou seu falecimento. Oito meses após o a sua morte,"
        f"\nno dia 15 de agosto de 2014, sua viúva Celeide Neves também faleceu, aos 67 anos, de infarto.",
        bg="#99FFCC"
        )
        
        self.lbl.image = self.minhaImagem
        self.lbl.pack()

janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()


