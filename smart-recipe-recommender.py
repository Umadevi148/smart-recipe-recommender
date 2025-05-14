WEIGHT_MAP = {
    'small onion': 30,
    'medium onion': 50,
    'big onion': 70,
    'onion': 50,
    'small tomato': 80,
    'medium tomato': 100,
    'big tomato': 150,
    'tomato': 100,
    '1 handful beans': 50,
    '2 handful beans': 100,
    '3 handful beans': 150
}

# Normalize ingredient names for internal consistency
NORMALIZE_MAP = {
    'small onion': 'onion',
    'medium onion': 'onion',
    'big onion': 'onion',
    'small tomato': 'tomato',
    'medium tomato': 'tomato',
    'big tomato': 'tomato',
    '1 handful beans': 'beans',
    '2 handful beans': 'beans',
    '3 handful beans': 'beans',
    'onion': 'onion',
    'tomato': 'tomato',
    'beans': 'beans'
}

# Sample recipe database
RECIPES = [
    {
        'name': 'Plain Onion Fry',
        'ingredients': {'onion': 50},
        'steps': [
            "Slice onions thinly.",
            "Heat oil, add mustard seeds and curry leaves.",
            "Add onions, salt, turmeric.",
            "Fry until golden. Serve with rice or roti."
        ]
    },
    {
        'name': 'Tomato Chutney',
        'ingredients': {'tomato': 100},
        'steps': [
            "Chop tomatoes.",
            "Heat oil, fry tomatoes with salt and spices.",
            "Cook until mushy. Cool and blend.",
            "Temper with mustard seeds."
        ]
    },
    {
        'name': 'Onion Tomato Curry',
        'ingredients': {'onion': 50, 'tomato': 100},
        'steps': [
            "Sauté chopped onions till golden.",
            "Add tomatoes and spices.",
            "Cook until soft and blended. Serve hot."
        ]
    },
    {
        'name': 'Beans Stir Fry',
        'ingredients': {'beans': 50},
        'steps': [
            "Chop beans.",
            "Heat oil, add mustard seeds and curry leaves.",
            "Add beans, salt, turmeric, chili powder.",
            "Stir-fry until cooked but crunchy."
        ]
    },
    {
        'name': 'Mixed Veg Curry',
        'ingredients': {'onion': 50, 'tomato': 100, 'beans': 50},
        'steps': [
            "Chop all vegetables.",
            "Sauté onion and tomato with spices.",
            "Add beans, a little water and cook covered.",
            "Simmer until vegetables are soft."
        ]
    }
]

def get_user_ingredients():
    print("\nEnter ingredients (e.g., '2 small onion', '1 medium tomato', '2 handful beans'). Type 'done' to finish.")
    ingredients = {}
    while True:
        entry = input("Ingredient input: ").strip().lower()
        if entry == 'done':
            break

        try:
            parts = entry.split(maxsplit=1)
            if len(parts) == 1:
                print("Invalid input. Try something like '2 small onion'.")
                continue

            count = int(parts[0])
            unit = parts[1]

            key = f"{count} {unit}" if 'handful' in unit else f"{unit}"
            if key not in WEIGHT_MAP:
                print(f"Unknown format: '{key}'. Valid options: small onion, big tomato, 2 handful beans, etc.")
                continue

            base_item = NORMALIZE_MAP[key]
            weight = count * WEIGHT_MAP[key] if 'handful' not in key else WEIGHT_MAP[key]
            ingredients[base_item] = ingredients.get(base_item, 0) + weight

        except Exception:
            print("Please enter in format like '1 small onion', '2 big tomato', or '1 handful beans'")
    return ingredients

def get_servings(user_ingredients, required_ings):
    servings = float('inf')
    for ing, amt in required_ings.items():
        if ing not in user_ingredients or user_ingredients[ing] < amt:
            return 0
        possible = user_ingredients[ing] // amt
        servings = min(servings, possible)
    return int(servings)

def suggest_recipes(user_ingredients):
    suggestions = []
    for recipe in RECIPES:
        servings = get_servings(user_ingredients, recipe['ingredients'])
        if servings >= 1:
            suggestions.append((recipe, servings))
    return suggestions

def main():
    user_ingredients = get_user_ingredients()
    suggestions = suggest_recipes(user_ingredients)

    if not suggestions:
        print("\nNo suitable recipes found for your inputs.")
        return

    print("\nBased on your ingredients, you can cook:")
    for recipe, serves in suggestions:
        print(f"\n--- {recipe['name']} ---")
        print(f"Can serve: {serves} person(s)")
        print("Steps:")
        for i, step in enumerate(recipe['steps'], 1):
            print(f"  {i}. {step}")

if __name__ == "__main__":
    main()