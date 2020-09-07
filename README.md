# Django App Permissions Access Request

UI for handling app permissions defined in the Django App Permissions package (https://github.com/amp89/django-app-permissions)

## Install
`pip install --upgrade django-app-permissions-access-request`

## Configure
`settings.py`
1. Must have `Django App Permissions` installed and setup
2. In `ACCESS_CONTROLLED_INSTALLED_APPS`, add `django_app_permissions_access_request`.  __IT MUST GO IN `ACCESS CONTROLLED` INSTALLED APPS, OR ANYONE WILL BE ABLE TO CHANGE THEIR OWN PERMISSIONS!
3. `SITE_HOME_URL_NAME`  This should be the __name__ of the url that is the home/ root site.
4. [RECOMMENDED] in `settings.py`: `REDIRECT_ACCESS_REQUEST_HOME = True` - this will redirect the user back to the `SITE_HOME_URL_NAME` page instead of the access request list, after submitting the access request form.
5. [RECOMMENDED] in `settings.py`: `REDIRECT_403_URL='django_app_permissions_access_request.request_access'` to direct the user to the request form
6. Add to base URLS: `path('access_request/', include('django_app_permissions_access_request.urls')),`

## Use:

The new urls are now:

`access_request/approvals/` (`name='django_app_permissions_access_request.approvals'`)  You must be a part of this app on the backend (in the `django_app_permissions_access_request` group) or a superuser with `ALLOW_ALL_SUPERUSER = True` to see this page.  This is where user requests are approved / denied.

`access_request/` (`name='django_app_permissions_access_request.request_list'`) A list of apps that the user can request

`access_request/request/?group_id` (`name='django_app_permissions_access_request.request_access'`) These are linked to in the above page, and if `REDIRECT_403_URL='django_app_permissions_access_request.request_access'` is set in settings, the user will be directed to the request page if they try to visit an app that they are not a part of.
