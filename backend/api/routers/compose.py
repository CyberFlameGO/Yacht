from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..actions.compose import (
    get_compose_projects,
    compose_action,
    compose_app_action,
    get_compose,
)
from fastapi_jwt_auth import AuthJWT
from ..auth import auth_check

router = APIRouter()


@router.get("/")
def get_projects(Authorize: AuthJWT = Depends()):
    auth_check(Authorize)
    return get_compose_projects()


@router.get("/{project_name}")
def get_project(project_name, Authorize: AuthJWT = Depends()):
    auth_check(Authorize)
    return get_compose(project_name)


@router.get("/{project_name}/{action}")
def get_compose_action(project_name, action, Authorize: AuthJWT = Depends()):
    auth_check(Authorize)
    return compose_action(project_name, action)


@router.get("/{project_name}/{action}/{app}")
def get_compose_app_action(project_name, action, app, Authorize: AuthJWT = Depends()):
    auth_check(Authorize)
    return compose_app_action(project_name, action, app)
