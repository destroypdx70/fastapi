from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieServices
from schemas.movie import movie


movie_router = APIRouter()

@movie_router.get("/movies", tags=["movies"], response_model=List[movie])
def get_movies() -> List[movie]:
    db = session()
    result = MovieServices(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.get("/movies/{id}", tags=["movies"], response_model=movie, status_code=200, dependencies=[Depends(JWTBearer)])
def get_movie(id: int = Path(ge=1,le=2000)) -> movie:
    db = session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"Message": "The movie does not has been found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.get("/movies/", tags=["movies"], response_model=List[movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[movie]:
    db = session()
    result = MovieServices(db).get_movies_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
 

@movie_router.post("/movies", tags=["movies"], response_model=dict, status_code=201)
def create_movie( movie: movie) -> dict:
    db = session()
    MovieServices(db).create_movie(movie)
    return JSONResponse(status_code=201,content={"message" : "The movie has been register"})


@movie_router.put("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def update_movie(id: int, movie: movie) -> dict:
    db = session()
    result = MovieServices(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"Message": "The movie does not has been found"})
    MovieServices(db).update_movie(id, movie)
    return JSONResponse(status_code=200,content={"message" : "The movie has been modified"})

@movie_router.delete("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def delete_route(id: int) -> dict:
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"Message": "The movie does not has been found"})
    MovieServices(db).delete_movie(id)
    return JSONResponse(status_code=200,content={"message" : "The movie has been eliminated"})
