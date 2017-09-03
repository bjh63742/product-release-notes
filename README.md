# product-release-notes

[![Build Status](https://travis-ci.org/nickromano/product-release-notes.svg?branch=master)](https://travis-ci.org/nickromano/product-release-notes)
[![Coverage Status](https://coveralls.io/repos/github/nickromano/product-release-notes/badge.svg?branch=master)](https://coveralls.io/github/nickromano/product-release-notes?branch=master)
[![PyPi](https://img.shields.io/pypi/v/product_release_notes.svg)](https://pypi.python.org/pypi/product-release-notes)

## Installation

1) Install the python package

```
pip install product_release_notes
```

2) Add `product_release_notes` to `INSTALLED_APPS` in your `settings.py`.

3) Add a url to your `urls.py`.

```python
# project.urls.py
from django.conf.urls import url, include

urlpatterns = [
    url(r'^release-notes/', include('product_release_notes.urls')),
]
```

4) Run migrations to create the release notes tables.

```
./manage.py migrate
```

## Settings

Optional settings to customize the release notes page.

```
RELEASE_NOTES_PAGE_DESCRIPTION = 'My product updates.'
```

5) Optional - Create release note drafts when new versions are released to iTunes

Fill in the `itunes_url` field when creating a client.

Add a scheduled job to run at least daily to check for new versions in iTunes

```
./manage.py check_app_stores
```

6) Optional - Customize the release notes page

Create a template `release_notes/base.html` to override the packages base template.

```
<!DOCTYPE html>
<html>
<head>
	<title>Release Notes</title>

	{% block release_notes_extra_head %}{% endblock %}
</head>
<body>

{% block release_notes_body_header %}{% endblock %}
{% block release_notes_body %}{% endblock %}

</body>
</html>
```
