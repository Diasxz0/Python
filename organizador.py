import os 
import shutil





download = os.path.expanduser('~/Downloads')
arquivos = os.listdir(download)

#Cria a pasta 'pdf' no destino 'download'
pdf = os.path.join(download, 'pdf')
txt = os.path.join(download, 'txt')
exe = os.path.join(download, 'exe')
mp4 = os.path.join(download, 'mp4')
zipp = os.path.join(download, 'zip')
rar = os.path.join(download, 'rar')
jpg = os.path.join(download, 'jpg')

#printa todos o caminho pra dowloaf
print(f'Pasta de Downloads: {download}')

# caso nao exista a pasta pdf, cria ela
if not os.path.exists(pdf):
    os.makedirs(pdf)

if not os.path.exists(txt):
    os.makedirs(txt)

if not os.path.exists(zipp):
    os.makedirs(zipp)

if not os.path.exists(rar):
    os.makedirs(rar)

if not os.path.exists(mp4):
    os.makedirs(mp4)

if not os.path.exists(exe):
    os.makedirs(exe)

if not os.path.exists(jpg):
    os.makedirs(jpg)



# printa arquivos da pasta de downloads
print('Esses são os arquivos da sua pasta de dowload:')
for arquivo in arquivos:
    print(arquivo)
    #cria o caminho de origem, falando que o arquivo
    # está em download e será dirigido para 'pdf', 'txt', etc
    origem = os.path.join(download, arquivo)
    destinopdf = os.path.join(pdf, arquivo)
    destinotxt = os.path.join(txt, arquivo )
    destinoexe = os.path.join(exe, arquivo )
    destinomp4 = os.path.join(mp4, arquivo)
    destinorar = os.path.join(rar, arquivo)
    destinozipp = os.path.join(zipp, arquivo)
    destinojpg = os.path.join(jpg, arquivo)
    #se aqrquivo terminar com '', tranfira ele da origem para ''
    if arquivo.endswith('.pdf'):
        shutil.move(origem, destinopdf)
    if arquivo.endswith(('.txt','.doc')):
        shutil.move(origem, destinotxt)
    if arquivo.endswith('.exe'):
        shutil.move(origem, destinoexe)
    if arquivo.endswith('.mp4'):
        shutil.move(origem, destinomp4)
    if arquivo.endswith('.zip'):
        shutil.move(origem, destinozipp)
    if arquivo.endswith('.rar'):
        shutil.move(origem, destinorar)
    if arquivo.endswith(('.jpg', '.jpeg', '.png')):
        shutil.move(origem, destinojpg)
print('Olhe sua pasta de downloads, novas pastas devem ter sido abertas')

       
