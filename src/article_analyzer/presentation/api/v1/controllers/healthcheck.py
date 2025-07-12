from fastapi import APIRouter, status
from pydantic import BaseModel

class HealthCheckSchema(BaseModel):
    healthy: bool = True


healthcheck_router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"]
)


healthcheck_schema = HealthCheckSchema()


@healthcheck_router.get(
    "",
    response_model=HealthCheckSchema,
    status_code=status.HTTP_200_OK,
    response_description='Health resource',
    description='Retrieves a health status of the application',
    summary='Retrieves a health status of the application'
    )
async def healthcheck() -> HealthCheckSchema:
    return healthcheck_schema
