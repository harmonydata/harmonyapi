from harmony.schemas.requests.text import MatchBody
from harmony_api import http_exceptions, helpers, constants


def model_from_match_body_is_available(match_body: MatchBody) -> bool:
    """
    Check model availability.
    """

    model = match_body.parameters
    __check_model(model.dict())

    return True


def __check_model(model_dict: dict):
    if model_dict not in constants.ALL_HARMONY_API_MODELS:
        raise http_exceptions.CouldNotProcessRequestHTTPException(
            "Could not process request because the model does not exist."
        )
    if not helpers.check_model_availability(model_dict):
        raise http_exceptions.CouldNotProcessRequestHTTPException(
            "Could not process request because the model is not available."
        )
