from fastapi import APIRouter, Depends, Request
from blog.core.api_dependencies import Dependencies
from blog.user.domain.user_schema import UserDto
from blog.user.application.user import UserIntegration


router = APIRouter()


def user_injected_dependecy(request: Request):
    dependencies: Dependencies = request.app.state.dep
    user_integration = UserIntegration(dependencies.user_repo)
    return user_integration


@router.post("/")
async def user_signup(user_data: UserDto,
                      test=Depends(user_injected_dependecy)):
    user_result = await test.create_an_user(user_data)
    return user_result
