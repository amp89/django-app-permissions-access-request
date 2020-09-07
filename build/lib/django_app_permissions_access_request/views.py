from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django_app_permissions.views import APIAppAuthView
from django_app_permissions.views import AppAuthView
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, Group
from django_app_permissions_access_request.models import Request
# Create your views here.
class RequestListView(LoginRequiredMixin, View):
    def get(self,request, *args, **kwargs):
        apps = settings.ACCESS_CONTROLLED_INSTALLED_APPS
        groups = Group.objects.filter(name__in=apps)
        group_list = []
        for group in groups:            
            if request.user.groups.filter(name=group.name).exists():
                access_status = "You have access"
            elif Request.objects.filter(user=request.user, group=group).exists():
                access_status="Access pending"
            else:
                access_status = False
                
            group_list.append({
                "id":group.id,
                "name":group.name.replace("_"," ").replace("-"," ").title(),
                "access":access_status,
            })
        # TODO: find a better solutin for user_is_admin
        return render(request, "app_permissions_access_request_list.html", {"group_list":group_list,"site_home":reverse(settings.SITE_HOME_URL_NAME),"user_is_admin":request.user.groups.filter(name="django_app_permissions_access_request").exists()})

class RequestView(LoginRequiredMixin, View):
    def get(self,request, *args, **kwargs):
        group_id = request.GET["group_id"]
        group = Group.objects.get(id=group_id)
        return render(request, "app_permissions_access_request.html", {"group":group,"site_home":reverse(settings.SITE_HOME_URL_NAME),"user_is_admin":request.user.groups.filter(name="django_app_permissions_access_request").exists()})

    def post(self,request, *args, **kwargs):
        group_id = request.GET["group_id"]
        description = request.POST.get("description","")
        if Request.objects.filter(user=request.user, group=Group.objects.get(id=group_id)).exists():
            messages.add_message(request, messages.ERROR, "You already have an open request for this app.")
            return redirect(reverse(settings.SITE_HOME_URL_NAME))
        try:
            Request.objects.create(user=request.user, group=Group.objects.get(id=group_id),description=description)
            messages.add_message(request, messages.SUCCESS, 'Request Submitted!')
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, 'Failed to Request. Please try again later.')
        
        if hasattr(settings,"REDIRECT_ACCESS_REQUEST_HOME") and settings.REDIRECT_ACCESS_REQUEST_HOME == True:
            return redirect(reverse(settings.SITE_HOME_URL_NAME))
        else:
            return redirect(reverse('django_app_permissions_access_request.request_list'))

class ApprovalsView(AppAuthView):
    def get(self,request, *args, **kwargs):
        all_requests = Request.objects.all()
        return render(request, "app_permissions_access_approval_list.html", {"requests":all_requests,"site_home":reverse(settings.SITE_HOME_URL_NAME),"user_is_admin":request.user.groups.filter(name="django_app_permissions_access_request").exists()})

class ApprovalView(AppAuthView):
    def get(self,request, *args, **kwargs):
        request_id = request.GET["request_id"]
        request_obj = Request.objects.get(id=request_id)
        return render(request, "app_permissions_access_approval.html", {"request_obj":request_obj,"site_home":reverse(settings.SITE_HOME_URL_NAME),"user_is_admin":request.user.groups.filter(name="django_app_permissions_access_request").exists()})

    def post(self,request, *args, **kwargs):
        request_id = request.GET["request_id"]
        # add user to group delete req and do stuff
        try:
            request_obj = Request.objects.get(id=request_id)
            request_obj.user.groups.add(request_obj.group)
            request_obj.delete()
            messages.add_message(request, messages.SUCCESS, 'User added to group.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Failed to add user to group - please try again')

        return redirect(reverse("django_app_permissions_access_request.approvals"))

class DenyView(AppAuthView):

    def post(self,request, *args, **kwargs):
        request_id = request.GET["request_id"]
        # reject user to group delete req and do stuff
        try:
            Request.objects.get(id=request_id).delete()
            messages.add_message(request, messages.SUCCESS, 'Request rejected')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Failed to reject request - please try again')
        
        return redirect(reverse("django_app_permissions_access_request.approvals"))


