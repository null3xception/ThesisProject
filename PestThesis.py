import customtkinter as ctk
import tkinter as tk
from thefuzz import fuzz
from PIL import Image, ImageTk

# Define the symptoms for each pest
pests_symptoms = {
    "Rice Black Bug": ["Stunted Growth", "Dead Heart", "Dry Leaves", "Yellow Leaves", "Wilting"],
    "Stem Borer": ["Yellow Leaves", "Dead Heart", "Dry Leaves", "Broken Stems", "Lodging", "White Yellow Larvae"],
    "Green Leaf Hopper": ["Yellow Leaves", "Dry Leaves", "Hopper Burn", "Stunted Growth", "Lower Yields"],
    "Brown Plant Hopper": ["Stunted Growth", "Unfilled Grains", "Wilting", "Dry Leaves", "Hopper Burn"],
    "Rice Bug": ["Feeding Damage", "Unfilled Grains", "Stunted Growth", "Drying Panicles"]
}

# Define the treatment information for each pest
pests_treatment = {
    "Rice Black Bug": [
        "Fipronil - Example products: Regent®, Termidor®",
        "Imidacloprid - Example products: Admire®, Confidor®",
        "Chlorpyrifos - Example products: Lorsban®, Dursban®",
        "Buprofezin - Example products: Applaud®, Buprofezin®",
        "Thiamethoxam - Example products: Actara®, Cruiser®"
    ],
    "Stem Borer": [
        "Chlorantraniliprole - Example products: Coragen®, Ferterra®",
        "Fipronil - Example products: Regent®, Termidor®",
        "Cartap hydrochloride - Example products: Padan®, Cartap®",
        "Thiamethoxam - Example products: Actara®, Cruiser®",
        "Buprofezin - Example products: Applaud®, Buprofezin®"
    ],
    "Green Leaf Hopper": [
        "Imidacloprid - Example products: Admire®, Gaucho®",
        "Thiamethoxam - Example products: Actara®, Cruiser®",
        "Chlorpyrifos - Example products: Lorsban®, Dursban®",
        "Bifenthrin - Example products: Talstar®, Brigade®",
        "Deltamethrin - Example products: Decis®, Delta Gold®"
    ],
    "Brown Plant Hopper": [
        "Imidacloprid - Example products: Admire®, Confidor®",
        "Thiamethoxam - Example products: Actara®, Cruiser®",
        "Dinotefuran - Example products: Starkle®, Safari®",
        "Fipronil - Example products: Regent®, Termidor®",
        "Buprofezin - Example products: Applaud®, Buprofezin®"
    ],
    "Rice Bug": [
        "Lambda-cyhalothrin - Example products: Karate®, Matador®",
        "Cypermethrin - Example products: Demon®, Ammo®",
        "Bifenthrin - Example products: Talstar®, Brigade®",
        "Chlorpyrifos - Example products: Lorsban®, Dursban®",
        "Deltamethrin - Example products: Decis®, Delta Gold®"
    ]
}


# Define the match_symptoms function
def match_symptoms(input_symptoms, threshold=100):
    results = {}

    # Check similarity of input symptoms with symptoms of each pest using fuzz library
    for pest, pest_symptoms in pests_symptoms.items():
        # Check if input symptoms are within the list of symptoms for the pest
        if set(input_symptoms).issubset(pest_symptoms):
            score = fuzz.token_set_ratio(input_symptoms, pest_symptoms)
            if score >= threshold:
                results[pest] = score

    # Sort results by score in descending order
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return sorted_results

# Initialize the main window
root = ctk.CTk()
w = 1050
h = 1000
string_dimension = f'{str(w)}x{str(h)}'
root.title("Pest Symptoms Selector")
root.geometry(string_dimension)
root.config(background="#304908")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates for the Tkinter window to be centered
x_coordinate = int((screen_width / 2) - (w / 2))
y_coordinate = int((screen_height / 2) - (h / 2))

root.geometry(f"{string_dimension}+{x_coordinate-5}+{y_coordinate-40}")

title_font = ctk.CTkFont(family="Montserrat", size=50, weight="bold")
text_font = ctk.CTkFont(family="Montserrat", size=15, weight="normal")
text_font_bold = ctk.CTkFont(family="Montserrat", size=15, weight="bold")
header_font = ctk.CTkFont(family="Montserrat", size=30, weight="bold")
subheader_font = ctk.CTkFont(family="Montserrat", size=20, weight="bold")

# Initialize the list to store selected symptoms
selected_symptoms = []

# Define a function to handle checkbox state changes
def on_checkbox_change(symptom, var):
    if var.get():
        if symptom not in selected_symptoms:
            selected_symptoms.append(symptom)
    else:
        if symptom in selected_symptoms:
            selected_symptoms.remove(symptom)
    print("Selected Symptoms:", selected_symptoms)
    show_results()  # Automatically show results after checkbox change

    if not selected_symptoms:
        detail_frame.grid_remove()  # Hide the detail_frame
    else:
        detail_frame.grid()  # Show the detail_frame
        # Reset the grid
        for widget in detail_frame.winfo_children():
            widget.grid_forget()

# Function to show the results
def show_results():
    # Clear previous results
    for widget in result_frame.winfo_children():
        widget.destroy()

    input_symptoms = selected_symptoms
    matches = match_symptoms(input_symptoms)
    print(matches)

    for pest, score in matches:
        pest_frame = ctk.CTkFrame(result_frame, width=200, height=200, corner_radius=50, bg_color="#304908", fg_color="#304908")
        pest_frame.pack_propagate(False)
        pest_frame.pack(pady=10, padx=10, fill='x')

        pest_label = ctk.CTkLabel(pest_frame, text=f"{pest}", font=text_font_bold, bg_color="#304908", fg_color="#304908")
        pest_label.pack(pady=10, padx=10)

        try:
            # Load and display pest image
            image = Image.open(f"{pest.replace(' ', '_')}.png")  # Assume image files are named as pest names with underscores
            image = image.resize((200, 200))  # Resize image
            ctk_image = ctk.CTkImage(dark_image=image, size=(150, 150))

            image_button = ctk.CTkButton(pest_frame, image=ctk_image, text="", width=150, height=150,  bg_color="#304908", fg_color="#304908", hover_color="#3e5a05", command=lambda p=pest: show_pest_details(p))
            image_button.pack(pady=15, padx=15)
        except Exception as e:
            print(f"Error loading image for {pest}: {e}")

def show_pest_details(pest):
    for widget in detail_frame.winfo_children():
        widget.destroy()

    pest_label = ctk.CTkLabel(detail_frame, text=f"Recommended Treatment for: {pest}", font=header_font, wraplength=450, width=500)
    pest_label.grid(row=0, column=0, pady=(10, 50), sticky="nsew")

    treatments = pests_treatment.get(pest, ["No treatment information available."])

    # Use grid layout for treatment frames
    for idx, treatment in enumerate(treatments[:5]):  # Display up to five treatments
        treatment_frame = ctk.CTkFrame(detail_frame, width=600, corner_radius=10, fg_color="#59761c")
        treatment_frame.grid(row=idx + 1, column=0, padx=5, pady=20, sticky="w")
        treatment_frame.grid_propagate(False)  # Prevent the frame from resizing based on its contents

        treatment_label = ctk.CTkLabel(treatment_frame, text=treatment, font=subheader_font, wraplength=450, width=500, justify="center")
        treatment_label.pack(pady=5, padx=5)
        treatment_label.pack_propagate(False)



# List of symptoms to create checkboxes for
symptoms = ["Stunted Growth", "Dead Heart", "Dry Leaves", "Yellow Leaves", "Wilting", 
            "Broken Stems", "Lodging", "White Yellow Larvae", "Hopper Burn", "Lower Yields", 
            "Unfilled Grains", "Feeding Damage", "Drying Panicles"]

title = ctk.CTkLabel(root, text="Fuzzy Pest", font=title_font, fg_color="transparent", bg_color="#304908", text_color="#c7d49c")
title.grid(row=0, column=0, columnspan=2, pady=3, padx=10, sticky=ctk.SW)
# Create checkboxes for each symptom and place them in the grid
row = 1
for symptom in symptoms:
    var = tk.BooleanVar()
    checkbox = ctk.CTkCheckBox(root, text=symptom, variable=var, command=lambda s=symptom, v=var: on_checkbox_change(s, v), bg_color="#304908", font=text_font, 
                               hover_color="#789b1d", text_color="#c7d49c", border_color="#c7d49c", fg_color="#789b1d")
    checkbox.grid(row=row, column=0, sticky="w", padx=10, pady=24)
    row += 1


pestFrame = ctk.CTkFrame(root, fg_color="#304908", bg_color="#304908")
pestFrame.grid(row=1, column=1, columnspan=2, rowspan=len(symptoms), padx=10, pady=10, sticky=ctk.NSEW)
# Create a text widget to display results and place it in the grid
result_frame = ctk.CTkFrame(pestFrame, bg_color="#304908", fg_color="#304908")
result_frame.grid(row=0, column=1, rowspan=len(symptoms), padx=10, pady=10, sticky="nsew")

# Create a detail frame to display pest details
detail_frame = ctk.CTkFrame(root, width=600, corner_radius=10, fg_color="#304908", bg_color="#304908")
detail_frame.grid(row=1, rowspan=len(symptoms), column=3, padx=30, pady=30, sticky="nsew")
detail_frame.grid_propagate(False)

# Run the application
root.mainloop()
