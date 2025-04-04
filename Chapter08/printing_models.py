
def print_models(unprinted, completed):
    """Simulate printing then move until all printed"""
    while unprinted:
        current = unprinted.pop()
        #simulate creating a 3d print
        print("Printing model: " + current)
        completed.append(current)

def show_completed(completed):
    """Display completed models"""
    print("\nThe following models have been printed:")
    for items in completed_models:
        print(items)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed(completed_models)
