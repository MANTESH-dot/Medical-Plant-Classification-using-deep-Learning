from tkinter import*
from tkinter import filedialog
from PIL import Image, ImageTk
import pickle
import cv2
import numpy as np
from tkinter import messagebox

class Main:
    def __init__(self, root):
        self.root = root
        root.geometry("1530x840+0+0")
        self.root.title("Medicinal Leaf Detection")

        main_frame = Frame(self.root, bd=10, relief=RIDGE)
        main_frame.place(x=0, y=0, width=1530, height=840)

        # Background Image
        img = Image.open("img.webp")
        img = img.resize((756, 825), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label = Label(main_frame, image=self.photoimg)
        f_label.place(x=0, y=0, width=756, height=825)

        # Predict button
        b1_1 = Button(main_frame, text="Classify", cursor="hand2",
                      font=("time new roman", 15, "bold"), bg="#4A7C59", fg="black", command=self.predict_image)
        b1_1.place(x=820, y=760, width=250, height=40)

        # Output label for displaying predictions directly below the button
        self.output_label = Label(main_frame, text="", font=("times new roman", 18, "bold"), fg="red", bg="light green")
        self.output_label.place(x=1300, y=760, width=180, height=40)

        # Information label for displaying medicinal uses on the left side
        self.info_label = Label(main_frame, text="", font=("times new roman", 13)
        , borderwidth=6, relief=RIDGE,fg="black", bg="#D0E2D0", justify=LEFT, wraplength=580)
        self.info_label.place(x=756, y=500, width=756, height=240)

        # Image label for displaying the selected image on the right side
        self.image_label = Label(main_frame, bg="#D0E2D0", borderwidth=6, relief=RIDGE)
        self.image_label.place(x=756, y=50, width=756, height=400)

        info_label = Label(main_frame, text="Medicinal Information", font=("times new roman", 20, "bold"),
                           fg="black", bg="light green", borderwidth=6, relief=RIDGE)
        info_label.place(x=756, y=450, width=756, height=50)

        image_label = Label(main_frame, text="Selected Image", font=("times new roman", 20, "bold"),
                            fg="black", bg="light green", borderwidth=6, relief=RIDGE)
        image_label.place(x=756, y=0, width=756, height=50)

        output_label = Label(main_frame, text="Name:", font=("times new roman", 18, "bold"), fg="black", bg="light green")
        output_label.place(x=1250, y=760, width=70, height=40)

        # Load the model
        with open(r"model_3.pkl", "rb") as file:
            self.model = pickle.load(file)

        # Medicinal uses dictionary
        self.medicinal_uses = {



            'Holy Basil': {
                            'properties': 'Rich in essential oils, antibacterial, antifungal, and adaptogenic properties.',
                            'uses': 'Used for cough, cold, fever, respiratory issues, and stress relief.',
                            'nutritional_benefits': 'Contains vitamins A and C, calcium, and zinc.',
                            'side_effects': 'Excessive consumption may cause nausea; not recommended during pregnancy in high doses.',
                            'additional_uses': 'Commonly used in religious rituals, herbal teas, and natural remedies.'
                        },
            'Chilly': {
                            'properties': 'Contains capsaicin with anti-inflammatory and pain-relieving properties.',
                            'uses': 'Used for pain relief, metabolism boosting, and improving circulation.',
                            'nutritional_benefits': 'Rich in vitamins A, C, and E, and beta-carotene.',
                            'side_effects': 'Excessive consumption can cause stomach irritation and heartburn.',
                            'additional_uses': 'Widely used as a spice and natural preservative.'
                        },
            'Water Hyssop': {
                            'properties': 'Enhances cognitive function, anti-inflammatory, and antioxidant properties.',
                            'uses': 'Used for memory enhancement, reducing anxiety, and improving concentration.',
                            'nutritional_benefits': 'Contains alkaloids, saponins, and flavonoids.',
                            'side_effects': 'May cause nausea and stomach upset in some individuals.',
                            'additional_uses': 'Used in Ayurvedic medicine and herbal supplements for mental health.'
                        },
            'Papaya': {
                            'properties': 'Contains papain enzyme, aids in digestion and rich in antioxidants.',
                            'uses': 'Used for digestive health, skin care, and improving immune function.',
                            'nutritional_benefits': 'High in vitamin C, folate, fiber, and carotenes.',
                            'side_effects': 'Excessive consumption may cause digestive upset and allergic reactions in some people.',
                            'additional_uses': 'Popular in skincare for exfoliation and as a digestive aid.'
                        },
            'Peppermint': {
                            'properties': 'Cooling and soothing properties, antibacterial and antifungal.',
                            'uses': 'Used for relieving headaches, congestion, and skin irritation.',
                            'nutritional_benefits': 'Contains menthol and essential oils.',
                            'side_effects': 'Excessive use may cause skin irritation or allergic reactions.',
                            'additional_uses': 'Used in balms, ointments, and as a flavoring agent.'
                        },
            'Five-leaved Chaste Tree': {
                            'properties': 'Antibacterial and antifungal properties, aids digestion.',
                            'uses': 'Used for treating indigestion, bad breath, and oral health.',
                            'nutritional_benefits': 'Rich in essential oils and tannins.',
                            'side_effects': 'Excessive consumption may cause nausea or throat irritation.',
                            'additional_uses': 'Used in traditional medicine for oral hygiene and in culinary preparations.'
                        },
            'Vida': {
                            'properties': 'Contains various antioxidants and vitamins, supports general health.',
                            'uses': 'Used for immune support, energy boost, and antioxidant benefits.',
                            'nutritional_benefits': 'Rich in various vitamins and polyphenols.',
                            'side_effects': 'May cause mild digestive issues in some individuals.',
                            'additional_uses': 'Commonly used in traditional medicine for boosting stamina and immunity.'
                        },
            'Hibiscus': {
                            'properties': 'Rich in antioxidants, aids in lowering blood pressure, supports liver health.',
                            'uses': 'Often used for hypertension, liver issues, and as an immune booster.',
                            'nutritional_benefits': 'Contains vitamin C, iron, calcium, and anthocyanins.',
                            'side_effects': 'May lower blood pressure excessively in some individuals; avoid during pregnancy.',
                            'additional_uses': 'Used in herbal teas and as a natural dye due to its red pigment.'
                        },
            'Neem': {
                            'properties': 'Antibacterial, antifungal, antiviral, and anti-inflammatory.',
                            'uses': 'Used for skin health, treating infections, and improving oral health.',
                            'nutritional_benefits': 'Contains nimbin, nimbidin, and other bioactive compounds.',
                            'side_effects': 'Excessive consumption may cause nausea and liver issues.',
                            'additional_uses': 'Used in cosmetics, skincare, and as a natural pesticide.'
                        },
            'Bitter Gourd': {
                            'properties': 'High in vitamin C and antioxidants, helps regulate blood sugar.',
                            'uses': 'Used to treat diabetes, digestive issues, and skin conditions.',
                            'nutritional_benefits': 'Rich in vitamins A and C, folate, and fiber.',
                            'side_effects': 'Can cause stomach upset in some individuals; excessive use may lead to hypoglycemia.',
                            'additional_uses': 'Often used in cooking for its bitter flavor and as a vegetable.'
                        },
            'Lemon': {
                            'properties': 'Rich in vitamin C, antioxidants, and antibacterial properties.',
                            'uses': 'Used for immunity boosting, digestive health, and detoxification.',
                            'nutritional_benefits': 'High in vitamin C, potassium, and pectin fiber.',
                            'side_effects': 'High acidity can erode tooth enamel; may cause heartburn in some people.',
                            'additional_uses': 'Used as a natural preservative, in cleaning, and in aromatherapy.'
                        },
            'Roselle': {
                            'properties': 'Rich in antioxidants and bioactive compounds.',
                            'uses': 'Used for promoting heart health and reducing inflammation.',
                            'nutritional_benefits': 'Contains flavourings, tannins, and poly phenols.',
                            'side_effects': 'May cause mild digestive issues if consumed excessively.',
                            'additional_uses': 'Used in herbal remedies and traditional medicine for relaxation.'
                        },
            'Curry Leaves': {
                            'properties': 'Antioxidant, antibacterial, and anti-inflammatory properties.',
                            'uses': 'Used for improving digestion, managing diabetes, and promoting hair growth.',
                            'nutritional_benefits': 'Rich in vitamins A, B, C, and E, and iron.',
                            'side_effects': 'Excessive consumption may cause stomach upset.',
                            'additional_uses': 'Widely used in cooking and Ayurvedic treatments for hair care.'
                        },
            'Guava': {
                            'properties': 'Rich in vitamin C, antioxidants, and dietary fiber.',
                            'uses': 'Used for boosting immunity, improving digestion, and skin health.',
                            'nutritional_benefits': 'Contains vitamin C, potassium, and lycopene.',
                            'side_effects': 'Excessive consumption may cause digestive discomfort.',
                            'additional_uses': 'Eaten as a fruit or used in juices, jams, and desserts.'
                        },
            'Tea': {
                            'properties': 'Contains antioxidants, caffeine, and anti-inflammatory compounds.',
                            'uses': 'Commonly used for alertness, reducing inflammation, and as an immune booster.',
                            'nutritional_benefits': 'Provides small amounts of potassium, fluoride, and manganese.',
                            'side_effects': 'High caffeine intake can lead to anxiety, insomnia, and digestive issues.',
                            'additional_uses': 'Used in skincare and as a flavoring ingredient in culinary dishes.'
                        },
            'MariGold': {
                            'properties': 'Contains lutein and flavourings with anti-inflammatory properties.',
                            'uses': 'Used for skin health, wound healing, and reducing inflammation.',
                            'nutritional_benefits': 'Rich in antioxidants and carotenoids.',
                            'side_effects': 'May cause allergic reactions in some individuals.',
                            'additional_uses': 'Used in skincare, teas, and as an ornamental plant.'
                        },
            'Turmeric': {
                            'properties': 'Contains curcumin, known for its anti-inflammatory and antioxidant effects.',
                            'uses': 'Used for arthritis, joint pain, digestive issues, and as an anti-inflammatory.',
                            'nutritional_benefits': 'Contains iron, manganese, and curcuminoids which support health.',
                            'side_effects': 'High doses may cause digestive upset; avoid during pregnancy in medicinal amounts.',
                            'additional_uses': 'Used in cooking, particularly in curries, and as a natural dye.'
                        },
            'Aloe Vera': {
                            'properties': 'Rich in vitamins and minerals, soothing and healing for skin.',
                            'uses': 'Used for burns, skin irritation, digestive health, and immune support.',
                            'nutritional_benefits': 'Contains vitamins A, C, E, and several B vitamins.',
                            'side_effects': 'Oral consumption may cause diarrhea; not recommended for pregnant women.',
                            'additional_uses': 'Used in cosmetics, skincare, and as a natural moisturizer.'
                        },
            'Taro': {
                            'properties': 'Rich in fiber, vitamins, and minerals, aids in digestion.',
                            'uses': 'Used for digestive issues, improving gut health, and as a source of energy.',
                            'nutritional_benefits': 'High in fiber, potassium, magnesium, and vitamin C.',
                            'side_effects': 'Must be cooked thoroughly to remove toxins; raw taro can cause throat irritation.',
                            'additional_uses': 'Widely used in cooking, especially in stews and as a starchy vegetable.'
                        },
            'Linden': {
                            'properties': 'Calming properties, often used in herbal teas.',
                            'uses': 'Used for relaxation, relieving anxiety, and promoting sleep.',
                            'nutritional_benefits': 'Contains flavourings, tannins, and volatile oils that support relaxation.',
                            'side_effects': 'Excessive use may lead to drowsiness or allergic reactions in sensitive individuals.',
                            'additional_uses': 'Used in aromatherapy and as a sleep aid in herbal preparations.'
                        },
            'Java Plum': {
                            'properties': 'Rich in antioxidants, supports blood sugar regulation.',
                            'uses': 'Used for managing diabetes, digestive health, and improving immunity.',
                            'nutritional_benefits': 'High in vitamin C, iron, and flavourings.',
                            'side_effects': 'Excessive consumption may lead to constipation or throat irritation.',
                            'additional_uses': 'Used in traditional medicine and as a flavoring in juices and desserts.'
                        },
            'Coriander': {
                            'properties': 'Anti-inflammatory, antimicrobial, and rich in antioxidants.',
                            'uses': 'Used for improving digestion, reducing blood sugar levels,and managing cholesterol.',
                            'nutritional_benefits': 'Rich in vitamin K, vitamin C,potassium, and dietary fiber.',
                            'side_effects':'Excessive consumption may cause skin sensitivity or allergic reactions in some individuals.',
                            'additional_uses': 'Commonly used as a spice,in herbal teas, and in traditional medicines for detoxification.'
                        },
            'White Fig': {
                            'properties': 'Rich in dietary fiber, antioxidants, and natural sugars.',
                            'uses': 'Used for managing constipation, improving digestion, and supporting heart health.',
                            'nutritional_benefits': 'High in calcium, potassium, and magnesium.',
                            'side_effects': 'Excessive consumption may cause diarrhea or bloating.',
                            'additional_uses': 'Used in traditional medicine, desserts, and as a natural sweetener.'
                        },
            'Cluster Fig': {
                            'properties': 'Anti diabetic, anti-inflammatory, and antimicrobial properties.',
                            'uses': 'Used for managing diabetes, skin infections, and improving liver health.',
                            'nutritional_benefits': 'Contains vitamins A and C, calcium, and photochemical.',
                            'side_effects': 'May cause mild gastrointestinal discomfort in sensitive individuals.',
                            'additional_uses': 'Used in herbal decorations, poultices, and traditional remedies.'
                        },
            'Adhul Sa': {
                            'properties': 'Anti-inflammatory, antibacterial, and expectorant properties.',
                            'uses': 'Used for treating cough, cold, asthma, and respiratory disorders.',
                            'nutritional_benefits': 'Rich in essential oils, flavonoids, and vitamins A and C.',
                            'side_effects': 'May cause mild irritation or allergies in some individuals.',
                            'additional_uses': 'Used in traditional medicines, teas, and as a remedy for throat infections.'
                        },
            'Tiki': {
                            'properties': 'Antibacterial, antifungal, and rich in bioactive compounds.',
                            'uses': 'Used for healing wounds, treating skin infections, and improving immunity.',
                            'nutritional_benefits': 'Contains antioxidants, tannins, and essential minerals.',
                            'side_effects': 'Overuse may cause minor skin irritation in sensitive individuals.',
                            'additional_uses': 'Used in poultices, herbal medicines, and natural remedies for skin health.'
                        },
            'Apata': {
                            'properties': 'Antimicrobial, anti-inflammatory, and diuretic properties.',
                            'uses': 'Used for treating urinary infections, skin issues, and reducing fever.',
                            'nutritional_benefits': 'Rich in micronutrients, vitamins, and essential minerals.',
                            'side_effects': 'May cause mild stomach upset if consumed in excess.',
                            'additional_uses': 'Used in traditional medicine for detoxification and as a herbal tea ingredient.'
                        }

        }

    def preprocess_image(self, img_path):
        img_ = cv2.imread(img_path)
        img_ = cv2.resize(img_, (256, 256))
        img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
        img_array = np.array(img_)
        img_array = img_array.reshape(1, 256, 256, 3)
        return img_array

    def predict_image(self):
        try:
            # labels = ["Holy Basil","Chilly","Water Hyssop","Papaya",
            #           "Peppermint","Five-leaved Chaste Tree","Vida",
            #           "Hibiscus","Neem","Bitter Gourd","Lemon","Roselle"
            #           ,"Curry Leaves","Guava","Tea","Marigold","Adhul Sa"
            #           ,"White Fig","Taro","Tiki","Apata","Turmeric",
            #           "Aloe Vera","Cluster Fig","Coriander","Linden"
            #           ,"Java Plum"]
            labels = ['Neem', 'Lemon', 'Java Plum', 'Guava', 'Aloe Vera', 'Tiki', 'Apata', 'Taro', 'MariGold',
                       'Turmeric', 'Papaya', 'Linden', 'Chilly', 'Bitter Gourd', 'Vida', 'Coriander', 'Curry Leaves',
                       'Holy Basil', 'White Fig', 'Adhul Sa', 'Water Hyssop', 'Cluster Fig', 'Peppermint', 'Tea', 'Roselle',
                       'Hibiscus', 'Five-leaved Chaste Tree']
            img_path = filedialog.askopenfilename()
            if not img_path:
                return

            processed_image = self.preprocess_image(img_path)
            prediction = self.model.predict(processed_image)
            i = prediction.argmax()
            predicted_label = labels[i]

            # Update the output label with the predicted leaf name
            self.output_label.config(text=f"{predicted_label}")

            # Display the medicinal information for the predicted label
            medicinal_info = self.medicinal_uses.get(predicted_label, {})
            info_text = (
                f"Properties: {medicinal_info.get('properties', 'N/A')}\n\n"
                f"Uses: {medicinal_info.get('uses', 'N/A')}\n\n"
                f"Nutritional Benefits: {medicinal_info.get('nutritional_benefits', 'N/A')}\n\n"
                f"Side Effects: {medicinal_info.get('side_effects', 'N/A')}\n\n"
                f"Additional Uses: {medicinal_info.get('additional_uses', 'N/A')}"
            )
            self.info_label.config(text=info_text)

            # Display the selected image on the right side
            img = Image.open(img_path)
            img.thumbnail((400, 400))
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
        except Exception as es:
            messagebox.showerror("Error","Leaf not found.")

if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    root.mainloop()

