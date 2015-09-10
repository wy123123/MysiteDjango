__author__ = 'Lovebonito'

#field validation function

def PW_validation(form,field_1,field_2,error_msg):
    if form.cleaned_data[field_1] != form.cleaned_data[field_2]:
        form._errors[field_1]=[error_msg]
        del form.cleaned_data[field_1],form.cleaned_data[field_2]
        return form
    else:
        return False