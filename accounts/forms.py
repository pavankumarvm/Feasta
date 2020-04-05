from django.contrib.auth.forms import UserChangeForm,UserCreationForm

from django.db import transaction
from .models import FeastaUser,MessOwner,Consumer

class FeastaUserSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = FeastaUser
        fields = UserCreationForm.Meta.fields

class MessOwnerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = FeastaUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_no', )

    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_messowner = True
        messowner = MessOwner.objects.create(user= user)
        user.save()
        return user


class ConsumerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = FeastaUser
        fields = UserCreationForm.Meta.fields

    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_consumer = True
        consumer = Consumer.objects.create(user= user)
        user.save()
        return user


class UserDetailsForm(UserChangeForm):

    class Meta:
        model = FeastaUser
        fields = UserChangeForm.Meta.fields