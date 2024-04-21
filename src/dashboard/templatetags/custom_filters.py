from django import template


register = template.Library()

def num_range():
    print("Value = ", 5)
    return (1,2,3,4,5)

register.filter('num_range', num_range)