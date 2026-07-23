"""Adapter for the endoflife.date API.

This module provides client access to the endoflife.date API, which tracks
end-of-life dates for software products, programming languages, and frameworks.
"""

from typing import Any

import requests


class EndOfLifeAdapter:
    """Client for the endoflife.date API.

    Provides methods to query products, categories, tags, and identifiers
    from the endoflife.date service.
    """

    def __init__(self, version: str = "v1") -> None:
        """Initialize the adapter with the specified API version.

        Parameters
        ----------
        version : str, optional
            API version string (default: "v1")
        """
        self.base_url = f"https://endoflife.date/api/{version}"
        self._headers = {
            "accept": "application/json",
        }

    def _url(self, path: str) -> str:
        """Construct the full URL for an API endpoint.

        Parameters
        ----------
        path : str
            The API endpoint path

        Returns
        -------
        str
            Full URL for the endpoint
        """
        return f"{self.base_url}/{path.lstrip('/')}"

    def _get(self, path: str, **kwargs: Any) -> requests.Response:
        """Make a GET request to the API.

        Parameters
        ----------
        path : str
            The API endpoint path
        **kwargs : dict
            Additional arguments to pass to requests.get()

        Returns
        -------
        requests.Response
            Response object from requests.get()
        """
        return requests.get(self._url(path), headers=self._headers, **kwargs)

    def index(self) -> dict:
        """Retrieve API index information.

        Returns
        -------
        dict
            Dictionary containing API metadata and available endpoints
        """
        response = self._get("")
        response.raise_for_status()
        return response.json()

    def get_products(self, full: bool = False) -> dict:
        """Retrieve list of available products.

        Parameters
        ----------
        full : bool, optional
            If True, include full product details (default: False)

        Returns
        -------
        dict
            Dictionary containing product list
        """
        path = "products/"
        if full:
            path += "full"
        response = self._get(path)
        response.raise_for_status()
        return response.json()

    def get_product(self, product_name: str, release: str | None = None) -> dict:
        """Retrieve information for a specific product.

        Parameters
        ----------
        product_name : str
            Name of the product to query
        release : str, optional
            Specific release version to query

        Returns
        -------
        dict
            Dictionary containing product information and release details
        """
        is_single_release = release is not None
        path = f"products/{product_name.lower()}"
        if is_single_release:
            path += f"/releases/{release}"

        response = self._get(path)
        response.raise_for_status()
        product = response.json()
        product["has_single_release"] = is_single_release

        return product

    def get_categories(self) -> dict:
        """Retrieve list of available product categories.

        Returns
        -------
        dict
            Dictionary containing category list
        """
        path = "categories"
        response = self._get(path)
        response.raise_for_status()
        return response.json()

    def get_category(self, category_name: str) -> dict:
        """Retrieve products in a specific category.

        Parameters
        ----------
        category_name : str
            Name of the category to query

        Returns
        -------
        dict
            Dictionary containing products in the category
        """
        path = f"categories/{category_name.lower()}"
        response = self._get(path)
        response.raise_for_status()
        return response.json()

    def get_tags(self) -> dict:
        """Retrieve list of available tags.

        Returns
        -------
        dict
            Dictionary containing tag list
        """
        path = "tags"
        response = self._get(path)
        response.raise_for_status()
        return response.json()

    def get_tag(self, tag_name: str) -> dict:
        """Retrieve products with a specific tag.

        Parameters
        ----------
        tag_name : str
            Name of the tag to query

        Returns
        -------
        dict
            Dictionary containing products with the tag
        """
        path = f"tags/{tag_name.lower()}"
        response = self._get(path)
        response.raise_for_status()
        return response.json()

    def get_identifiers(self) -> dict:
        """Retrieve list of available identifiers.

        Returns
        -------
        dict
            Dictionary containing identifier list
        """
        path = "identifiers"
        response = self._get(path)
        response.raise_for_status()
        return response.json()

    def get_identifier(self, identifier_type: str) -> dict:
        """Retrieve details for a specific identifier type.

        Parameters
        ----------
        identifier_type : str
            The identifier type to query

        Returns
        -------
        dict
            Dictionary containing identifier information
        """
        path = f"identifiers/{identifier_type.lower()}"
        response = self._get(path)
        response.raise_for_status()
        return response.json()
