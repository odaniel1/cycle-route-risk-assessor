"""
Strava API client module.
Provides StravaService to fetch route geometry from Strava.
"""

from typing import List, Tuple
from stravalib.client import Client

from libs.config import Settings


class StravaService:
    """
    Service for interacting with the Strava API.

    Attributes:
        client (Client): Authenticated Strava client.
    """

    def __init__(self, access_token: str = None):
        """
        Initialize the StravaService.

        Args:
            access_token (str, optional): OAuth access token for Strava API.
                If not provided, will be read from STRAVA_ACCESS_TOKEN env var
                via Settings.
        """
        settings = Settings()
        self.access_token = access_token or settings.strava_access_token
        self.client = Client(access_token=self.access_token)

    def get_route(self, route_id: int) -> List[Tuple[float, float]]:
        """
        Fetch a route from Strava and return its geometry as a list
        of (lat, lon).

        Args:
            route_id (int): The ID of the Strava route.

        Returns:
            List[Tuple[float, float]]: Sequence of latitude/longitude pairs.

        Raises:
            NotImplementedError: Method not yet implemented.
        """
        raise NotImplementedError("StravaService.get_route not implemented")
