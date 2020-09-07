# Django App Permissions Access Request

UI for handling app permissions defined in the Django App Permissions package (https://github.com/amp89/django-app-permissions)

## Install
`pip install --upgrade django-app-permissions-access-request`

## Configure
`settings.py`
1. Must have `Django App Permissions` installed and setup
2. In `ACCESS_CONTROLLED_INSTALLED_APPS`, add `django_app_permissions_access_request`.  __IT MUST GO IN `ACCESS CONTROLLED` INSTALLED APPS, OR ANYONE WILL BE ABLE TO CHANGE THEIR OWN PERMISSIONS!
3. `SITE_HOME_URL_NAME`  This should be the __name__ of the url that is the home/ root site.
4. [RECOMMENDED] `REDIRECT_ACCESS_REQUEST_HOME = True` - this will redirect the user back to the `SITE_HOME_URL_NAME` page instead of the access request list, after submitting the access request form.
5. [RECOMMENDED] Add to `settings.py`: `REDIRECT_403_URL='django_app_permissions_access_request.request_access'` to direct the user to the request form
6. Add to base URLS: `path('access_request/', include('django_app_permissions_access_request.urls')),`
