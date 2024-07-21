from django import template

register = template.Library()


@register.filter
def get_date_formset(section_form, date_formsets):
    for date_formset in date_formsets:
        if date_formset.instance.pk == section_form.instance.pk:
            return date_formset
    return None