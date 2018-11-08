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

    context.homepage_settings = frappe.get_doc('Homepage', 'Homepage')
    context.get_item_route = get_item_route

    homepage_sections = frappe.get_all('Homepage Section', order_by='section_order asc')
    context.custom_sections = [frappe.get_doc('Homepage Section', name) for name in homepage_sections]

    context.twitter_handle = 'erpnext'
    context.facebook_id = 'RohitCuttingTools'
    context.youtube_channel_id = 'UCrVTlU5g3SeNSZDc1MQV8GA'
    context.youtube_video_id = '8cER4UUPxK8'
    context.email = 'help@rigpl.com'
    context.phone = '+91 2265 4545'

    return context

def get_item_route(item_code):
    return frappe.db.get_value('Item', item_code, 'route')