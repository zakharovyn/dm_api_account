from dm_api_account.models.user_details_envelope_model import UserDetailsEnvelope
from dm_api_account.models.change_password_model import ChangePassword
from dm_api_account.models.reset_password_model import ResetPassword
from dm_api_account.models.user_envelope_model import UserEnvelope
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.change_email_model import ChangeEmail
from dm_api_account.utilites import validate_request_json, validate_status_code
from restclient.restclient import Restclient
from requests import Response
import allure


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)
        # self.client.session.headers.update(headers) if headers else None

    def post_v1_account(
            self,
            json: Registration,
            status_code: int = 201,
            **kwargs
    ) -> Response:
        """
        Register new user

        :param status_code: статус код ответа сервера
        :param json Registration
        :return:
        """
        with allure.step(f'POST {self.host}/v1/account'):
            response = self.client.post(
                path=f"/v1/account",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)

        return response

    def get_v1_account(
            self,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserDetailsEnvelope:
        """
        Get current user

        :return:
        """
        with allure.step(f'GET {self.host}/v1/account'):
            response = self.client.get(
                path=f"/v1/account",
                **kwargs
            )
        validate_status_code(response, status_code)

        if response.status_code == 200:
            return UserDetailsEnvelope(**response.json())

        return response

    def put_v1_account_token(
            self,
            token: str,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Activate registered user

        :return:
        """
        with allure.step(f'PUT {self.host}/v1/account/{token}'):
            response = self.client.put(
                path=f"/v1/account/{token}",
                **kwargs
            )
        validate_status_code(response, status_code)

        if response.status_code == 200:
            return UserEnvelope(**response.json())

        return response

    def post_v1_account_password(
            self,
            json: ResetPassword,
            status_code: int = 201,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Reset registered user password

        :return:
        """
        with allure.step(f'POST {self.host}/v1/account/password'):
            response = self.client.post(
                path=f"/v1/account/password",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)

        if response.status_code == 201:
            return UserEnvelope(**response.json())

        return response

    def put_v1_account_password(
            self,
            json: ChangePassword,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Change registered user password

        :return:
        """
        with allure.step(f'PUT {self.host}/v1/account/password'):
            response = self.client.put(
                path=f"/v1/account/password",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)

        if response.status_code == 200:
            return UserEnvelope(**response.json())

        return response

    def put_v1_account_email(
            self,
            json: ChangeEmail,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        Change registered user email

        :return:
        """
        with allure.step(f'PUT {self.host}/v1/account/email'):
            response = self.client.put(
                path=f"/v1/account/email",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)

        if response.status_code == 200:
            return UserEnvelope(**response.json())

        return response
