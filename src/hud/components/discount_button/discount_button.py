from django_components import component

@component.register("discount_button")
class DiscountButton(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "discount_button/discount_button.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(self, div_class='', input_class='', btn_class='', item=None ):
        return {
            "item": item,
            "div_class": div_class,
            "input_class": input_class,
            "btn_class": btn_class,
        }