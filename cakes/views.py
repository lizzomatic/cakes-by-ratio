from django.shortcuts import render
import math

def calculator(request):
    recipe = None
    error = None
    #message = None
    eggs_input = ''
    people_input = ''
    
    if request.method == 'POST':
        try:
            eggs = int(request.POST.get('eggs', 0))
            people = int(request.POST.get('people', 0))
            eggs_input = eggs
            people_input = people
            
            if eggs < 2 * people:
                multiplier = eggs
            if eggs <= 0 or people <= 0:
                error = "Please enter positive numbers for eggs and people."
            else:
            
                # Base recipe (for 1 egg)
                base_recipe = {
                    'banana': 1,
                    'banana_cups': 0.5,
                    'eggs': 1,
                    'baking_soda': 0.75,
                    'flax_seeds': 1,
                    'seeds_nuts_grains': 0.5,
                    'cinnamon': 1,
                    'ginger': 1,
                    'vinegar': 2.5,
                    'fresh fruit': 0.5,
                }
                
                # Scale recipe - determine multiplier & message
                # eggs limiting factor
                if (eggs < 2 * people):
                    multiplier = eggs
                # people limiting factor
                #if  (eggs >= 2 * people):
                else:
                    multiplier = math.ceil(people / 2)
              
                recipe = {
                    'banana': base_recipe['banana'] * multiplier,
                    'banana_cups': base_recipe['banana_cups'] * multiplier,
                    'eggs': base_recipe['eggs'] * multiplier,
                    'baking_soda': base_recipe['baking_soda'] * multiplier,
                    'flax_seeds': base_recipe['flax_seeds'] * multiplier,
                    'seeds_nuts_grains': base_recipe['seeds_nuts_grains'] * multiplier,
                    'cinnamon': base_recipe['cinnamon'] * multiplier,
                    'ginger': base_recipe['ginger'] * multiplier,
                    'vinegar': base_recipe['vinegar'] * multiplier,
                    'fruit': base_recipe['fresh fruit'] * multiplier,
                    'serves': eggs * 2,
                    'cakes_made': eggs,
                }
                
        except ValueError:
            error = "Please enter valid numbers."
    
    return render(request, 'cakes/calculator.html', {
        'recipe': recipe,
        'error': error,
        'eggs_input': eggs_input,
        'people_input': people_input,
    })