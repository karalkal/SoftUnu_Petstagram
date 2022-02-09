from django.shortcuts import render

from SoftUni_Petstagram.main_app.models import Profile, PetPhoto


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


# Create your views here.
def home(request):
    context = {'hide_additional_menu_items': True}
    return render(request, 'home_page.html', context)


def dashboard(request):
    # check pets for specific user, in our case first one
    profile = get_profile()
    # owners_pets = profile.pet_set.all()
    owners_pets_photos = set(PetPhoto.objects.filter(tagged_pets__owner=profile))
    context = {"owners_pets_photos": owners_pets_photos}
    return render(request, 'dashboard.html', context)


def profile(request):
    return render(request, 'profile_details.html')


def photo_details(request, pk):
    searched_photo = PetPhoto.objects.get(pk=pk)
    context = {"searched_photo": searched_photo}
    return render(request, 'photo_details.html', context)