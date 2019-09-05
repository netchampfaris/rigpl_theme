import frappe

def update_top_bar_items(context):
	context.top_bar_items = get_top_bar_items()

def get_top_bar_items():
	all_top_items = frappe.db.sql("""
		select * from `tabTop Bar Item`
		where parent='Website Settings' and parentfield = 'top_bar_items'
		order by idx asc""", as_dict=1)

	top_items = all_top_items[:]

	# attach child items to parent items
	for d in all_top_items:
		if d['parent_label']:
			for t in top_items:
				if t['label']==d['parent_label']:
					if not 'child_items' in t:
						t['child_items'] = []
					t['child_items'].append(d)
					break
	return top_items
