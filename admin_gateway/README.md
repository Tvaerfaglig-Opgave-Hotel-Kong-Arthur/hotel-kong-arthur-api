# Admin Gateway: NOT UPDATED
- Add csv endpoints
- drinks and guest endpoints
Gateway, som giver adgang til alle endpoints.

## API Endpoints

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

### Find room by id

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

#### Update product amount

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

   