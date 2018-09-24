from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


User = get_user_model()


from .models import Profile
from .forms import UserAdminCreationForm, UserAdminChangeForm



class ProfileItemInline(admin.TabularInline):
    model = Profile
    raw_id_field = [ 'phone',]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin','id',)
    list_filter = ('admin','staff','active')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        # ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    # filter_horizontal = ()

    inlines = [ProfileItemInline]


admin.site.register(User, UserAdmin)


admin.site.register(Profile)