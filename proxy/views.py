from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote


def proxy(request, url):
    """
    Proxy view for handling external URLs. It retrieves the content of the
    specified URL, modifies the HTML by adding proxy information to links
    and forms, and returns the modified content.

    Args:
        request (HttpRequest): The Django HttpRequest object.
        url (str): The URL to proxy.

    Returns:
        HttpResponse: The HTTP response containing the modified HTML content.
    """
    try:
        # Extract the start_url parameter from the request's query parameters
        start_url = request.GET.get("start_url", "")

        full_url = urljoin(start_url, url)

        soup = BeautifulSoup(requests.get(full_url).content, "html.parser")

        # Modify HTML content by adding proxy information to links
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if href and not href.startswith(("http:", "https:")):
                target_url = urljoin(start_url, href)
                a_tag[
                    "href"
                ] = f"/proxy/{quote(target_url)}?start_url={quote(full_url)}"

        # Modify HTML content by adding proxy information to form actions
        for form_tag in soup.find_all("form", action=True):
            action = form_tag["action"]
            if action and not action.startswith(("http:", "https:")):
                target_url = urljoin(start_url, action)
                form_tag[
                    "action"
                ] = f"/proxy/{quote(target_url)}?start_url={quote(full_url)}"

        content = str(soup)
    except requests.RequestException as e:
        content = str(e)
        return HttpResponse(content, status=500, content_type="text/plain")

    return HttpResponse(content, content_type="text/html")
