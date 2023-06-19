from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import NewUser, PrivateMusicRecord, PublicMusicRecord, ProtectedMusicRecord
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == 'POST':
        email_id = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email_id, password=password)
        if user is not None and hasattr(user, 'newuser'):
            login(request, user)
            user_id = user.id
            return redirect('MelodyShare:main', user_id=user_id)
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_id = request.POST.get('email_id')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})

        # Get the last used ID
        last_used_id = NewUser.objects.last()
        if last_used_id:
            last_id_number = int(last_used_id.id)
            new_id_number = last_id_number + 1
        else:
            new_id_number = 1000

        # Create user instance
        user = User.objects.create_user(username=email_id, password=password1)
        user.save()

        # Create NewUser instance with the generated ID
        new_user = NewUser(user=user, id=new_id_number, email_id=email_id, name=name)
        new_user.save()

        return redirect('MelodyShare:login')
    else:
        return render(request, 'signup.html')



@login_required
def main(request, user_id):
    private_records = PrivateMusicRecord.objects.filter(user_id=user_id)
    public_records = PublicMusicRecord.objects.all()

    user = User.objects.get(id=user_id)
    user_email = user.email

    if user_email:
        protected_records = ProtectedMusicRecord.objects.filter(email_ids__contains=[user_email])
    else:
        protected_records = ProtectedMusicRecord.objects.all()

    context = {
        'private_records': private_records,
        'public_records': public_records,
        'protected_records': protected_records,
        'user_id': user_id
    }

    return render(request, 'main.html', context)



@login_required
def upload(request, user_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        record_type = request.POST.get('record_type')
        media_file = request.FILES.get('media_file')

        if record_type == 'private':
            record = PrivateMusicRecord(name=name, description=description, media_file=media_file, user_id=user_id)
        elif record_type == 'public':
            record = PublicMusicRecord(name=name, description=description, media_file=media_file)
        elif record_type == 'protected':
            email_ids = [email.strip() for email in request.POST.get('email_ids').split(',') if email.strip()]
            allowed_emails = []
            for email in email_ids:
                try:
                    NewUser.objects.get(email_id=email)
                    allowed_emails.append(email)
                except ObjectDoesNotExist:
                    pass
            record = ProtectedMusicRecord(name=name, description=description, email_ids=allowed_emails, media_file=media_file)
        else:
            return render(request, 'upload.html', {'error': 'Invalid record type.'})

        record.save()
        return redirect('MelodyShare:main', user_id=request.user.id)
    else:
        return render(request, 'upload.html')
