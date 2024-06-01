import customtkinter as ctk
import tkinter as tk
from thefuzz import fuzz
from PIL import Image, ImageTk
from custom_hovertip import CustomTooltipLabel
from tkinter import PhotoImage

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


def match_symptoms(input_symptoms, threshold=100):
    results = {}

    # Check similarity of input symptoms with symptoms of each pest using fuzz library
    for pest, pest_symptoms in pests_symptoms.items():
        # Check if input symptoms are a subset of the pest symptoms
        if set(input_symptoms).issubset(pest_symptoms):
            score = fuzz.token_set_ratio(input_symptoms, pest_symptoms)
            if score >= threshold:
                results[pest] = score

    # If no exact match found, check for partial matches
    if not results:
        for pest, pest_symptoms in pests_symptoms.items():
            score = fuzz.token_set_ratio(input_symptoms, pest_symptoms)
            if score >= threshold:
                results[pest] = score

    # Sort results by score in descending order
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return sorted_results


# Initialize the main window
root = ctk.CTk()
w = 1600
h = 900
string_dimension = f'{str(w)}x{str(h)}'
root.title("FuzzPest")
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
label_font = ctk.CTkFont(family="Montserrat", size=20, weight="normal")

landingpageBG = ctk.CTkImage(light_image=Image.open("fuzzpestbg.jpg"),
                    dark_image=Image.open("fuzzpestbg.jpg"),
                    size=(1600, 900))

landingpageBGWidget = ctk.CTkLabel(root, image=landingpageBG, text="")
landingpageBGWidget.place(x=0, y=0, relwidth=1, relheight=1)


def showMainPage():
    mainPageWindow =  ctk.CTkToplevel(root)
    mainPageWindow.title("FuzzPest")
    mainPageWindow.geometry(string_dimension)
    mainPageWindow.geometry(f"{string_dimension}+{x_coordinate-5}+{y_coordinate-40}")
    mainPageWindow.config(background="#304908")
    mainPageWindow.resizable(False, False)
    root.withdraw()

    def on_close():
        mainPageWindow.destroy()
        root.deiconify()  
    
    mainPageWindow.protocol("WM_DELETE_WINDOW", on_close)


    mainPageLogo = ctk.CTkImage(light_image=Image.open("fuzzpestlogo.png"),
                    dark_image=Image.open("fuzzpestlogo.png"),
                    size=(100, 100))
    mainPageLogoWidget = ctk.CTkButton(mainPageWindow, image=mainPageLogo, text="", hover_color="#59761c", fg_color="#304908", bg_color="#304908", command=on_close)
    mainPageLogoWidget.grid(row=0, column=0, columnspan=2, pady=10, padx=10 ,sticky=ctk.W)

    mainPagetitle = ctk.CTkLabel(mainPageWindow, text="FuzzPest", font=title_font, fg_color="#304908", bg_color="#304908", text_color="#c7d49c")
    mainPagetitle.grid(row=0, column=0, columnspan=7, padx=(150,10), sticky=ctk.W)

    mainPageHelpButton = ctk.CTkButton(mainPageWindow, text="?", border_width=2, fg_color="#304908", bg_color="#304908", border_color="#c7d49c", font=subheader_font, 
                                        hover_color="#789b1d", width=30, height=30, corner_radius=30)
    mainPageHelpButton.grid(row=0, column=7, pady=10, padx=10 ,sticky=ctk.E)

    #------------------SYMPTOMS SECTION ---------------------------------------------

    # Define symptom descriptions
    symptom_descriptions = {
        "Stunted Growth": "Stunted growth in rice fields refers to a condition where rice plants exhibit reduced or slowed growth, resulting in shorter \nand less robust plants compared to healthy ones. This condition can significantly impact rice yields and quality.",
        "Dead Heart": "Deadheart is a term used in rice farming to describe a condition where the central shoot of a young rice plant dies prematurely, \nleaving behind a brown or dead appearance at the center of the plant.",
        "Dry Leaves": "Dry leaves in rice fields typically refer to the condition where the leaves of rice plants lose moisture, \nbecome brittle, and turn brown or yellowish, resembling dry or dead foliage.",
        "Yellow Leaves": "Yellow leaves it typically indicates a situation where a plant's leaves are turning yellow due to an infestation of pests.",
        "Wilting": "Wilting in seedlings, the leaves dry out and wilt, a syndrome known as kresek. \nInfected seedlings usually are killed by bacterial blight within two to three weeks of being infected",
        "Broken Stems": "Broken stems stems are easily broken and usually mixed with the grains.",
        "Lodging": "Lodging Rice plants \nthat lean excessively or \nfall over are said to be lodged.",
        "White Yellow Larvae": "White yellow larvae the adult is white and slender and resembles the yellow stem borer, \nbut it does not have a black spot on the forewing.",
        "Hopper Burn": "Hopper burn in rice refers to a condition where the edges of rice leaves become scorched or burnt, \ntypically starting from the leaf tips and progressing towards the base.  ",
        "Lower Yields": "Lower yields in rice refer to the reduced quantity of rice \nproduced per unit area of cultivation compared to expected or desired levels.",
        "Unfilled Grains": "Unfilled grains also known as chalky or immature grains, \nare grains that fail to fill completely during the grain-filling stage of rice development",
        "Feeding Damage": "Feeding Damage refers to the physical harm inflicted on \nrice plants by various pests during their feeding activities.",
        "Drying Panicles": "Drying of Panicles, the panicles \nare tied in bundles and placed on pavements \nor mats or hung from frames. \nThere is uneven drying because the grains \n on the outside dry faster than the grains on the inside."
    }

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
        showResults()

    def showResults():
        input_symptoms = selected_symptoms
        if not input_symptoms:
            for widget in detail_frame.grid_slaves():
                widget.destroy()
            for pest_name in pest_buttons:
                disable_pest_buttons(pest_name)
            return
        matches = match_symptoms(input_symptoms)
        for pest_name, button in pest_buttons.items():
            if any(pest_name in match for match in matches):
                button.configure(state="normal", fg_color="#59761c", hover_color="#789b1d")
                button.bind("<Button-1>", lambda event, pest_name=pest_name: on_pest_button_click(pest_name))
            else:
                button.configure(state="disabled", fg_color="#b4496b")

    symptoms_row1 = ["Stunted Growth", "Dead Heart", "Dry Leaves", "Yellow Leaves", "Wilting", 
                "Broken Stems", "Lodging"]
    symptoms_row2 = ["White Yellow Larvae", "Hopper Burn", "Lower Yields", 
                "Unfilled Grains", "Feeding Damage", "Drying Panicles"]
    
    mainPageWindow.grid_columnconfigure(0, weight=1)
    mainPageWindow.grid_columnconfigure(8, weight=1)

    label = ctk.CTkLabel(mainPageWindow, text="Select Symptoms Below:", font=subheader_font, fg_color="#304908", bg_color="#304908", text_color="#c7d49c")
    label.grid(row=1, column=2, columnspan=4, padx=100, pady=10, sticky="ew")

    # Create checkboxes for symptoms row 1
    column = 1
    for symptom in symptoms_row1:
        var = tk.BooleanVar()
        var.trace("w", lambda name, index, mode, var=var, symptom=symptom: on_checkbox_change(symptom, var))
        checkbox = ctk.CTkCheckBox(mainPageWindow, text=symptom, variable=var, bg_color="#304908", font=text_font, 
                                    hover_color="#789b1d", text_color="#c7d49c", border_color="#c7d49c", fg_color="#789b1d")
        checkbox.grid(row=2, column=column, sticky="w", padx=(20, 20), pady=20)
        tooltip_text = symptom_descriptions.get(symptom, "No description available")
        tooltip = CustomTooltipLabel(anchor_widget=checkbox, text=tooltip_text, foreground="#c7d49c", background="#59761c", font=text_font, justify="left")
        column += 1

    # Create checkboxes for symptoms row 2
    column = 1
    for symptom in symptoms_row2:
        var = tk.BooleanVar()
        var.trace("w", lambda name, index, mode, var=var, symptom=symptom: on_checkbox_change(symptom, var))
        checkbox = ctk.CTkCheckBox(mainPageWindow, text=symptom, variable=var, bg_color="#304908", font=text_font, 
                                    hover_color="#789b1d", text_color="#c7d49c", border_color="#c7d49c", fg_color="#789b1d")
        checkbox.grid(row=3, column=column, sticky="w", padx=(80, 10), pady=20)
        tooltip_text = symptom_descriptions.get(symptom, "No description available")
        tooltip = CustomTooltipLabel(anchor_widget=checkbox, text=tooltip_text, foreground="#c7d49c", background="#59761c", font=text_font, justify="left")
        column += 1

    #----------------------- PEST SECTION ----------------------------------------------
    pest_images = [
        ("Brown_Plant_Hopper.png", "Brown Plant Hopper"),
        ("Green_Leaf_Hopper.png", "Green Leaf Hopper"),
        ("Rice_Black_Bug.png", "Rice Black Bug"),
        ("Rice_Bug.png", "Rice Bug"),
        ("Stem_Borer.png", "Stem Borer")
    ]

    pest_descriptions = {
        "Brown Plant Hopper": "Brown plant hoppers are insects that feed on plant sap, \ncausing damage to crops such as rice and sugarcane. \nThey are typically brown in color and hop around plants.",
        "Green Leaf Hopper": "Green leaf hoppers are small insects that feed on plant sap \nby piercing plant tissues. They are often green in color \nand can cause damage to a variety of crops, \nincluding rice, corn, and vegetables.",
        "Rice Black Bug": "Rice black bugs are pests that feed on rice plants by sucking \nsap from the stems and grains. They are small, \nblack insects that can cause significant yield losses in rice crops.",
        "Rice Bug": "Rice bugs are pests of rice crops that feed on the grains, \ncausing damage and reducing the quality of the rice. \nThey are typically brown or reddish-brown in color and can \nbe a problem in rice-growing regions.",
        "Stem Borer": "Stem borers are moth larvae that bore into the stems of plants, \nincluding rice, corn, and sugarcane. They can cause wilting, \nstunting, and lodging of the affected plants, \nleading to yield losses."
    }
        

    pest_frames = []
    pest_buttons = {}

    for i, (image_path, pest_name) in enumerate(pest_images):
        # Load the original image
        original_image = Image.open(image_path)

        # Resize the image to fit the button
        button_size = (150, 150)  # Set the desired button size
        resized_image = original_image.resize(button_size)

        # Convert the resized image to PhotoImage
        image = ImageTk.PhotoImage(resized_image)

        # Create a frame to contain the image
        frame = ctk.CTkFrame(mainPageWindow, bg_color="#b4496b", fg_color="#b4496b")
        frame.grid_propagate(False)  # Disable auto-resizing of the frame
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        # Create a button to display the image
        button = ctk.CTkButton(frame, image=image, border_width=0, bg_color="#304908", fg_color="#b4496b", compound="top", text=pest_name, font=text_font_bold, width=250, height=250, state="disabled")
        button.grid(row=0, column=0, sticky="nsew")

        # Keep a reference to the image to prevent garbage collection
        button.image = image

        # Position the frame in row 4
        frame.grid(row=4, column=i+2, padx=10, pady=30, sticky="e")

        # Add the frame to the list
        pest_frames.append(frame)

        pest_buttons[pest_name] = button

        tooltip_text = pest_descriptions.get(pest_name, "No description available")
        tooltip = CustomTooltipLabel(anchor_widget=button, text=tooltip_text, foreground="#c7d49c", background="#59761c", font=text_font, justify="left")

        #------ RECOMMENDATION SECTION -----------------------------------
        treatment_frames = []
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

        treatment_descriptions = {
            "Fipronil - Example products: Regent®, Termidor®": "WHAT?\n Fipronil: A broad-spectrum insecticide that acts through both contact and ingestion, effective against brown planthoppers.\n Example products: Regent®, Termidor®\n Regent®: Commonly used in rice and other crops, Regent® provides effective control of brown planthoppers and other pests. It can be applied as a foliar spray or soil treatment to protect plants.\n Termidor®: While primarily known for termite control, Termidor® contains fipronil and can be used for a variety of pest control applications. In agricultural settings, it can provide effective control of soil and foliar pests.",
            "Imidacloprid - Example products: Admire®, Confidor®": "WHAT?\n Imidacloprid: A neonicotinoid insecticide effective due to its systemic action, targeting the nervous system of the pests. \n Example products: Admire®, Confidor® \nAdmire®: Often used for soil and foliar applications to protect against a variety of sucking pests in crops such as rice, vegetables, and fruits.\n Confidor®: Commonly used as a foliar spray or seed treatment to protect crops from early-stage pest infestations.\n WHY?\n Admire® and Confidor® are recommended for brown planthopper control because they provide effective, long-lasting, and broad-spectrum pest management while being safer for non-target organisms and the environment when used according to guidelines. ",
            "Chlorpyrifos - Example products: Lorsban®, Dursban®": "Chlorpyrifos: An organophosphate insecticide used to manage a wide range of pests, including rice bugs.\n •	Example products: Lorsban®, Dursban®\n o	Lorsban®: Lorsban® is one of the well-known brand names for insecticides containing chlorpyrifos. It has been used to control a wide range of insect pests in various crops, including rice, fruits, vegetables, and cotton.\n Dursban®: Dursban® was another prominent brand name for insecticides containing chlorpyrifos. Like Lorsban®, it was used for pest control in agriculture as well as in residential and commercial settings.",
            "Buprofezin - Example products: Applaud®, Buprofezin®": "WHAT?\n Buprofezin: An insect growth regulator that disrupts the molting process, targeting nymph stages of brown planthoppers.\n •	Example products: Applaud®, Buprofezin®\n Applaud®: Often used as a foliar spray, Applaud® is effective in controlling nymph stages of brown planthoppers and other pests. It can be applied to a variety of crops, including rice, vegetables, and fruit trees.\n Buprofezin®: This product is used similarly to Applaud®, targeting immature stages of pests and providing long-lasting residual control. It is suitable for use in a wide range of crops.",
            "Thiamethoxam - Example products: Actara®, Cruiser®": "Thiamethoxam, a neonicotinoid insecticide, is effective against sucking insects such as brown planthoppers. Actara® and Cruiser® are example products containing thiamethoxam. Actara® is a foliar spray for crops like rice, while Cruiser® is a seed treatment, both providing rapid pest control. They are recommended for brown planthopper management due to their systemic action, rapid knockdown, and long-lasting control, with low toxicity and compatibility with Integrated Pest Management (IPM) programs.",
            "Chlorantraniliprole - Example products: Coragen®, Ferterra®": "Description of Chlorantraniliprole treatment...",
            "Cartap hydrochloride - Example products: Padan®, Cartap®": "Description of Cartap hydrochloride treatment...",
            "Dinotefuran - Example products: Starkle®, Safari®": "WHAT?\n Dinotefuran: Known for its rapid action, this neonicotinoid is highly effective against brown planthoppers.\n •	Example products: Starkle®, Safari®\n Starkle®: Often used as a granular or foliar application to control a variety of pests in crops like rice, vegetables, and fruits. It provides systemic protection and rapid control of pest populations.\n Safari®: Commonly used for ornamental plants, landscape plants, and crops. It is effective in controlling a range of pests and can be applied as a foliar spray, soil drench, or trunk injection.\n ",
            "Lambda-cyhalothrin - Example products: Karate®, Matador®": "Lambda-cyhalothrin is a synthetic pyrethroid pesticide known for its effectiveness against various pests, including rice bugs like the Brown Planthopper, Rice Bug, Rice Black Bug, Green Leafhopper, and White/Yellow Stem Borer. Example products containing lambda-cyhalothrin include Karate® and Matador®, both used for foliar applications in rice and other crops. These products provide rapid knockdown and residual activity, offering broad-spectrum control and extended protection against pests.",
            "Cypermethrin - Example products: Demon®, Ammo®": "Cypermethrin is another synthetic pyrethroid pesticide effective against rice bugs and other insect pests. Example products containing cypermethrin include Demon® and Ammo®. These products provide effective control against pests such as the Brown Planthopper, Rice Bug, Rice Black Bug, Green Leafhopper, and White/Yellow Stem Borer. Demon® and Ammo® are commonly used as foliar applications in crops like rice, known for their rapid knockdown and long-lasting residual effects, offering broad-spectrum control and extended protection against pests.",
            "Bifenthrin - Example products: Talstar®, Brigade®": "Bifenthrin is a pyrethroid insecticide effective in controlling various agricultural pests, including rice bugs. Example products containing bifenthrin include Talstar® and Brigade®. These products provide effective control against pests such as the Brown Planthopper, Rice Bug, Rice Black Bug, Green Leafhopper, and White/Yellow Stem Borer. Talstar® and Brigade® are commonly used as foliar applications in crops like rice, known for their rapid knockdown and long-lasting residual effects, offering broad-spectrum control and extended protection against pests.",
            "Deltamethrin - Example products: Decis®, Delta Gold®": "Deltamethrin: A pyrethroid insecticide that works well against many pests, including rice bugs.\n •	Example products: Decis®, Delta Gold®\n Decis®: Decis® is one of the most widely recognized brand names for insecticides containing deltamethrin. It is available in formulations such as emulsifiable concentrate (EC), suspension concentrate (SC), and wettable powder (WP), and is used for the control of pests in various crops, including vegetables, fruits, cereals, and cotton.\n Delta Gold®: Delta Gold® is another brand name for insecticides containing deltamethrin. It is available in formulations such as emulsifiable concentrate (EC) and suspension concentrate (SC), and is used for the control of a wide range of pests in crops like cotton, soybeans, corn, and vegetables."
        }

        def show_pest_details(pest):
            # Add pest label
            pest_label = ctk.CTkLabel(detail_frame, text=f"Recommended Treatment for: {pest}", font=header_font, wraplength=450, width=500)
            pest_label.grid(row=1, column=1, columnspan=3, pady=(10, 20), sticky="nsew")

            treatments = pests_treatment.get(pest, ["No treatment information available."])

            def show_popup(treatment):
                description = treatment_descriptions.get(treatment, "No description available")
                if description == "No description available":
                    return  # Don't show popup if no description is available
                
                popup_window = ctk.CTkToplevel()
                popup_window.title("Treatment Details")

                # Set the size of the popup window
                popup_window.geometry("800x600")
                popup_window.config(background="#304908")
        
                popup_label = ctk.CTkLabel(popup_window, text=description, font=subheader_font, width=700, wraplength=700, fg_color="#304908")
                popup_label.pack(padx=10, pady=60)

                # Calculate the position to center the popup window
                screen_width = popup_window.winfo_screenwidth()
                screen_height = popup_window.winfo_screenheight()
                x_coordinate = (screen_width - 800) // 2
                y_coordinate = (screen_height - 600) // 2
                
                # Set the position of the popup window
                popup_window.geometry(f"+{x_coordinate}+{y_coordinate}")
                
                # Bring the popup window to the front and keep it in front
                popup_window.lift()
                popup_window.grab_set()

            # Use grid layout for treatment frames
            for idx, treatment in enumerate(treatments[:5]):  # Display up to five treatments
                row_position = 2 if idx < 3 else 3
                column_position = idx if idx < 3 else idx - 3

                treatment_frame = ctk.CTkFrame(detail_frame, width=1600, corner_radius=10, fg_color="#59761c")
                treatment_frame.grid(row=row_position, column=column_position + 1, padx=5, pady=10, sticky="nsew")
                treatment_frame.grid_propagate(False)  # Prevent the frame from resizing based on its contents

                treatment_label = ctk.CTkLabel(treatment_frame, text=treatment, font=subheader_font, wraplength=450, width=500, justify="center")
                treatment_label.pack(pady=5, padx=5)
                treatment_label.pack_propagate(False)

                def on_frame_click(event, treatment):
                    print(f"Treatment clicked: {treatment}")
                    show_popup(treatment)

                # Bind click event to treatment frame
                treatment_label.bind("<Button-1>", lambda event, treatment=treatment: on_frame_click(event, treatment))
            
               # Adjust column weights to center rows
            for col in range(5):
                detail_frame.columnconfigure(col, weight=1)


        def disable_pest_buttons(pest_name):
            button = pest_buttons.get(pest_name)
            if button:
                button.configure(state="disabled", fg_color="#b4496b")
                button.unbind("<Button-1>")

        def on_pest_button_click(pest_name):
            show_pest_details(pest_name)

        # Example setup for the detail frame
        detail_frame = ctk.CTkFrame(mainPageWindow, width=1600, height=325, corner_radius=10, fg_color="#304908")
        detail_frame.grid(row=8, column=0, columnspan=10, padx=10, pady=10, sticky="nsew")



landingpageButton = ctk.CTkButton(root, width=50, height=50, corner_radius=30, 
                                border_width=2, fg_color="#385319", bg_color="#3e5a05", 
                                border_color="#c7d49c", text="Start Identifying", font=subheader_font, hover_color="#789b1d",
                                command=showMainPage)


landingpageButton.pack(pady=(812,30), padx=(50))
# Run the application
root.resizable(False, False)
root.mainloop()