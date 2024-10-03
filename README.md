# OAuth 2.0 com Django

Este é o repositório para o projeto de duas páginas feito em Django para o Python Brasil 2024. Faça o download dos arquivos iniciais e vamos iniciar!

## Configuração do Ambiente Virtual (venv)

Para garantir um ambiente de desenvolvimento limpo e isolado, é recomendável usar um ambiente virtual do Python. Siga as etapas abaixo para configurar e ativar o ambiente virtual:

1. Abra o terminal e navegue até o diretório raiz do projeto.
2. Crie um novo ambiente virtual dentro do diretório do projeto:

    ```
    python -m venv venv
    ```

3. Ative o ambiente virtual. No Windows, execute:

    ```
    venv\Scripts\activate
    ```

    No macOS/Linux, execute:

    ```
    source venv/bin/activate
    ```

4. Agora você está no ambiente virtual, onde pode instalar dependências necessárias para o funcionamento do projeto.

## Instalando Dependências

Você pode instalar as dependências necessárias para o projeto. Certifique-se de que o ambiente virtual está ativado antes de prosseguir. Execute o seguinte comando:

```
pip install -r requirements.txt
```

Este comando instalará todas as dependências listadas no arquivo `requirements.txt`.

## Migrações do Banco de Dados

Antes de iniciar a aplicação, é necessário aplicar as migrações ao banco de dados. Certifique-se de estar no ambiente virtual e no diretório raiz do projeto. Execute o seguinte comando:

```
python manage.py makemigrations
python manage.py migrate
```

Isso aplicará todas as migrações pendentes ao banco de dados.

## Executando a Aplicação

Após configurar o ambiente virtual, instalar as dependências e aplicar as migrações, você pode iniciar o servidor de desenvolvimento Django. Certifique-se de estar no ambiente virtual e no diretório raiz do projeto. Execute o seguinte comando:

```
python manage.py runserver
```

Isso iniciará o servidor de desenvolvimento em `http://localhost:8000/`. Você pode acessar este URL em seu navegador para interagir com a aplicação.
