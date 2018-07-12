# Quantified Self (Django)
  This application is an API designed to handle the backend processes of a frontend 'meal and food manager' called [Quantified Self Front End](https://github.com/anubiskhan/qs_frontend_django). The frontend is deployed via [GitHub Pages](https://anubiskhan.github.io/qs_frontend_django/), while the backend is hosted on an instance of Heroku. MY [Heroku App](https://serene-savannah-88118.herokuapp.com/api/v1/foods/api/v1/foods) instance.

  It is essentially a collection of endpoints that provide CRUD functionality for Food, and psuedo-CRUD functionality for Meals. (An end user cannot create or destroy meals, but is able to create associations between pre-seeded meals and foods).

### Setup
##### Requirements
  - Python 3 +
  - Django 2 +

In order to consume the API, take the following steps:
  1. Clone down this repository to your local machine
  ```
  git clone git@github.com:anubiskhan/quantified-self-django.git
  ```
  and head into the directory
  ```
  cd quantified-self-django/
  ```
  2. Run the following on your command line in order to make sure that you'll have all of the necessary packages
  ```
  pip3 install -r requirements.txt
  ```

  3. In order to get the database established and seeded run the following on your command line
  ```
  python3 manage.py migrate
  ```
  4. Initialize the server by running the following on your command line
  ```
  python3 manage.py runserver 3000
  ```

### Endpoints

#### Foods
To retrieve a list of all foods in the database
```
GET /api/v1/foods
```
Returns all food objects

To retrieve a single food
```
GET /api/v1/foods/:id
```
Returns the food object with the given :id OR a 404 status if the food is not found

To add a food object to the database
Use format:
{
    "food": {
        "name": "newFood",
        "calories": "10"
    }
}
```
POST /api/v1/foods/
```
Creates a new food object
Returns the food object OR a 400 status if the food fails to create

To update an existing food(Must have both name and calories filled out)
Use format:
{
    "food": {
        "name": "newFood",
        "calories": "10"
    }
}
```
PATCH /api/v1/foods/:id
```
Updates the existing food object with the given :id
Returns the food object OR a 400 status if the food fails to update

To delete an existing food
```
DELETE /api/v1/foods/:id
```
Deletes the existing food object with the given :id
Returns status 204 OR 404 if the food fails to delete

#### Meals
To retrieve a list of all meals and each meal's associated foods
```
GET /api/v1/meals
```
Returns all meal objects along with associated foods

To retrieve a single meal and its associated foods
```
GET /api/v1/meals/:meal_id/foods
```
Returns the meal of given :meal_id with associated food objects OR a 404 status if the meal cannot be found

To create an association between an existing meal and an existing food
Use format:
{
    "food": {
    	"id": 1
    }
}
```
POST /api/v1/meals/:meal_id/foods/:id
```
Creates a new association between the meal object and food object of the given :meal_id and :id, respectively
Returns a 201 status and the message {"message": "Successfully added FOODNAME to MEALNAME"} OR a 404 status if the post fails

To delete an association between an existing meal and an existing food
```
DELETE /api/v1/meals/:meal_id/foods/:id
```
Deletes the association between the meal object and food object of the given :meal_id and :id, respectively
Returns the message {"message": "Successfully removed FOODNAME to MEALNAME"} OR a 404 status if the delete fails
