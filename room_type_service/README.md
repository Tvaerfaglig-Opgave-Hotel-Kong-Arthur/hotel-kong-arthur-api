# Room type service:
Håndterer Værelsestyperne.
Tilbyder funktioner til at tilføje, fjerne og opdatere værelsestyper.

## API Endpoints

### See all room type items

- **URL:** `/room_types`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns room_type data
  - **204 No content:** No items in room_type
  - **500:** Some error happened

### Find room by id

- **URL:** `/room_types/<int:id>`
- **Method:** `GET

- **Response:**

  - **200 OK:** Returns room_type data by id
  - **404 Not found:** Item not found
  - **500:** Some error happened


### Add new room type

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

### Delete item from room type

- **URL:** `/room_types/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Item deleted from room type successfully
  - **404 Not Found:** Item not found
  - **500:** Some error happened

### Update product amount

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

   
