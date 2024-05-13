## Bibliotecas utilizadas
Criei esta pasta para aprofundar a discussão sobre as bibliotecas utilizadas em minhas APIs. Se você estiver interessado, separei-a em quatro pastas principais, cada uma com o nome de uma biblioteca específica (MediaPipe, NumPy, OpenCV e SkFuzzy). Cada pasta contém uma contextualização geral da biblioteca, um guia passo a passo sobre como utilizá-la e exemplos de código para ilustrar seu uso.

## Frontend 
Para o Frontend foi usado HTML, CSS e JS. Peguei templates prontos e fui modificando, tudo que está sendo usado no frontend estão nas seguintes páginas do código: 

- **static:** Nesta pasta, encontramos todos os recursos estáticos do projeto, como imagens, folhas de estilo (CSS) e scripts (JavaScript).

- **templates:** Os templates desempenham um papel crucial ao permitir a inserção de dados dinâmicos gerados pelo backend. Esta separação de responsabilidades facilita a manutenção do código e a implementação de designs coesos e flexíveis.

1. HTML: 
HTML, ou Hypertext Markup Language, é a espinha dorsal da internet. É uma linguagem de marcação que define a estrutura e o conteúdo de uma página da web. No cerne do HTML está a ideia de marcação. As tags HTML são elementos fundamentais que envolvem e estruturam o conteúdo de uma página da web. Cada tag possui uma função específica, desde definir títulos e parágrafos até inserir imagens e criar links para outras páginas.

Uma página HTML básica começa com a tag <html>, que indica o início do documento HTML. Dentro desta tag, encontramos duas seções principais: <head> e <body>. A seção <head> contém metadados, como o título da página e links para folhas de estilo CSS, enquanto a seção <body> contém o conteúdo visível da página, como texto, imagens e elementos interativos.

2. CSS: 
CSS, ou Cascading Style Sheets, é uma linguagem de estilo usada em conjunto com o HTML para controlar a apresentação e o layout de páginas da web. Enquanto o HTML define a estrutura e o conteúdo de uma página, o CSS permite que os desenvolvedores determinem a aparência visual, o design e a experiência do usuário.

A estrutura básica do CSS é composta por seletores e declarações. Os seletores são padrões que identificam os elementos HTML aos quais as regras de estilo serão aplicadas, enquanto as declarações especificam como esses elementos devem ser estilizados. Por exemplo, um seletor pode ser uma classe (class) ou um identificador (id) em HTML, e as declarações podem definir propriedades como cor, tamanho, fonte e espaçamento.

3. JS: 
Ao contrário do HTML, que é uma linguagem de marcação para estruturação de conteúdo, e do CSS, que é uma linguagem de estilos para apresentação visual, o JavaScript adiciona comportamento e dinamismo às páginas da web. Com JavaScript, os desenvolvedores podem responder a eventos do usuário, manipular elementos HTML, criar animações, validar formulários e muito mais.

Uma das características mais poderosas do JavaScript é sua capacidade de manipular o DOM (Document Object Model). O DOM é uma representação em árvore dos elementos HTML de uma página e suas propriedades. Com JavaScript, os desenvolvedores podem acessar e modificar o DOM em tempo real, permitindo atualizações dinâmicas e interações responsivas com o usuário.

## Backend 
O backend da página web foi todo desenvolvido em Python Django https://www.djangoproject.com

- **Django:** Foi utilziado o framework Django para desenvolver o backend da aplicação devido à sua robustez, flexibilidade e familiaridade com a linguagem Python. Vale ressaltar também que por as APIs serem feitas com a ligugaem python, facilita para chamar as APIs no Django. 

- **measure_mate:** Essa é a pasta central do projeto Django, representando o núcleo do sistema. Ao iniciar um novo projeto, é aqui que começamos, pois contém todas as configurações essenciais, como definições de banco de dados, configurações de segurança e outros elementos fundamentais para a execução do projeto.

- **main:** A pasta main desempenha um papel vital na organização do backend do projeto. É aqui que estruturamos e implementamos as funcionalidades principais, como a definição de modelos de dados, criação de rotas para acessar as APIs e a implementação da lógica de negócios principal.
