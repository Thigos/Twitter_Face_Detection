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

### FLAGS

```sh
python3 main.py -p [PATH_DO_QUERY.txt]
```

# Dados

Todos os dados serão salvos na pasta ``data``

