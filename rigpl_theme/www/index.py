from __future__ import unicode_literals
import frappe

no_cache = 1
no_sitemap = 1

def get_context(context):
    context.blogs = frappe.get_all('Blog Post',
        fields=['title', 'blogger', 'blog_intro', 'route'],
        filters={
            'published': 1
        },
        order_by='modified desc',
        limit=3
    )

    context.products = frappe.get_all('Item',
        filters={
            'show_in_website': 1,
        },
        fields=['image', 'item_name', 'item_group', 'route', 'weightage'],
        order_by='modified desc',
        limit=3
    )

    homepage_sections = frappe.get_all('Homepage Section')
    context.custom_sections = [frappe.get_doc('Homepage Section', name) for name in homepage_sections]

    return context
