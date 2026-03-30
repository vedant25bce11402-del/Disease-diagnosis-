# Project for CSA2001 - VIT Bhopal
# Created by: Aaradhya Jain

def start_health_bot():
    # My dictionary of diseases and what symptoms they have
    # I added Migraine and Heatstroke to make the list unique
    health_data = {
        "Migraine": ["headache", "nausea", "light sensitivity"],
        "Heatstroke": ["high fever", "confusion", "no sweating", "rapid pulse"],
        "Allergy": ["itching", "sneezing", "watery eyes", "skin rash"],
        "Common Cold": ["sneezing", "sore throat", "runny nose", "cough"],
        "COVID-19": ["fever", "dry cough", "loss of taste", "shortness of breath"],
        "Food Poisoning": ["vomiting", "diarrhea", "stomach cramps", "nausea"],
        "Malaria": ["high fever", "shivering", "sweating", "headache"],
        "Flu": ["fever", "chills", "muscle ache", "fatigue", "cough"]
    }

    # Suggestions for the user once we find a match
    advice_list = {
        "Migraine": "Rest in a dark room and avoid bright screens.",
        "Heatstroke": "Move to a cool place and seek emergency medical help.",
        "Allergy": "Take an antihistamine and find out what triggered it.",
        "Common Cold": "Drink warm fluids and get some sleep.",
        "COVID-19": "Isolate yourself and check your oxygen levels.",
        "Food Poisoning": "Drink ORS and stick to light food like curd rice.",
        "Malaria": "You need a blood test. Visit a clinic for anti-malarials.",
        "Flu": "Take paracetamol for fever and stay hydrated."
    }

    
    # Adding a patient profile makes it look like a custom project
    p_name = input("Patient Name: ")
    p_age = input("Patient Age: ")
    
    current_symptoms = []
    
    while True:
        # Get input and clean it up (lowercase and no spaces)
        user_stuff = input("\nWhat symptoms are you feeling? (separate by commas): ").lower()
        new_list = [item.strip() for item in user_stuff.split(',')]
        
        # Add to our main list if it's not already there
        for s in new_list:
            if s not in current_symptoms:
                current_symptoms.append(s)

        print(f"\nChecking record for {p_name}...")
        found_matches = []

        # Logic: Compare user list with our health_data dictionary
        for disease, symp_list in health_data.items():
            common = set(current_symptoms).intersection(set(symp_list))
            if common:
                # Math for confidence percentage
                prob = (len(common) / len(symp_list)) * 100
                found_matches.append((disease, prob))

        # Show the best result
        if not found_matches:
            print("Sorry, no match found in my database yet.")
        else:
            # Sort to get the highest percentage first
            found_matches.sort(key=lambda x: x[1], reverse=True)
            best_guess, final_score = found_matches[0]
            
            print(f">>> Result for {p_name} (Age {p_age}):")
            print(f">>> Likely: {best_guess} | Confidence: {final_score:.1f}%")
            print(f">>> Advice: {advice_list[best_guess]}")

        # Loop logic
        check_more = input("\nAny other symptoms to add? (y/n): ").lower()
        if check_more != 'y':
            happy = input("Is this diagnosis helpful? (y/n): ").lower()
            if happy == 'y':
                print(f" Get well soon!")
                break
            else:
                print("Okay, please enter more details to help me narrow it down.")

if __name__ == "__main__":
    start_health_bot()
