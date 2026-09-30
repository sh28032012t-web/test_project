from rest_request.get_users import router as router_get_user
from config import app

app.include_router(router_get_user)