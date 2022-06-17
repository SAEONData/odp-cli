import os
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests
from authlib.integrations.base_client.errors import OAuthError
from authlib.integrations.requests_client import OAuth2Session
from dotenv import load_dotenv


@dataclass
class ODPResponse:
    status: int
    content: Optional[Dict] = None
    error: Any = None


class ODPClient:
    def __init__(self):
        load_dotenv()
        self.api_url = os.environ['ODP_API_URL']
        self.token = OAuth2Session(
            client_id=os.environ['ODP_CLIENT_ID'],
            client_secret=os.environ['ODP_CLIENT_SECRET'],
            scope=os.environ['ODP_CLIENT_SCOPE'],
        ).fetch_token(
            url=os.environ['ODP_TOKEN_URL'],
            grant_type='client_credentials',
            timeout=10.0,
        )

    def get(self, path, **params):
        return self._request('GET', path, None, params)

    def post(self, path, data, **params):
        return self._request('POST', path, data, params)

    def put(self, path, data, **params):
        return self._request('PUT', path, data, params)

    def delete(self, path, **params):
        return self._request('DELETE', path, None, params)

    def _request(self, method, path, data, params):
        try:
            r = requests.request(
                method=method,
                url=self.api_url + path,
                json=data,
                params=params,
                headers={
                    'Accept': 'application/json',
                    'Authorization': 'Bearer ' + self.token['access_token'],
                }
            )
            r.raise_for_status()

            return ODPResponse(
                status=r.status_code,
                content=r.json(),
            )

        except requests.RequestException as e:
            if e.response is not None:
                status = e.response.status_code
                try:
                    error = e.response.json()
                except ValueError:
                    error = e.response.text
            else:
                status = 503
                error = str(e)

            return ODPResponse(
                status=status,
                error=error,
            )

        except OAuthError as e:
            return ODPResponse(
                status=401,
                error=str(e),
            )
