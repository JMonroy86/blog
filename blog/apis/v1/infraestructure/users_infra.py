from fastapi import FastAPI, APIRouter, Depends, Request, HTTPException, status, Query
from fastapi.responses import JSONResponse
from blog.core.api_dependencies import Dependencies
from blog.user.domain.user_schema import UserDto
from blog.user.application.user import UserApplication


router = APIRouter()


class CustomException(HTTPException):
  def __init__(self, det: str, stat_code: int):
    self.detail = det,
    self.status_code = stat_code


def user_injected_dependecy(request: Request):
  dependencies: Dependencies = request.app.state.dep
  user_integration = UserApplication(dependencies.user_repo)
  return user_integration


@router.post("/")
async def user_signup(user_data: UserDto,
                      user=Depends(user_injected_dependecy)):
  try:
    user_result = await user.create_an_user(user_data)
    return user_result
  except Exception as e:
    raise CustomException(stat_code=status.HTTP_404_NOT_FOUND, det=str(e))


@router.get("/")
async def get_user(email: str = Query(...), user=Depends(user_injected_dependecy)):
  try:
    print(email, "en emai")
    user_result = await user.get_user_by_email(email)
  except Exception as e:
    raise CustomException(stat_code=404, det=str(e))
  
  return user_result
