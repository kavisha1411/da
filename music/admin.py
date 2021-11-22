from django.contrib import admin, messages
from django.http.response import HttpResponseRedirect
from .models import Artist, Album, Song
from django.utils.translation import ngettext
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

admin.site.empty_value_display = 'unknown'
admin.site.site_header = 'Django example header'
admin.site.site_title = 'Django example title'
admin.site.index_title = 'Welcome to this Portal'


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'status')
    actions = ['mark_verified', 'mark_unverified']
    list_display_links = ('name', 'surname')
    list_editable = (['status'])
    
    @admin.action(description='Mark selected artists as verified')
    def mark_verified(self, request, queryset):
        number_updated = queryset.update(status='v')
        self.message_user(request, ngettext(
            '%d artist was successfully marked as verified.',
            '%d artists were successfully marked as verified.',
            number_updated,
        ) % number_updated, messages.SUCCESS)

    @admin.action(description='Mark selected artists as unverified')
    def mark_unverified(self, request, queryset):
        number_updated = queryset.update(status='u')
        self.message_user(request, ngettext(
            '%d artist was successfully marked as unverified.',
            '%d artists were successfully marked as unverified.',
            number_updated,
        ) % number_updated, messages.SUCCESS)


class AlbumForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Album
        fields = ('name', )
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique"
            }
        }


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'details_album']
    name = ['name']
    list_filter=(name)
    search_fields = ('name__startswith', )
    form = AlbumForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'number_songs'),
        }),
    )


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song)


