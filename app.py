"""
1º Entrar com os dados do artísta:
> nome real;
> nome artístico;
> data de nascimento;
> nacionalidade;
> naturalidade;
> data de falecimento;
> adicionar foto (mais jovem e atual);

2º Contar um pouco da história/trajetória:

3º Inserir algumas músicas;

"""

nome = "Reginaldo Rodrigues dos Santos"
nome_art = "Reginaldo Rossi"
data_nasc = "14 de fevereiro de 1944"
data_fal = "20 de dezembro de 2013"
nacional = "brasileiro"
natural = "Recife/PE"
# imagens

nome_art = input("Digite o nome do artísta: ")
print(f"{nome}, mais conhecido como {nome_art}, é {nacional}, nascido em {data_nasc} na cidade de {natural}. Faleceu no dia {data_fal}.")
