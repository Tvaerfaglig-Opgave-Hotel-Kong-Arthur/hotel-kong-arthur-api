# Drinks Service: 
Håndterer brugerens drinks kort.
Tilbyder funktioner til at tilføje, fjerne og opdatere drinks databasen.

## API Endpoints

### See all drinks

- **URL:** `/drinks`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns drinks data
  - **204 No content:** drinks is empty
  - **500:** Some error happened

### See all drinks prices in a descending order

- **URL:** `/drinks/prices`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns drink prices data
  - **204 No content:** drinks is empty
  - **500:** Some error happened

### Get drinks order by category

- **URL:** `/drinks/<category>`
- **Method:** `GET`
- **Example** `/drinks/Cocktail`

- **Response:**

  - **200 OK:** Returns drinks order by the entered category data
  - **204 No content:** drinks is empty
  - **500:** Some error happened

### Add new drinks to the card

- **URL:** `/drinks`
- **Method:** `POST`
- **Request Body:** JSON

  ```json
  {
    "drink_name": "Coca Cola Zero",
    "category": "Soda",
    "price": 45,
    "units_sold": 100
  }
  ```

- **Response:**

  - **201 Created:** Drink added to database successfully
  - **500:** Some error happened

### Delete drink from database

- **URL:** `/drinks/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Drink deleted from database successfully
  - **404 Not Found:** Drink not found
  - **500:** Some error happened

### Update drink price

- **URL:** `/drinks/<id>`
- **Method:** `PATCH`
- **Request Body:** JSON

  ```json
  {
      "price": 75.95
  }
  ```

- **Response:**

  - **200 OK:** Updates applied, details: price: 75.95
  - **400:** No valid fields provided
  - **500:** Some error happened


### Update units sold 
- **URL:** `/drinks/<id>`
- **Method:** `PATCH`
- **Request Body:** JSON

  ```json
  {
      "units_sold": 225
  }
  ```

- **Response:**

  - **200 OK:** Updates applied, details: units sold: 225
  - **400:** No valid fields provided
  - **500:** Some error happened
   
**It's possible to update both price and units sold at the same time**