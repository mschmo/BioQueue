from django import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class SingleJobForm(forms.Form):
    protocol = forms.IntegerField(
        required=True,
        widget=forms.Select(
            attrs={
                'class': u'input-block-level',
            }
        )
    )

    input_file_rf = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': u'input-block-level',
            }
        )
    )

    input_file_r = forms.CharField(
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': u'input-block-level',
            }
        )
    )

    parameter = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': u'input-block-level',
            }
        )
    )


class JobManipulateForm(forms.Form):
    job = forms.IntegerField(
        required=True
    )


class ProtocolManipulateForm(forms.Form):
    parent = forms.IntegerField(
        required=True
    )


class CreateProtocolForm(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': u'input-block-level',
            }
        )
    )


class CreateStepForm(forms.Form):
    software = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': u'input-block-level',
            }
        )
    )
    parameter = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': u'input-block-level',
            }
        )
    )
    parent = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput()
    )


class StepManipulateForm(forms.Form):
    parent = forms.IntegerField(
        required=True,
    )
    id = forms.IntegerField(
        required=True,
    )
    parameter = forms.CharField(
        required=False,
    )


class ShareProtocolForm(forms.Form):
    peer = forms.CharField(
        required=True,
    )
    pro = forms.IntegerField(
        required=True,
    )


class QueryLearningForm(forms.Form):
    stephash = forms.CharField(
        required=True,
    )
    type = forms.IntegerField(
        required=True,
    )


class CreateReferenceForm(forms.Form):
    name = forms.CharField(
        required=True,
    )
    path = forms.CharField(
        required=True,
    )


class RestrictedFileField(forms.FileField):

    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")

        super(RestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        file = super(RestrictedFileField, self).clean(data, initial)

        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
                        filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise ValidationError(_('Filetype not supported.'))
        except AttributeError:
            pass

        return data


class BatchJobForm(forms.Form):
    job_list = RestrictedFileField(content_types=['text/plain'], max_upload_size=2621440)