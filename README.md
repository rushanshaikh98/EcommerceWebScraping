# E-Commerce Web Scrapping

## Setup

### Create a virtualenv and install the requirements
```
python3 -m virtualenv myvenv
# activate the virtual enviroment
source myvenv/bin/activate
pip install -r requirements.txt
```

### Start the app.
```
python3 main.py
```
This will start the server at **localhost** on port **5000** (http://127.0.0.1:5000).

## API Endpoint
**Endpoint:** `/api/get/product_details`

**Method**: POST

### Request Body
> URL: str (Link of the detail page of a product)

Example
```json
{
    "url": "https://www.example.com/products/xxxxx/"
}
```

### RESPONSE

#### SUCCESS
```json
{
    "data": {
        "brand_name": "",
        "product_image": [
            
        ],
        "product_name": "",
        "product_price": ""
    },
    "status": "success"
}
```

#### FAILURE
```json
{
    "details": "Received 404 response for URL: 'https://www.example.com/products/xxxxx/'",
    "status": "error"
}
```