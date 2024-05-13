from django_components import component

@component.register("qty_button")
class QuantityButton(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "qty_button/qty_button.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, div_class='', input_class='', btn_class='', qty=1 ):
        return {
            "qty": qty,
            "div_class": div_class,
            "input_class": input_class,
            "btn_class": btn_class,
        }

    class Media:
        css = "qty_button/qty_style.css"
        js = "qty_button/qty_script.js"