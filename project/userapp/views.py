from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect 
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .form import SignUpForm, profileForm, User_form
from .models import Profile
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('send_mail')
    template_name = 'registration/register.html'

    # if SignUpForm.uniqueError:

    #     email = User.objects.create(email=email_input)
    #     send_mail(
    #             "EXISTING CUSTOMER",
    #             """Dear Valid user, You try to create a new account with this email, please try again later """,
    #            
    #             [email], #to email
    #             fail_silently=False,)
    # else:
    #     pass

def sendWElcomEmail(request):
    pro = Profile.objects.all().filter(staff=False)
    for x in pro:
        email1 = x.user.email
        # Profile = request.myProfile()
        #send mail to the patient
        send_mail(
                "WELCOME TO TECHMORE",
                """Dear patient, Your account has being succefull Created, please Procced to your
                profile to Update it """,
                'techmoredev@gmail.com', #from emal (sender)
                [email1], #to email
                fail_silently=False,)
        return redirect('login')

@login_required
def profileView(request, _id):
    profile = Profile.objects.all().filter(user_id = _id)
    for x in profile:
        global email1
        email1 = x.user.email
    return render(request, "userapp/profile.html", {"profile": profile})

@login_required
def updateProfile(request, id):
    if request.method == "POST":
        user = get_object_or_404(User, id = id)
        user_form = User_form(request.POST, instance=user)
        profile_form = profileForm(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()
            email = user_form.cleaned_data["email"]
            if profile_form.cleaned_data['staff']:
                user.is_staff = True
                user_form.save()

            else:
                user.is_staff = False
                user_form.save()
            messages.success(request, ('Your Profile has being successfully Updated'))
            send_mail(
             "Welcome To TECHMORE", #subject
                # 'a custormer with the id:'+str(staff_id)+"just made an order \n Check "
                f"""Your Profile has been successfully updated
                
                    contact us if you're unaware on this action 
                    techmoredev@gmail.com

                    NB:This is for a testing.""",
                'techmoredev@gmail.com', #from emal (sender)
                [email], #to email
                fail_silently=False,
            )
            return profileView(request, id)
        else:
            messages.error(request, ("There is an Error With Your Profile, please contact us Immidiatly"))
            return HttpResponsePermanentRedirect(reverse("update_profile", args=(id,)))
    else:
        user = get_object_or_404(User, id=id )
        user_form = User_form(instance=user)
        profile_form = profileForm(instance=user.profile)
        messages.error(request, ("An error Occur While updating your Profile"))
        return render(request, 'userapp/update_profile.html', {
        'user_form': user_form, 
        'profile_form': profile_form })
    
@login_required
def deactivateProfile(request, _id):
    user_profile = User.objects.only("is_active").filter(id= _id)

    if user_profile.values()[0].get('is_active') == True:
        User.objects.only('is_active').filter(id=_id).update(is_active=False)
    elif user_profile.values()[0].get('is_active') == False:
        User.objects.only('is_active').filter(id=_id).update(is_active=True)
    else:
        User.objects.only('is_active').filter(id=_id).update(is_active=True)
    return profileView(request, _id)

@login_required
def displayStaff(request):
    staff = Profile.objects.all().filter(staff = True)
    return render(request, 'userapp/display.html', {'staff':staff})

@login_required
def displayCustomer(request):
    staff = Profile.objects.all().filter(staff = False)
    return render(request, 'userapp/display.html', {'staff':staff})
