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

       #All details about medicinal leaves

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

