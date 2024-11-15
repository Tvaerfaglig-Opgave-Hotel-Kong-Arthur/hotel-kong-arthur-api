# Public Gateway: NOT UPDATED
Håndterer hotellets offentlige informationer som drinks og deres priser samt værelsestyper.

## API Endpoints

### See all drinks

- **URL:** `/drinks`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns drinks data
  - **204 No content:** drinks is empty
  - **500:** Some error happened

### See all room type items

- **URL:** `/room_types`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns room_type data
  - **204 No content:** No items in room_type
  - **500:** Some error happened

