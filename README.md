# Hotel Kong Arthur Api

## Prerequisites
Before you begin, ensure you have installed the following:
- Python
- Git
- Docker

## Installation

1. Clone repository:

```bash
git clone https://github.com/Tvaerfaglig-Opgave-Hotel-Kong-Arthur/hotel-kong-arthur-api
cd hotel-kong-arthur-api
```

2. Create Docker network:
```bash
docker network create hotel_kong_arthur_network
```

3. For each gateway/microservice, use a separate terminal:

Admin Gateway:
```bash
cd admin_gateway
docker build -t admin_gateway .
docker run -it --name admin_gateway --network hotel_kong_arthur_network --rm -p 5000:5000 admin_gateway
```

Public Gateway:
```bash
cd public_gateway
docker build -t public_gateway .
docker run -it --name public_gateway --network hotel_kong_arthur_network --rm -p 5001:5001 public_gateway
```

Drinks microservice:
```bash
cd drinks_service
docker build -t drinks_service .
docker run -it --name drinks_service --network hotel_kong_arthur_network --rm -p 5002:5002 drinks_service
```

Reservations microservice:
```bash
cd reservations_service
docker build -t reservations_service .
docker run -it --name reservations_service --network hotel_kong_arthur_network --rm -p 5003:5003 reservations_service
```

Room type microservice:
```bash
cd room_type_service
docker build -t room_type_service .
docker run -it --name room_type_service --network hotel_kong_arthur_network --rm -p 5004:5004 room_type_service
```

## Ports:
- 5000: Admin gateway

- 5001: Public gateway

- 5002: Drinks microservice

- 5003: Reservations microservice

- 5004: Room type microservice