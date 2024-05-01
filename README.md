# MeasureMate

Bem-vindo ao repositório do MeasureMate!

O MeasureMate é uma plataforma dedicada à aplicação prática de algoritmos de extração de medidas corporais e à determinação do tamanho ideal de vestuário com base nessas medidas. Este repositório foi criado com o propósito de hospedar o código-fonte e os recursos relacionados ao servidor web do MeasureMate.

**Nota Importante:** Por questões de desenvolvimento próprio, os algoritmos fundamentais utilizados no MeasureMate não estão disponíveis neste repositório.

## Sobre o Projeto

O MeasureMate visa fornecer uma solução fácil de usar para determinar o tamanho correto de vestuário com base nas medidas corporais dos usuários. Ele simplifica o processo de compras online, ajudando os usuários a escolherem o tamanho mais adequado sem a necessidade de experimentar fisicamente as roupas.

## Frameworks e Tecnologias Utilizadas

- **Django:** Utilizamos o framework Django para desenvolver o backend da aplicação devido à sua robustez, flexibilidade e familiaridade com a linguagem Python.
- **HTML, CSS e JS:** O frontend do MeasureMate é desenvolvido utilizando HTML, CSS e JavaScript. Adotamos uma abordagem de personalização de templates pré-existentes para alcançar a estética desejada.
-  **OpenCV:** Utilizei da OpenCV para o processamento da imagem no algoritmo de extração de medidas corporais.
- **NumPY:** Utilizei para fazer as operações na imagem após ser lida pelo OpenCV.
- **MediaPipe:** Ela é uma biblioteca de pose, foi utilizada para traçar pose no ser humano, também foi utilizada no algoritmo de extração de medidas corporais. 
- **SkFuzzy:** Foi utilizada para traçar a lógica fuzzy a qual determina o tamanho do vestuário ideal da pessoa com base nas medidas corporais dela, para ela funcionar é necessário que instale também a biblioteca matplotlib. 

## Configuração do Ambiente de Desenvolvimento

Siga as etapas abaixo para configurar o ambiente de desenvolvimento local:

1. Clone este repositório: `git clone https://github.com/valeragabriel/MeasureMate.git`
2. Crie e ative um ambiente virtual:
    ```bash
    mkvirtualenv <nome_do_projeto>
    workon <nome_do_projeto>
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Execute as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Crie um superusuário para acessar o painel de administração em http://127.0.0.1:8000/admin/:
    ```bash
    python manage.py createsuperuser
    ```
6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
7. Dockerfile:
    ```
    Para garantir que o servidor web funcione sem problemas, optei por utilizar o Docker. O Docker é uma ferramenta usada para implantar aplicativos em containers virtuais, permitindo que vários aplicativos funcionem em diferentes ambientes de forma simplificada. Nesse código tem o arquivo Docker mostrando o passo a passo do que tem que fazer para funcionar o código. 
    ```
8. Back4app:
    ```
    cluir as etapas acima, é hora de disponibilizar o código no GitHub. Em seguida, acesse o Back4app para criar um novo projeto. Escolha a opção de servidor com containers e autorize o acesso ao seu repositório no GitHub. Selecione o projeto que você deseja implantar como servidor web. O Back4app realizará o deploy e a construção do projeto, gerando um link acessível que será hospedado online. Após isso, volte ao seu código e adicione o link gerado no arquivo settings.py, na seção onde está definido ALLOWED_HOSTS = ['link_gerado_pelo_back4app']. Faça o commit dessas alterações e retorne ao Back4app. Aguarde a conclusão do processo de construção e, em seguida, acesse o link gerado para visualizar o código disponível na web.
    ```

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).