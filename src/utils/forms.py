
def add_attr(item, attr, value):
    existing_value = item.field.widget.attrs.get(attr, '')
    return item.as_widget(attrs={
        **item.field.widget.attrs,
        attr: ' '.join(
            filter(None, [existing_value, value])
        ),
    })
