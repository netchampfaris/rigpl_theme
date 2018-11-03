import frappe
from itertools import product

def get_context(context):
	valid_attribute_keys = []
	attributes_map = frappe._dict({})

	for variant in (context.variants or []):
		variant.attribute_map = frappe._dict({})
		for attr in variant.attributes:
			variant.attribute_map[attr.attribute] = attr.attribute_value

	for d in context.attributes:
		attributes_map[d.attribute] = d

		if context.attribute_values:
			attr_values = context.attribute_values[d.attribute]
			if len(attr_values) > 1:
				valid_attribute_keys.append(d.attribute)

	context.valid_attribute_keys = valid_attribute_keys
	context.attributes_map = attributes_map

	# meta information
	doc = context.doc

	context.meta = frappe._dict({})
	context.meta.keywords = ','.join([doc.item_code, doc.item_name, doc.description, doc.item_group])
	context.meta.url = frappe.utils.get_url() + '/' + context.route
	context.meta.image = frappe.utils.get_url() + context.website_image
	context.meta.description = doc.description[:150]

	return context
