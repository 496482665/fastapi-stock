from typing import Union

import uvicorn
from fastapi import FastAPI, Request, Query, UploadFile, Form, File
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from api.base import router

from initlize.db import init_db, close_db
from initlize.app import init_app
from initlize.schedules import init_schedule, close_schedule


# 构造app
def get_application() -> FastAPI:
    app = FastAPI()

    # 添加数据库钩子
    app.add_event_handler(
        "startup",
        init_db,
    )
    app.add_event_handler(
        "shutdown",
        close_db,
    )

    # 添加周期任务钩子
    app.add_event_handler(
        "startup",
        init_schedule,
    )
    app.add_event_handler(
        "shutdown",
        close_schedule,
    )

    # 添加路由
    app.include_router(router, prefix="/api")

    return app


app = get_application()


@app.get("/")
def root_page():
    return RedirectResponse("/docs")


@app.post("/common/{common_id}")
def get_common(common_id: int, request: Request, name: str = Form(), price: int = Form()):
    print(common_id, request, name, price)
    return common_id


# 上传文件
@app.post("/uploadFile")
def upload_file(file: UploadFile = File(...)):
    print(file.filename)
    return {}


# 执行重定向到指定URL
@app.get("/redirect")
def redirect(q: str = Query(
    None,
    min_length=2,
    max_length=50,
    title="Query parameter",
    description="添加了就不跳转",
    deprecated=True,
)):
    if q:
        # 添加请求头
        headers = {"X-Custom-Header": "custom-header-value"}
        return JSONResponse(headers=headers, content={})
    return RedirectResponse(url="https://www.baidu.com", status_code=302)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=8001)
