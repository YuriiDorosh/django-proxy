# Django Proxy

## Overview

A Django project that provides a proxy view for handling external URL addresses. This view allows fetching content from a specified URL, modifying the HTML by adding proxy information to links and forms, and returning the modified content.

## Features

- **Proxy for External Resources:** Enables fetching content from external URL addresses and adds proxy information to links and forms.
- **HTML Modification:** The view uses BeautifulSoup to modify HTML code and add proxy information to the content.
- **Link and Form Handling:** Provides a proxy for links and forms on the page to avoid issues with link schemes.

## Usage

1. **Install Dependencies:** Before using the project, install the necessary dependencies using the command `pip install -r requirements.txt`.

2. **Run the Server:** Start the Django server with the command 
```bash
make setup
```

to run the project use command
```bash
make run
```

3. **Use the Proxy:** To use the proxy, access the `/proxy/` view and pass the URL you want to proxy as a parameter.

   Example call: `http://localhost:8000/proxy/https://github.com/YuriiDorosh/`

## Important Notes

- **Security:** Be mindful of the potential for proxy abuse and adhere to best security practices.
- **Usage Limits:** This project is intended for proxying web resources and may not be suitable for all use cases.

## License

This project is distributed under the [MIT License](LICENSE). Read more about the license terms in the `LICENSE` file.


## Support

If you have questions or issues, please contact the project author via [GitHub Issues](https://github.com/YuriiDorosh/django-proxy/issues).

---

