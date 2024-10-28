# Guests Service:
Håndterer hotellets gæster.
Tilbyder funktioner til at se, tilføje, fjerne og opdatere gæster.

## API Endpoints

### See all guests

- **URL:** `/guests`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns guests data
  - **204 No content:** guests is empty
  - **500: Error** Some error occured

### See guest by id

- **URL:** `/guests/<id>`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns guest data
  - **204 No content:** guest not found
  - **500: Error** Some error occured

### Add new guest

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

### Delete guest

- **URL:** `/guests/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Item deleted from guests successfully
  - **404 Not Found:** Item not found
  - **500: Error** Some error occured

### Update guest

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

