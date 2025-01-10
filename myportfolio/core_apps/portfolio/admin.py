from django.contrib import admin

from .models import (
    AboutSectionTitleModel, ContactModel, MediaFileUploadModel, ResumeCounterModel, RoleNameModel, ShortIntroModel
)

# Register your models here.
admin.site.register(ContactModel)
admin.site.register(RoleNameModel)
admin.site.register(AboutSectionTitleModel)
admin.site.register(ResumeCounterModel)
admin.site.register(ShortIntroModel)
admin.site.register(MediaFileUploadModel)
