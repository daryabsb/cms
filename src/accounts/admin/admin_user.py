from django.contrib import admin
from src.accounts.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea


@admin.register(User)
class UserAdminConfig(UserAdmin):
	model = User
	# search_fields = ('email','name',)
	list_filter = ('email','name','is_active','is_staff')
	ordering = ('-dob',)
	list_display=('email','name','is_active','is_staff','created','updated')

	fieldsets=(
			(None,{'fields':('email', 'name','image','dob','password')}),
			('Permissions',{'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
			('Personal',{'fields':('phone_number','facebook_url','twitter_url','linkedin_url','about',)}),
		)

	formfield_overrides = {
		User.about: {'widget': Textarea(attrs={'rows':10,'cols':40})},
	}

	add_fieldsets = (
	(None,{
		'classes':('wide',),
		'fields':('email','phone_number','name','image','dob','password1','password2','is_active','is_staff','groups','user_permissions')
		}
		),
	)


# Register your models here.
