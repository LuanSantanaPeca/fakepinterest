Projeto de cópia de funções básicas do Pinterest (criação de conta, login, upload de imagens, separação de imagens por conta)
Utiliza HTML, CSS e Python (no lugar de JS para a lógica)

Funciona com um Postgres local. Só roda localmente, não coloquei em nenhum servidor por ser um projeto pequeno.

Para visualizar o projeto (construído no Python 3.12):
1. Baixe o repositório em sua integridade;
2. Extraia o arquivo .zip;
3. Abra a pasta fakepinterest-main em um editor de código;
3/1. Também é possível rodar diretamente pelo CMD ou PowerShell, navegando diretamente até a pasta fakepinterest-main;
4. No terminal, rode a linha:
   py -m pip install Flask Flask-SQLAlchemy Flask-Login Flask-Bcrypt Flask-WTF email-validator
   para baixar todas as dependências;
5. Ainda no terminal, rode:
   py main.py
6. O projeto rodará em um servidor local, indicado no próprio terminal

Possível sequência de testes sugerida:
- Crie uma conta com email, nome de usuário e senha;
- Vá para a aba de perfil e faça upload de uma ou duas imagens;
- Saia da conta criada;
- Escolha "Navegar como visitante";
Nesse caso as imagens colocadas pela conta logada ainda aparecerão, mas não existirá uma página de perfil ou como fazer upload enquanto visitante.
É possível também criar mais de uma conta para os testes. Nesse caso, todas as contas poderão ver todos os uploads, mas cada um verá somente seus próprios uploads na página de perfil.

Ao parar o servidor local (com Ctrl + C) o sql local criado anteriormente é deletado, então parar o servidor e iniciá-lo novamente fará com que todas as contas e imagens sejam apagadas.

*Utilização de Inteligência Artificial para auxiliar no desenvolvimento do sistema de apagar o banco de dados local quando encerrando o servidor, desenvolvido bastante tempo após o projeto original.*
