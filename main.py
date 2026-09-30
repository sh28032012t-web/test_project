from rest_request.get_users import router as router_get_user
from rest_request.post_users import router as router_post_user

from schemes.config import app


app.include_router(router_get_user)
app.include_router(router_post_user)