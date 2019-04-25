from django.contrib import messages

class DangerMessageMixin:
    """
    Add a success message on successful form submission.
    """
    danger_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        danger_message = self.get_danger_message(form.cleaned_data)
        if danger_message:
            messages.error(self.request, danger_message)
        return response

    def get_danger_message(self, cleaned_data):
        return self.danger_message % cleaned_data


class WarningMessageMixin:
    """
    Add a success message on successful form submission.
    """
    warning_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        warning_message = self.get_warning_message(form.cleaned_data)
        if warning_message:
            messages.warning(self.request, warning_message)
        return response

    def get_warning_message(self, cleaned_data):
        return self.warning_message % cleaned_data

class InfoMessageMixin:
    """
    Add a success message on successful form submission.
    """
    info_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        info_message = self.get_info_message(form.cleaned_data)
        if info_message:
            messages.info(self.request, info_message)
        return response

    def get_info_message(self, cleaned_data):
        return self.info_message % cleaned_data
