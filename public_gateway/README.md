# Public Gateway: NOT UPDATED
Håndterer hotellets offentlige informationer som drinks og deres priser samt værelsestyper.

## API Endpoints

### See all room type items

- **URL:** `/room_types`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns room_type data
  - **204 No content:** No items in room_type
  - **500:** Some error happened