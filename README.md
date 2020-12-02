# book-store

## Instalar e rodar a aplicação
- Clonar repositorio para uma pasta
- Executar o comando "docker-compose build" na raiz do projeto
- Executar o comando "docker-compose up -d" na raiz do projeto

## Comandos requisitados
Para executar os comandos requisitados no enunciado do problema, primeiramente entrar dentro do container da aplicação através do comando "docker-compose exec web sh"
Logo após, é necessario inicializar o banco de dados através do comando "python manage.py db init" e realizar o migrate através do comando "pyton manage.py db upgrade"
Para as operações requisitadas, executar os seguintes comandos:
- Adicionar 3 usuarios = "python manage.py add_3_users"
- Adicionar 5 livros = "python manage.py add_5_books"
- Adicionar 3 transações = "python manage.py add_3_transactions"

## Endpoints requisitados
Para acessar as informacoes de um usuario através do seu id, acessar a url "http://localhost:5000/customers/<id>"
  
Para acessar as informacoes de todos usuarios, acessar a url "http://localhost:5000/customers/"

Para inserir um usuário, realizar um POST para o endpoint "http://localhost:5000/customers/" com um form data contendo os dados necessários, exemplo:

  name:"teste"
  
  email:"teste@teste.com"
  
  address:"rua"
  
  phone:"123123123"
  
  city:"cidade"
  
  state:"estado"
  
  zipcode:"1234567-89"
      
