# Manual da API

Aplicação para controle de Leads. Aplicação capaz de realizar um CRUD completo usando SQLAlchemy, Dataclass, Blueprint, Migrations e Padrão Flask Factory.

Lead: São pessoas que podem estar interessados em algum tipo de produto ou serviço. Esses possíveis futuros clientes podem ser coletados através de preenchimento de formulários ou cliques em páginas da internet, os dados geralmente são utilizados em campanhas publicitárias.

## Cadastrar lead:
POST http://{BASE_URL}/lead

```json
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
}
```
#

## Ver todos os leads:
GET http://{BASE_URL}/lead

```json
[
  {
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Tue, 05 Oct 2021 00:00:00 GMT",
    "last_visit": "Tue, 05 Oct 2021 00:00:00 GMT",
    "visits": 1
  },
  {
    "name": "Math",
    "email": "math@email.com",
    "phone": "(41)90000-1111",
    "creation_date": "Tue, 05 Oct 2021 00:00:00 GMT",
    "last_visit": "Tue, 05 Oct 2021 00:00:00 GMT",
    "visits": 1
  }
]
```
#

## Atualizar um lead:
PATCH http://{BASE_URL}/lead

 Atualiza apenas o valor de visits e last_visit em cada requisição. O email do Lead deve ser utilizado para encontrar o registro a ser atualizado. A cada requisição o valor de visits acrescenta em 1 e o valor de last_visit é atualizado para a data do request.

```json
{
    "email": "john@email.com"
}
```
#

## Deletar um post:
DELETE http://{BASE_URL}/lead

```json
{
    "email": "john@email.com"
}
```
#