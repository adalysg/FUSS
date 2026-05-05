import pytest

# Create your tests here.
from users.models import *

@pytest.mark.django_db
def test_custom_user_creation():

    user = CustomUser.objects.create_user(
        email = 'unittest01@gmail.com',
        username = 'unit',
        password = 'abc123'
    )

    assert user.email == 'unittest01@gmail.com'
    assert user.username == 'unit'
    assert user.check_password('abc123')

@pytest.mark.django_db
def test_custom_user_creation_no_username():
    """
    Tests that when no username is provided, the username is defaulted to the email address.
    """

    user = CustomUser.objects.create_user(
        email = 'unittest01@gmail.com',
        password = 'abc123'
    )

    assert user.email == 'unittest01@gmail.com'
    assert user.check_password('abc123')
    assert user.username == user.email


# === Organization Model == #
@pytest.mark.django_db
def test_custom_user_to_org_relationship():

    user = CustomUser.objects.create_user(
        email = 'unittest01@gmail.com',
        password = 'abc123',
    )

    organization = Organization.objects.create(
        user = user,
        name = 'Important Company',
        size = 1500,
        industry = 'Tech'
    )

    assert organization.user.email == 'unittest01@gmail.com'
    assert organization.name == 'Important Company'
    assert organization.size == 1500
    assert organization.industry == 'Tech'

@pytest.mark.django_db
def test_custom_user_to_org_profile_signal():
    """
    Tests that the signal correctly creates an Organization Profile 
    from the CustomUser instance when an 'is_organization' flag is added.
    """
    
    user = CustomUser.objects.create_user(
        email = 'unit-test02@gmail.com',
        password = 'abc123',
        is_organization = True
    )

    orgs = Organization.objects.filter(user=user) # returns a QuerySet

    assert orgs.count() == 1
    assert orgs[0].user.email == 'unit-test02@gmail.com'
    assert orgs[0].size == 0

@pytest.mark.django_db
def test_custom_user_to_org_profile_signal_two_users():
    """
    Tests that the signal correctly creates a single Organization Profile from one of two 
    CustomUser instances with the 'is_organization' flag.
    """
    
    user1 = CustomUser.objects.create_user(
        email = 'unit-test02@gmail.com',
        password = 'abc123',
    )

    user2 = CustomUser.objects.create_user(
        email = 'unit-test03@gmail.com',
        password = 'xyz123',
        is_organization = True
    )

    all_users = CustomUser.objects.all()
    orgs = Organization.objects.all() # returns a QuerySet

    assert all_users.count() == 2 # confirms two instances created
    assert orgs.count() == 1 # confirums only one has an Organization profile from the flag
    assert orgs[0].user.email == 'unit-test03@gmail.com'
    assert orgs[0].size == 0

# === Contributor Model == #