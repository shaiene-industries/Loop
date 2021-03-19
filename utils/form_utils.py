def bootstrap_format(fields : dict, float=False):    
    """
    Aplica a classe .form-control nos inputs e o tipo 'date' nos inputs de data
    """
    NON_FORM_CONTROL = ('hidden', 'checkbox')
    def add_widget_attrs(field, value, attr="class"):
        try:
            field.widget.attrs[attr] += " "+value
        except KeyError:
            field.widget.attrs[attr] = value
        return field
    for field in fields:
        try:
            ### Formatação de inputs
            # form-control
            if(fields[field].widget.__module__ == 'markdownx.widgets'):
                fields[field] = add_widget_attrs(fields[field], "form-control")
            if (fields[field].widget.input_type not in NON_FORM_CONTROL):        
                fields[field] = add_widget_attrs(fields[field], "form-control")
                if float:
                    fields[field] = add_widget_attrs(fields[field], "placeholder", "placeholder")
            # date
            if ('data' in field):
                fields[field].widget.attrs['title'] = "Insira uma data no formato dd/mm/aaaa"
                fields[field].widget.input_type = "date"
            # Interrogação para checkbox
            if (fields[field].widget.input_type == 'checkbox'):
                fields[field] = add_widget_attrs(fields[field], "check-question")
            # Seta em selects
            if (fields[field].widget.input_type == 'select'):
                fields[field] = add_widget_attrs(fields[field], "form-select")
        except AttributeError:            
            continue
    return fields