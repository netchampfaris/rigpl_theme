from itertools import product

def get_context(context):
	print(context.attributes, context.attribute_values)

	values_to_cross = []

	for d in context.attributes:
		attr_values = context.attribute_values[d.attribute]
		values_to_cross.append(attr_values)

	context.cross_product = list(product(*values_to_cross))
	return context
