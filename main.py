from fastapi import FastAPI
import models
from db.config import Engine
from router import user,post

app = FastAPI( title="Todo API",
    description="Corporate-grade Todo application",
    version="1.0.0",
    docs_url="/docs")
models.Base.metadata.create_all(bind = Engine)

app.include_router(user.api, prefix="")
app.include_router(post.api,prefix="")




