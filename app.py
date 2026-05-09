from logic import get_routine

print("✨ Welcome to GlowGuide AI ✨")
print("Personalized Skin Care Routine Generator\n")

skin_type = input("Enter your skin type: ")
concern = input("Enter your skin concern: ")

age = int(input("Enter your age: "))

if age <= 17:
    age_group = "Teen"

elif age <= 25:
    age_group = "18-25"

elif age <= 35:
    age_group = "26-35"

elif age <= 45:
    age_group = "36-45"

else:
    age_group = "45+"

routine = get_routine(
    skin_type,
    concern,
    age_group
)

print(routine)