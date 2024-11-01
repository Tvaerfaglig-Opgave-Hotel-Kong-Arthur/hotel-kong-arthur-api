# Admin Gateway: NOT UPDATED
- Add csv endpoints
- drinks and guest endpoints
Gateway, som giver adgang til alle endpoints.

## API Endpoints

### Drinks service endpoints

#### See all drinks

- **URL:** `/drinks`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns drinks data
  - **204 No content:** drinks is empty
  - **500:** Some error happened

#### See all drinks prices in a descending order

- **URL:** `/drinks/prices`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns drink prices data
  - **204 No content:** drinks is empty
  - **500:** Some error happened

#### Get drinks order by category

- **URL:** `/drinks/<category>`
- **Method:** `GET`
- **Example** `/drinks/Cocktail`

- **Response:**

  - **200 OK:** Returns drinks order by the entered category data
  - **204 No content:** drinks is empty
  - **500:** Some error happened

#### Add new drinks to the card

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

#### Delete drink from database

- **URL:** `/drinks/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Drink deleted from database successfully
  - **404 Not Found:** Drink not found
  - **500:** Some error happened

#### Update drink price

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


#### Update units sold 
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

### Reservation service endpoints

#### See all reservations

- **URL:** `/reservations`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns reservations data
  - **204 No content:** reservations is empty
  - **500: Error** Some error occured

#### See reservation by id

- **URL:** `/reservations/<id>`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns reservation data
  - **204 No content:** reservation not found
  - **500: Error** Some error occured

#### See reservation by guest id

- **URL:** `/reservations/guest/<id>`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns reservation data
  - **204 No content:** reservation not found
  - **500: Error** Some error occured

#### Add new reservation

- **URL:** `/reservations`
- **Method:** `POST`
- **Request Body:** JSON

  ```json
  {
    "first_name": "Alice",
    "family_name": "Johnson",
    "country": "United States",
    "room_type_id": 5,
    "days_rented": 3,
    "season": "high",
    "price": 7543
  }
  ```

- **Response:**

  - **201 Created:** Reservation created successfully
  - **500: Error** Some error occured

#### Delete reservation

- **URL:** `/reservations/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Item deleted from reservations successfully
  - **404 Not Found:** Item not found
  - **500: Error** Some error occured

#### Update reservation

- **URL:** `/reservations/<id>`
- **Method:** `PATCH`
- **Request Body:** JSON

  ```json
  {
    "price": 5743,
    "season": "mid"
  }
  ```

- **Response:**

  - **200 OK:** Reservation updated successfully
  - **404: Not found** No reservation found
  - **500: Error** Some error occured

### Room type service endpoints

#### See all room type items

- **URL:** `/room_types`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns room_type data
  - **204 No content:** No items in room_type
  - **500:** Some error happened

#### Find room by id

- **URL:** `/room_types/<int:id>`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns room_type data by id
  - **404 Not found:** Item not found
  - **500:** Some error happened


#### Add new room type

- **URL:** `/room_types`
- **Method:** `POST`
- **Request Body:** JSON

  ```json
  {
      "type": "Standard Single",
      "low": 950,
      "mid": 1100,
      "high": 1300
  }
  ```

- **Response:**

  - **201 Created:** Item added to room types successfully
  - **500:** Some error happened

#### Delete item from room type

- **URL:** `/room_types/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Item deleted from room type successfully
  - **404 Not Found:** Item not found
  - **500:** Some error happened

#### Update room types 

- **URL:** `/room_types/<id>`
- **Method:** `PATCH`
- **Request Body:** JSON

  ```json
  {
      "low": 2000
  }
  ```

- **Response:**

  - **200 OK:** Room type updated successfully
  - **400:** Room type not found
  - **500:** Some error happened

### Guest service endpoints

#### See all guests

- **URL:** `/guests`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns guests data
  - **204 No content:** guests is empty
  - **500: Error** Some error occured

#### See guest by id

- **URL:** `/guests/<id>`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns guest data
  - **204 No content:** guest not found
  - **500: Error** Some error occured

#### Add new guest

- **URL:** `/guests`
- **Method:** `POST`
- **Request Body:** JSON

  ```json
  {
    "first_name": "Alice",
    "family_name": "Johnson",
    "country": "United States"
  }
  ```

- **Response:**

  - **201 Created:** guest created successfully
  - **500: Error** Some error occured

#### Delete guest

- **URL:** `/guests/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Item deleted from guests successfully
  - **404 Not Found:** Item not found
  - **500: Error** Some error occured

#### Update guest

- **URL:** `/guests/<id>`
- **Method:** `PATCH`
- **Request Body:** JSON

  ```json
  {
    "country": "China"
  }
  ```

- **Response:**

  - **200 OK:** guest updated successfully
  - **404: Not found** No guest found
  - **500: Error** Some error occured