from schemes.config import app
from schemes.api_router import router

import rest_request.get_users
import rest_request.post_users
import rest_request.delete_users
import rest_request.put_users

app.include_router(router)