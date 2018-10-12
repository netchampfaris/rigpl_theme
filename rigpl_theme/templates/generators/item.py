from itertools import product

def get_context(context):
	print(context.attributes, context.attribute_values)

	valid_attribute_keys = []
	values_to_cross = []

	for d in context.attributes:
		attr_values = context.attribute_values[d.attribute]
		if len(attr_values) > 1:
			valid_attribute_keys.append(d.attribute)
			values_to_cross.append(attr_values)

	context.cross_product = list(product(*values_to_cross))
	context.valid_attribute_keys = valid_attribute_keys
	return context
