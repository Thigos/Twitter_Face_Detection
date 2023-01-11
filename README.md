# Detectando rostos em vídeos do Twitter

Com este código, a partir de palavras chaves, será feita a detecção e armazenamento de faces encontradas nos vídeos publicados no Twitter

# Usando o Script

1 - Acesse a pasta raiz do projeto

```sh
cd Twitter_Facial_Detect
```

2 - Instale as Libs necessárias

```sh
pip install -r requirements.txt
```

3 - Adicione palavras chaves no arquivo ``query.txt`` (Separadas por quebra de linha)

4 - Execute o Scritp

```sh
python3 main.py
```

#### FLAGS

```sh
python3 main.py -p [PATH_DO_QUERY.txt]
```

# Dados

Todos os dados serão salvos na pasta ``data``

# Debug - Etapas do Código

1. Download do Firefox, caso necessário. (código em ``firefox_downloader.py``)</br>
    1- Download pelo servidor ftp.mozilla.org</br>
    2- Extração do ZIP para a pasta ``downloads/firefox``
    
2. WebScraping com o Selenium-Wire na página de pesquisa do Twitter, filtrado pela palavra chave e por vídeos. (código em ``twitter_scraping.py``)</br>
    1- Load do Firefox controlado pelo Selenium</br>
    2- GET na URL</br>
    3- Análise do tráfico de rede da página</br>
    4- GET de todos os vídeos disponíveis
    
3. Análise dos vídeos e armazenamento dos arquivos. (código em ``main.py``)</br>
    1- Detecção de faces para cada vídeo encontrado na etapa 2</br>
    2- Armazenamento das faces na pasta ``data/PALAVRA_CHAVE_face_crop/frame_(CONTAGEM_DE_FRAMES)_face_CONTAGEM_DE_FACES.png``</br>
    3- Armazenamento de cada frame que contenha 1 ou + faces ``data/PALAVRA_CHAVE/frame_CONTAGEM_DE_FRAMES.png``

# Constantes

#### MAX_TRY = 10 -> ``twitter_scraping.py``
Número de tentativas para pegar links dos vídeos. Para cada tentativa o Scroll da página será setado para TAMANHO_DA_JANELA*(NUM_TENTATIVA/2)


