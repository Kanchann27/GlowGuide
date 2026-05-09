import pandas as pd

products = pd.read_csv("products.csv")

products.columns = products.columns.str.strip()

products["SkinType"] = products["SkinType"].str.strip().str.lower()
products["Concern"] = products["Concern"].str.strip().str.lower()
products["AgeGroup"] = products["AgeGroup"].str.strip().str.lower()

def get_routine(skin_type, concern, age_group):

    skin_type = skin_type.lower().strip()
    concern = concern.lower().strip()
    age_group = age_group.lower().strip()

    filtered = products[

        (products["SkinType"] == skin_type) &

        (products["Concern"] == concern) &

        (
            (products["AgeGroup"] == age_group) |

            (products["AgeGroup"] == "all")
        )

    ]

    if filtered.empty:
        return "⚠ No skincare routine found for this combination."

    routine = "\n========== YOUR SKINCARE ROUTINE ==========\n"

    morning_routine = "\n🌞 MORNING ROUTINE\n"
    night_routine = "\n🌙 NIGHT ROUTINE\n"
    weekly_routine = "\n🗓 WEEKLY TREATMENTS\n"

    for index, row in filtered.iterrows():

        product_info = f"""

Category   : {row['Category']}
Product    : {row['Product']}
Ingredient : {row['Ingredient']}
Frequency  : {row['Frequency']}

--------------------------------------------------
"""

        usage = row["Usage"].lower()

        if "morning" in usage:
            morning_routine += product_info

        if "night" in usage:
            night_routine += product_info

        if "weekly" in usage:
            weekly_routine += product_info

    routine += morning_routine
    routine += night_routine
    routine += weekly_routine

    routine += "\n💡 SKINCARE TIPS:\n"

    if concern == "acne":

        routine += "- Avoid touching your face frequently.\n"
        routine += "- Use non-comedogenic products.\n"
        routine += "- Change pillow covers regularly.\n"

    elif concern == "pigmentation":

        routine += "- Sunscreen is extremely important.\n"
        routine += "- Avoid excessive sun exposure.\n"

    elif concern == "sensitivity":

        routine += "- Avoid harsh scrubs.\n"
        routine += "- Patch test new products.\n"

    elif concern == "aging":

        routine += "- Use sunscreen daily.\n"
        routine += "- Focus on hydration and retinol.\n"

    elif concern == "dark circles":

        routine += "- Improve sleep schedule.\n"
        routine += "- Stay hydrated.\n"

    routine += "\n⚠ INGREDIENT WARNINGS:\n"

    ingredients = filtered["Ingredient"].str.lower().tolist()

    warning_found = False

    if "retinol" in ingredients and "glycolic acid" in ingredients:

        routine += "- Avoid using Retinol and Glycolic Acid together.\n"

        warning_found = True

    if "retinol" in ingredients and "aha" in ingredients:

        routine += "- Retinol and AHA should not be used on same night.\n"

        warning_found = True

    if "salicylic acid" in ingredients and "benzoyl peroxide" in ingredients:

        routine += "- Salicylic Acid + Benzoyl Peroxide may cause dryness.\n"

        warning_found = True

    if "kojic acid" in ingredients:

        routine += "- Use sunscreen regularly while using Kojic Acid.\n"

        warning_found = True

    if warning_found == False:

        routine += "- No major ingredient conflicts detected.\n"

    return routine