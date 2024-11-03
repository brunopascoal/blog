# Blog Portifólio

![GitHub repo size](https://img.shields.io/github/directory-file-count/brunopascoal/blog?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/top/brunopascoal/blog?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/brunopascoal/blog?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/brunopascoal/blog?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/brunopascoal/blog?style=for-the-badge)

> Este projeto é uma aplicação web desenvolvida com Django que permite aos usuários criar, editar e gerenciar posts que representam seus portfólios. Os usuários podem se registrar, fazer login, criar posts e comentar nos posts existentes. Se um post for criado sem uma imagem, o sistema utiliza a API do ChatGPT para gerar uma imagem automaticamente.



<!-- # Imagens -->

<!-- ![login](https://user-images.githubusercontent.com/49947689/235822991-c530e034-8f8c-4873-a201-96dfb2fc8e2d.png)
![page](https://user-images.githubusercontent.com/49947689/235823020-f2468ada-daaa-4bba-95cf-c26aecb7deaa.png) -->



<!-- ### Atualizações futuras

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Edição e exclusão do post;
- [ ] Login por redes sociais;
- [ ] Otimização do processo;
- [ ] Ajustes na interface; -->

## Funcionalidades

- **Registro e autenticação de usuários**
- **Criação, edição e exclusão de posts**
- **Comentários em posts**
- **Armazenamento de imagens com o Cloudinary**
- **Geração automática de imagens via API do ChatGPT**

## Estrutura do Projeto

- **Core**: Aplicação principal do Django.
- **Accounts**: Aplicação responsável pelo gerenciamento de usuários.
- **Blog**: Aplicação que lida com os posts e comentários.

## Tecnologias Utilizadas

- Django
- Cloudinary para armazenamento de imagens
- API do ChatGPT para geração de imagens
- Python-Decouple para gerenciamento de variáveis de ambiente

## 💻 Pré-requisitos

- Python instalado na máquina
- Conta no Cloudinary para armazenamento de imagens
- Chave de API do ChatGPT
- Ambiente virtual configurado (recomendado)


## 🚀 Instalando blog

Para instalar blog, siga estas etapas:

### Clone o repositório:

```
git clone https://github.com/brunopascoal/blog.git
```

### Entre no diretório do projeto:

```
cd blog
```

### Crie e ative um ambiente virtual

Linux e macOS:

```
python -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\activate
```

### Instale as bibliotecas necessárias:

```
pip install -r requirements.txt
```

### Configure as variáveis de ambiente:

Crie um arquivo .env com as informações
```
API_KEY_OPENAI="sua_api"
CLOUD_NAME_CLOUDINARY="seu_cloud_name"
API_KEY_CLOUDINARY="sua_api"
API_SECRET_CLOUDINARY="sua_secret_key"
```

### Aplique as migrações do banco de dados:

```
python manage.py migrate
```


## ☕ Usando blog

Para usar blog, siga estas etapas:

1.Inicie o servidor

```
python manage.py runserver
```

2.Acesse a aplicação:

Abra o navegador e vá para http://localhost:8000/.

### Uso

- Registro e Login:
  Crie uma nova conta ou faça login com uma conta existente.
- Criar um Post:
    Após o login, crie um novo post para adicionar ao seu portfólio.
    Se nenhuma imagem for fornecida, uma imagem será gerada automaticamente via API do ChatGPT.
- Comentar em Posts:
    Visualize posts existentes e adicione comentários conforme necessário.

## 📫 Contribuindo para blog

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin blog / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.


