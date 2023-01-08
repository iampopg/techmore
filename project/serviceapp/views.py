
from django.shortcuts import render, get_object_or_404
from .forms import messageForm, uploadForm, statusForm, decideForm, bugForm
from .models import message, uploadIdea, bugsModel
from django.shortcuts import redirect
from django.urls import reverse

from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from project.userapp import Profile

# Create your views here.

def messageView(request):

    # messagess= messageForm(request.POST)
    if request.method == "POST":
        # global messagess
        messagess= messageForm(request.POST)
        if messagess.is_valid():
            me = messagess.save()
            first_name = me.first_name
            last_name = me.first_name
            email = me.email
            messageToPass = me.messages
            toEmail = "techmoredev@gmail.com"
    
            send_mail(
                "MORE",
                f"""{first_name} {last_name} sent this message ({messageToPass})""",
                'techmoredev@gmail.com', #from emal (sender)
                (toEmail,), #to email
                fail_silently=False,)

            
            send_mail(
                "TECHMORE",
                f"""dear {first_name},Your message has being received, your will get a responce from us within 24hrs, Thanks for your time.
                You can also call us at +2348135729554""",
                'techmoredev@gmail.com', #from emal (sender)
                (email,), #to email
                fail_silently=False,)
            messages.success(request, ("Your message had being sent succefully."))
            return redirect('massage')
        else:
            messages.error(request, ('Unfortunately, Your message was unable to send'))
            return render(request, 'serviceapp/message.html',{'message':messagess})
    else:
        messagess = messageForm()
        return render(request, 'serviceapp/message.html',{'message':messagess})

@login_required
def uploadD(request, _id):
    if request.method == 'POST':
        update = User.objects.all().filter(id = _id).get()
        file = uploadForm(request.POST, request.FILES)
        if file.is_valid():
            upload = file.save(commit=False)
            import random
            code= random.randint(000000,999999)
            upload.pincode = code
            upload.user_id = _id
            pincode = upload.pincode
            # upload.status = 
            upload.save()
            email = upload.email
            file = upload.fileToUpload

            
            name1 = update.first_name
            name2 = update.last_name
            send_mail("TECHMORE FILE SUBMISSION", f'this file {file}, was recieved from {name1} {name2}', 'techmoredev@gmail.com', ['techmoredev@gmail.com'], fail_silently=False,)
            messages.success(request, ('Your Idea Frame File is sent succefully, Click on "HOME" then CHECK STATUS to check your status '))
            
            send_mail("TECHMORE FILE SUBMISSION", f'we have recieved your file, we will get back to you very soon and let you know if you are being approved. To check your submission status you need your email and this "pincode" {pincode} You can be checking your Status here.', 'techmoredev@gmail.com', [email], fail_silently=False,)
            messages.success(request, ('Your Idea Frame File is sent succefully'))
            return HttpResponseRedirect(reverse( 'upload', args=_id))
        # else:
        #     messages.error(request, ('There was an error, Please Try again'))
        #     return HttpResponsePermanentRedirect(reverse('upload', args=(_id)))
    else:
        file = uploadForm()
        return render(request,'serviceapp/upload.html',{'file': file})

@login_required
def checkStatus(request, _id):
    if request.method == "POST":
        email=uploadIdea.objects.all().filter(user_id = _id)
        # pincode=uploadIdea.objects.only('pincode').filter(user_id = _id)
        status = statusForm(request.POST)
        status.save(commit=False)
        if status in email:
            # return redirect("home") 
            return HttpResponseRedirect(reverse( 'upload', args=_id))
        else:
            messages.error(request, ("Wr couldnt find any Data match with what you inputed, Try again"))
            return HttpResponseRedirect(reverse( 'status', args=_id)) 
    else:
        status = uploadIdea.objects.all().filter(user_id = _id)
        statu = statusForm()
        return render(request,'serviceapp/status.html',{'status': status, 'statu':statu})

@login_required
def decideView(request, _id):
    if request.method == "POST":
        status = uploadIdea.objects.only('status').filter(id = _id).get()
        decide = decideForm(request.POST or None, instance=status)
        if decide.is_valid():
            decide.save(commit=False)
            if decide.cleaned_data['status']:
                uploadIdea.objects.only('status').filter(id = _id).update(status=True)
                decide.save()

                
                stat = uploadIdea.objects.all().filter(id = _id).get()
                email = stat.email
                pincode = stat.pincode
                send_mail("TECHMORE FILE APPROVAL", f'Your File with pincode "{pincode}" has being Approved. login for more details', 'techmoredev@gmail.com', [email,], fail_silently=False,)
                messages.success(request, ('You have successfully Approved this IDEA'))
                # messages.success(request, ('You have successfully Decline this IDEA'))
                return redirect('index')
                
            else:
                uploadIdea.objects.only('status').filter(id = _id).update(status=False)
                
                # decide.status = False
                decide.save()

                stat = uploadIdea.objects.all().filter(id = _id).get()
                email = stat.email
                pincode = stat.pincode
                send_mail("TECHMORE FILE Decline", f'Your File with pincode "{pincode}" has being Decline. login for more details', 'techmoredev@gmail.com', [email,], fail_silently=False,)
                messages.success(request, ('You have successfully Decline this IDEA'))
                # return decideView(request, _id)
                return redirect('index')

        else:
            # decide.status = False
            
            messages.error(request, ("An error occur, please try again"))
            return HttpResponseRedirect(reverse('decide', args= (_id))) 
    else:
        status = uploadIdea.objects.all().filter(id = _id).get()      
        decide = decideForm(instance=status)
        return render(request, 'serviceapp/decide.html', {'decide':decide})

@login_required
def statusAdmin(request):
    status = uploadIdea.objects.all()
    statu = statusForm()
    return render(request, 'serviceapp/status.html', {'status':status, 'statu':statu})


def bugView(request):
    if request.method == 'POST':
        bug = bugForm(request.POST)
        if bug.is_valid():
            # bug.save()

            buga = bug.save()
            name =buga.bug_name
            type= buga.bug_type
            email = buga.email
            description = buga.description
            messages.success(request, ('Your bug issue has being sent successfully, You will get an email within 24hrs when it being solved'))

            #company
            send_mail("TECHMORE BUGS BUGS", f'''A bug issue was submited now.The bug is about{type} and main is {name} and the description is "{description}"
            Thanks''', 'techmoredev@gmail.com', ['techmoredev@gmail.com',], fail_silently=False,)

            #customer
            send_mail("TECHMORE BUGS", f'''We have received your "{type}" bug issue, Please wait for the next 24hrs to be solved. We will contact you again if needed.
            Thanks''', 'techmoredev@gmail.com', [email,], fail_silently=False,)
            return redirect('bug')
        else:
            messages.error(request, ('There was an error with your input, Please Try again'))
            return redirect('bug')
    else:
        bug= bugForm()
        return render(request, 'serviceapp/bugs.html', {'bug':bug})