# FastAPI Tour

Learning and Experimenting With FastAPI


### Features of API

1. Automatic Documentation:
   2. FastAPI Generates Automatic Swagger Documentation For ALL Of Oour Endpoint Which We Can Access ``http://<HOST>:<PORT>/docs``
   3. It Also Generates Redoc format documentation which can be accessible via ``http://<HOST>:<PORT>/redoc`` 
   
2. Uses Standard Python3
3. Security and Authentication
4. Dependency Injection
5. Testing:
   6. Provide 100% Coverage
   
   
### Setup

#### Create virtual environment

```commandline
cd fastapi_tour
python -m venv venv
venv\Scripts\activate
```

#### Run your app

```commandline
uvicorn src.main:app --reload
```

### Interesting Features

#### Routers:

- Separate operations into multiple files
- Share prefix between multiple operations
- Share tags

```commandline
from fastapi import APIRouter
router=APIRouter(prefix="/blog", tags=["blog"])

@router.get("/")
```

```commandline
from routers import blog
app = FastAPI()
app.include_router(blog.router)
```