from django import template

register = template.Library()

def isRowStart(value):
    return (value-1)%3

register.filter('isRowStart', isRowStart)