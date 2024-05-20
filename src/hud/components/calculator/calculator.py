from django_components import component


@component.register("calculator")
class Calculator(component.Component):
    template_name = "calculator/calculator.html"

    def get_context_data(self, el_id='', url='', div_class='', digits=[], is_ajax=False, template_name=None):
        return {
            "is_ajax": is_ajax,
            "div_class": div_class,
            "el_id": el_id,
            "template_name": template_name,
            "url": url,
            "digits": digits,
        }

    class Media:
        css = "calculator/calculator.css"
        js = "calculator/calculator.js"
