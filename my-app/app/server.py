from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    """
    Redirects the root URL ("/") to the documentation page ("/docs").

    Returns:
        RedirectResponse: A FastAPI response that redirects to another page.
    """
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, NotImplemented)

"""
This function adds routes to the FastAPI application. It is currently not implemented.

Parameters:
    app (FastAPI): The FastAPI application to add routes to.
    NotImplemented: This parameter is not yet implemented.

Raises:
    NotImplementedError: This function will raise a NotImplementedError if called.
"""

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
