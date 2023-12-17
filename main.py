from fastapi import FastAPI, HTTPException

app = FastAPI(redirect_slashes=False)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def say_hello():
    return {"message": "Hello!"}


reports = {
    "1": {"title": "Report 1", "description": "This is a report"},
    "2": {"title": "Report 2", "description": "This is another report"},
    "3": {"title": "Report 3", "description": "This is a third report"}
}


@app.get("/reports")
async def get_reports():
    return reports


@app.delete("/reports/{report_id}", status_code=204)
async def delete_report(report_id: str):
    if report_id in reports:
        del reports[report_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
