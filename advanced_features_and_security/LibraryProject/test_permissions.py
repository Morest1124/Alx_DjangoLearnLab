import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from relationship_app.models import UserProfile

def create_test_users():
    User = get_user_model()

    # Create groups if they don't exist
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    librarian_group, _ = Group.objects.get_or_create(name='Librarian')
    member_group, _ = Group.objects.get_or_create(name='Member')

    # Create an admin user
    admin_user, created = User.objects.get_or_create(username='admin', defaults={'email': 'admin@example.com'})
    if created:
        admin_user.set_password('adminpassword')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        admin_user.groups.add(admin_group)
        print('Admin user created.')
    UserProfile.objects.filter(user=admin_user).update(role='Admin')

    # Create a librarian user
    librarian_user, created = User.objects.get_or_create(username='librarian', defaults={'email': 'librarian@example.com'})
    if created:
        librarian_user.set_password('librarianpassword')
        librarian_user.is_staff = True
        librarian_user.save()
        librarian_user.groups.add(librarian_group)
        print('Librarian user created.')
    UserProfile.objects.filter(user=librarian_user).update(role='Librarian')

    # Create a member user
    member_user, created = User.objects.get_or_create(username='member', defaults={'email': 'member@example.com'})
    if created:
        member_user.set_password('memberpassword')
        member_user.save()
        member_user.groups.add(member_group)
        print('Member user created.')
    UserProfile.objects.filter(user=member_user).update(role='Member')

if __name__ == '__main__':
    create_test_users()

print(u'''
Test users have been created with the following credentials:

- **Admin:**
  - **Username:** admin
  - **Password:** adminpassword

- **Librarian:**
  - **Username:** librarian
  - **Password:** librarianpassword

- **Member:**
  - **Username:** member
  - **Password:** memberpassword

**Instructions for Manual Testing:**

1. **Run the Django development server:**
   ```bash
   python manage.py runserver
   ```

2. **Open your web browser and navigate to the admin login page:**
   [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

3. **Log in with each user and verify the following:**

   - **Admin User (`admin`):**
     - Should have access to the entire admin interface.
     - Can create, read, update, and delete all models (Books, Authors, Libraries, Users, etc.).

   - **Librarian User (`librarian`):**
     - Should have access to the admin interface but with limited permissions.
     - Should be able to add, change, and delete books.
     - Should not be able to delete users or change their permissions.
     - Verify access to other parts of the application that are specific to librarians.

   - **Member User (`member`):**
     - Should **not** have access to the admin interface.
     - Should be able to log in to the main application (if a login page exists outside the admin).
     - Should only have permissions to view books and other public content.
     - Should not be able to add, edit, or delete any data.

**To run this script, execute the following command in your shell:**
```bash
python "d:\mores\ALX BACK-END DEV\Week11\advanced_features_and_security\LibraryProject\test_permissions.py"
```
''')