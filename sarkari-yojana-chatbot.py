def chatbot():
    print("Hello! Main ek Sarkari Yojna Chatbot hoon. Aap kis scheme ke baare mein jaanana chahenge?")
    print("Aap in schemes ke baare mein pooch sakte hain: PMAY, PMKVY, Ayushman Bharat, PMJDY, Beti Bachao.")

    while True:
        user_input = input("Aapka sawaal likhiye (ya 'exit' likhkar band karein): ").lower()

        if 'pmay' in user_input:
            print("PMAY (Pradhan Mantri Awas Yojana): Gramin aur Shehri ilako mein ghar banwane ke liye loan aur subsidy milti hai.")
        elif 'pmkvy' in user_input:
            print("PMKVY (Pradhan Mantri Kaushal Vikas Yojana): Free skill training aur certificate courses provide kiye jaate hain.")
        elif 'ayushman' in user_input:
            print("Ayushman Bharat: 5 lakh tak ka free health insurance har eligible family ke liye.")
        elif 'pmjdy' in user_input:
            print("PMJDY (Jan Dhan Yojana): Sabke liye bank account kholne ki yojana, zero balance account aur insurance ke saath.")
        elif 'beti' in user_input or 'bachao' in user_input:
            print("Beti Bachao, Beti Padhao: Ladkiyon ki shiksha aur suraksha ke liye government scheme.")
        elif 'exit' in user_input:
            print("Dhanyavaad! Aapne chatbot ka upyog kiya.")
            break
        else:
            print("Maaf kijiye, main is vishay mein madad nahi kar sakta. Kripya kisi aur scheme ka naam likhiye.")

# Run the chatbot
chatbot()