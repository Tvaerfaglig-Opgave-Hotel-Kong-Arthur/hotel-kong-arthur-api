# Reservations Service: NOT UPDATED
Håndterer hotellets reservationer af værelser.
Tilbyder funktioner til at se, tilføje, fjerne og opdatere reservationer.

## API Endpoints

### See all reservations

- **URL:** `/reservations`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns reservations data
  - **204 No content:** reservations is empty
  - **500: Error** Some error occured

### See reservation by id

- **URL:** `/reservations/<id>`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns reservation data
  - **204 No content:** reservation not found
  - **500: Error** Some error occured

### Add new reservation

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

### Delete reservation

- **URL:** `/reservations/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Item deleted from reservations successfully
  - **404 Not Found:** Item not found
  - **500: Error** Some error occured

### Update reservation

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

