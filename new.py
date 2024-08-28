import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyttsx3  # For text-to-speech functionality 

# Sample data about 100 medicinal plants
plants_data = {
    # Add your 100 plant data here...
    "Aloe Vera": {
        "description": "Aloe Vera is used for its soothing properties and is commonly used to treat skin conditions.",
        "image_path": "sih2024/aloevera.jpg"
    },
    "Tulsi (Holy Basil)": {
        "description": "Tulsi, also known as Holy Basil, is revered in Ayurvedic medicine for its adaptogenic properties.",
        "image_path": "images/tulsi.jpg"
    },
    "Neem": {
        "description": "Neem is known for its antiseptic properties and is used for detoxification and treating skin disorders.",
        "image_path": "images/neem.jpg"
    },
    "Ginger": {
        "description": "Ginger aids in digestion and helps with nausea and inflammation.",
        "image_path": "images/ginger.jpg"
    },
    "Turmeric": {
        "description": "Turmeric has anti-inflammatory and antioxidant properties, commonly used for joint pain and general health.",
        "image_path": "images/turmeric.jpg"
    },
    "Echinacea": {
        "description": "Echinacea is used to support the immune system and help prevent colds.",
        "image_path": "images/echinacea.jpg"
    },
    "Peppermint": {
        "description": "Peppermint helps with digestive issues and relieves headaches.",
        "image_path": "images/peppermint.jpg"
    },
    "Lavender": {
        "description": "Lavender is used to reduce anxiety and improve sleep quality.",
        "image_path": "images/lavender.jpg"
    },
    "Chamomile": {
        "description": "Chamomile aids in relaxation and helps with digestive issues.",
        "image_path": "images/chamomile.jpg"
    },
    "Ginseng": {
        "description": "Ginseng boosts energy and enhances cognitive function.",
        "image_path": "images/ginseng.jpg"
    },
    "Garlic": {
        "description": "Garlic supports cardiovascular health and has antimicrobial properties.",
        "image_path": "images/garlic.jpg"
    },
    "Ginkgo Biloba": {
        "description": "Ginkgo Biloba is known for improving cognitive function and circulation.",
        "image_path": "images/ginkgo_biloba.jpg"
    },
    "Cinnamon": {
        "description": "Cinnamon helps regulate blood sugar levels and has anti-inflammatory properties.",
        "image_path": "images/cinnamon.jpg"
    },
    "Milk Thistle": {
        "description": "Milk Thistle is used for liver detoxification and is an antioxidant.",
        "image_path": "images/milk_thistle.jpg"
    },
    "Saw Palmetto": {
        "description": "Saw Palmetto supports prostate health and urinary tract function.",
        "image_path": "images/saw_palmetto.jpg"
    },
    "St. John's Wort": {
        "description": "St. John's Wort is used for mood stabilization and as an antidepressant.",
        "image_path": "images/st_johns_wort.jpg"
    },
    "Dandelion": {
        "description": "Dandelion supports liver function and acts as a diuretic.",
        "image_path": "images/dandelion.jpg"
    },
    "Rosemary": {
        "description": "Rosemary enhances memory and aids digestion.",
        "image_path": "images/rosemary.jpg"
    },
    "Thyme": {
        "description": "Thyme supports respiratory health and has antimicrobial properties.",
        "image_path": "images/thyme.jpg"
    },
    "Fennel": {
        "description": "Fennel helps with digestive issues and has anti-inflammatory effects.",
        "image_path": "images/fennel.jpg"
    },
    "Elderberry": {
        "description": "Elderberry boosts the immune system and provides relief from colds and flu.",
        "image_path": "images/elderberry.jpg"
    },
    "Yarrow": {
        "description": "Yarrow aids in wound healing and has anti-inflammatory properties.",
        "image_path": "images/yarrow.jpg"
    },
    "Ashwagandha": {
        "description": "Ashwagandha helps reduce stress and boosts energy.",
        "image_path": "images/ashwagandha.jpg"
    },
    "Moringa": {
        "description": "Moringa is nutrient-rich and acts as an antioxidant.",
        "image_path": "images/moringa.jpg"
    },
    "Hawthorn": {
        "description": "Hawthorn supports heart health and improves circulation.",
        "image_path": "images/hawthorn.jpg"
    },
    "Hibiscus": {
        "description": "Hibiscus helps regulate blood pressure and has antioxidant properties.",
        "image_path": "images/hibiscus.jpg"
    },
    "Licorice Root": {
        "description": "Licorice Root supports respiratory health and aids digestion.",
        "image_path": "images/licorice_root.jpg"
    },
    "Black Cohosh": {
        "description": "Black Cohosh supports menstrual health and alleviates menopause symptoms.",
        "image_path": "images/black_cohosh.jpg"
    },
    "Cayenne Pepper": {
        "description": "Cayenne Pepper provides pain relief and boosts metabolism.",
        "image_path": "images/cayenne_pepper.jpg"
    },
    "Valerian Root": {
        "description": "Valerian Root helps with sleep disorders and reduces anxiety.",
        "image_path": "images/valerian_root.jpg"
    },
    "Sage": {
        "description": "Sage supports cognitive function and aids digestion.",
        "image_path": "images/sage.jpg"
    },
    "Oregano": {
        "description": "Oregano has antimicrobial properties and supports digestive health.",
        "image_path": "images/oregano.jpg"
    },
    "Catnip": {
        "description": "Catnip helps with digestive issues and acts as a mild sedative.",
        "image_path": "images/catnip.jpg"
    },
    "Marshmallow Root": {
        "description": "Marshmallow Root soothes mucus membranes and aids digestion.",
        "image_path": "images/marshmallow_root.jpg"
    },
    "Jasmine": {
        "description": "Jasmine helps reduce stress and enhances mood.",
        "image_path": "images/jasmine.jpg"
    },
    "Passionflower": {
        "description": "Passionflower reduces anxiety and aids in sleep.",
        "image_path": "images/passionflower.jpg"
    },
    "Basil": {
        "description": "Basil supports digestive health and has anti-inflammatory effects.",
        "image_path": "images/basil.jpg"
    },
    "Beetroot": {
        "description": "Beetroot supports blood health and aids in detoxification.",
        "image_path": "images/beetroot.jpg"
    },
    "Barberry": {
        "description": "Barberry supports liver health and aids digestion.",
        "image_path": "images/barberry.jpg"
    },
    "Celery Seed": {
        "description": "Celery Seed supports joint health and acts as a diuretic.",
        "image_path": "images/celery_seed.jpg"
    },
    "Chili Pepper": {
        "description": "Chili Pepper provides pain relief and boosts metabolism.",
        "image_path": "images/chili_pepper.jpg"
    },
    "Coltsfoot": {
        "description": "Coltsfoot supports respiratory health and relieves coughs.",
        "image_path": "images/coltsfoot.jpg"
    },
    "Creeping Charlie": {
        "description": "Creeping Charlie supports respiratory health and has anti-inflammatory effects.",
        "image_path": "images/creeping_charlie.jpg"
    },
    "Horsetail": {
        "description": "Horsetail supports urinary tract health and bone health.",
        "image_path": "images/horsetail.jpg"
    },
    "Kava": {
        "description": "Kava helps with anxiety relief and muscle relaxation.",
        "image_path": "images/kava.jpg"
    },
    "Mistletoe": {
        "description": "Mistletoe supports blood pressure regulation and boosts the immune system.",
        "image_path": "images/mistletoe.jpg"
    },
    "Nettle": {
        "description": "Nettle provides allergy relief and is nutrient-rich.",
        "image_path": "images/nettle.jpg"
    },
    "Oat Straw": {
        "description": "Oat Straw supports the nervous system and bone health.",
        "image_path": "images/oat_straw.jpg"
    },
    "Psyllium": {
        "description": "Psyllium supports digestive health and provides fiber.",
        "image_path": "images/psyllium.jpg"
    },
    "Raspberry Leaf": {
        "description": "Raspberry Leaf supports women's health and relieves menstrual symptoms.",
        "image_path": "images/raspberry_leaf.jpg"
    },
    "Schisandra": {
        "description": "Schisandra acts as an adaptogen and supports liver function.",
        "image_path": "images/schisandra.jpg"
    },
    "Slippery Elm": {
        "description": "Slippery Elm soothes digestive issues and the throat.",
        "image_path": "images/slippery_elm.jpg"
    },
    "Astragalus": {
        "description": "Astragalus boosts the immune system and provides energy.",
        "image_path": "images/astragalus.jpg"
    },
    "Burdock Root": {
        "description": "Burdock Root supports detoxification and skin health.",
        "image_path": "images/burdock_root.jpg"
    },
    "Cardamom": {
        "description": "Cardamom aids digestion and supports respiratory health.",
        "image_path": "images/cardamom.jpg"
    },
    "Chicory": {
        "description": "Chicory supports liver health and aids digestion.",
        "image_path": "images/chicory.jpg"
    },
    "Cilantro": {
        "description": "Cilantro supports detoxification and digestive health.",
        "image_path": "images/cilantro.jpg"
    },
    "Dill": {
        "description": "Dill aids in digestion and has anti-inflammatory properties.",
        "image_path": "images/dill.jpg"
    },
    "Elderflower": {
        "description": "Elderflower supports respiratory health and boosts the immune system.",
        "image_path": "images/elderflower.jpg"
    },
    "Feverfew": {
        "description": "Feverfew helps with migraine relief and has anti-inflammatory effects.",
        "image_path": "images/feverfew.jpg"
    },
    "Gotu Kola": {
        "description": "Gotu Kola supports cognitive function and aids in wound healing.",
        "image_path": "images/gotu_kola.jpg"
    },
    "Lemongrass": {
        "description": "Lemongrass supports digestive health and has anti-inflammatory effects.",
        "image_path": "images/lemongrass.jpg"
    },
    "Mango Ginger": {
        "description": "Mango Ginger aids in digestion and has anti-inflammatory properties.",
        "image_path": "images/mango_ginger.jpg"
    },
    "Rhubarb": {
        "description": "Rhubarb supports digestive health and aids in detoxification.",
        "image_path": "images/rhubarb.jpg"
    },
    "Sarsaparilla": {
        "description": "Sarsaparilla supports detoxification and skin health.",
        "image_path": "images/sarsaparilla.jpg"
    },
    "Shatavari": {
        "description": "Shatavari supports women's health and reproductive function.",
        "image_path": "images/shatavari.jpg"
    },
    "Suma Root": {
        "description": "Suma Root acts as an adaptogen and boosts energy.",
        "image_path": "images/suma_root.jpg"
    },
    "Sweet Woodruff": {
        "description": "Sweet Woodruff aids in digestion and has anti-inflammatory effects.",
        "image_path": "images/sweet_woodruff.jpg"
    },
    "Witch Hazel": {
        "description": "Witch Hazel supports skin health and has anti-inflammatory properties.",
        "image_path": "images/witch_hazel.jpg"
    },
    "Ylang-Ylang": {
        "description": "Ylang-Ylang helps reduce stress and enhances mood.",
        "image_path": "images/ylang_ylang.jpg"
    },
    "Alfalfa": {
        "description": "Alfalfa is nutrient-rich and supports detoxification.",
        "image_path": "images/alfalfa.jpg"
    },
    "Arnica": {
        "description": "Arnica provides pain relief and helps with bruising.",
        "image_path": "images/arnica.jpg"
    },
    "Bee Balm": {
        "description": "Bee Balm has antimicrobial properties and supports respiratory health.",
        "image_path": "images/bee_balm.jpg"
    },
    "Borage": {
        "description": "Borage supports skin health and has anti-inflammatory effects.",
        "image_path": "images/borage.jpg"
    },
    "Cranberry": {
        "description": "Cranberry supports urinary tract health and has antioxidant properties.",
        "image_path": "images/cranberry.jpg"
    },
    "Flaxseed": {
        "description": "Flaxseed supports digestive health and heart health.",
        "image_path": "images/flaxseed.jpg"
    },
    "Goldenseal": {
        "description": "Goldenseal boosts the immune system and aids in digestion.",
        "image_path": "images/goldenseal.jpg"
    },
    "Juniper": {
        "description": "Juniper supports urinary tract health and detoxification.",
        "image_path": "images/juniper.jpg"
    },
    "Knotweed": {
        "description": "Knotweed supports blood pressure regulation and has antioxidant properties.",
        "image_path": "images/knotweed.jpg"
    },
    "Motherwort": {
        "description": "Motherwort supports women's health and cardiovascular health.",
        "image_path": "images/motherwort.jpg"
    },
    "Noni": {
        "description": "Noni boosts the immune system and acts as an antioxidant.",
        "image_path": "images/noni.jpg"
    },
    "Oregano": {
        "description": "Oregano has antimicrobial properties and supports digestive health.",
        "image_path": "images/oregano.jpg"
    },
    "Peppermint": {
        "description": "Peppermint helps with digestive issues and relieves headaches.",
        "image_path": "images/peppermint.jpg"
    },
    "Red Clover": {
        "description": "Red Clover supports menstrual health and skin health.",
        "image_path": "images/red_clover.jpg"
    },
    "Saw Palmetto": {
        "description": "Saw Palmetto supports prostate health and urinary tract function.",
        "image_path": "images/saw_palmetto.jpg"
    },
    "Tea Tree": {
        "description": "Tea Tree oil has antimicrobial properties and supports skin health.",
        "image_path": "images/tea_tree.jpg"
    },
    "Valerian Root": {
        "description": "Valerian Root helps with sleep disorders and reduces anxiety.",
        "image_path": "images/valerian_root.jpg"
    },
    "Wormwood": {
        "description": "Wormwood supports digestive health and acts as an antiparasitic.",
        "image_path": "images/wormwood.jpg"
    },
    "Chaste Tree": {
        "description": "Chaste Tree supports menstrual health and hormonal balance.",
        "image_path": "images/chaste_tree.jpg"
    },
    "Angelica Root": {
        "description": "Angelica Root aids digestion and supports respiratory health.",
        "image_path": "images/angelica_root.jpg"
    },
    "Baikal Skullcap": {
        "description": "Baikal Skullcap supports immune function and has anti-inflammatory properties.",
        "image_path": "images/baikal_skullcap.jpg"
    }
    # Add more plants as needed...
}

class HerbalGardenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Herbal Garden")
        
        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()

        # Create a frame for the search and plant list
        self.frame_list = tk.Frame(root)
        self.frame_list.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Create a search box
        self.search_label = tk.Label(self.frame_list, text="Search:")
        self.search_label.pack()
        
        self.search_entry = tk.Entry(self.frame_list, width=40)
        self.search_entry.pack()
        
        self.search_button = tk.Button(self.frame_list, text="Search", command=self.search_plants)
        self.search_button.pack(pady=5)
        
        # Create a listbox to display plant names
        self.plant_listbox = tk.Listbox(self.frame_list, width=40, height=20)
        self.plant_listbox.pack()
        
        # Populate the listbox with plant names
        self.update_plant_listbox()
        
        # Create a frame for the plant details
        self.frame_details = tk.Frame(root)
        self.frame_details.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Create a label to display plant image
        self.plant_image_label = tk.Label(self.frame_details)
        self.plant_image_label.pack(pady=10)
        
        # Create a text widget to display plant description
        self.plant_description_text = tk.Text(self.frame_details, wrap=tk.WORD, width=60, height=20)
        self.plant_description_text.pack()
        
        # Create a button to read out the plant description
        self.speech_button = tk.Button(self.frame_details, text="Read Description", command=self.read_description)
        self.speech_button.pack(pady=10)
        
        # Bind the listbox selection event
        self.plant_listbox.bind("<<ListboxSelect>>", self.display_plant_info)
    
    def update_plant_listbox(self):
        # Clear current items in listbox
        self.plant_listbox.delete(0, tk.END)
        # Populate the listbox with plant names
        for plant in plants_data.keys():
            self.plant_listbox.insert(tk.END, plant)
    
    def search_plants(self):
        search_term = self.search_entry.get().lower()
        self.plant_listbox.delete(0, tk.END)
        
        for plant in plants_data.keys():
            if search_term in plant.lower():
                self.plant_listbox.insert(tk.END, plant)
    
    def display_plant_info(self, event):
        # Get the selected plant name
        selected_plant = self.plant_listbox.get(self.plant_listbox.curselection())
        
        # Fetch the plant data
        plant_data = plants_data[selected_plant]
        
        # Update the plant description
        self.plant_description_text.delete(1.0, tk.END)
        self.plant_description_text.insert(tk.END, plant_data["description"])
        
        # Update the plant image
        try:
            image = Image.open(plant_data["image_path"])
            image = image.resize((300, 200), Image.ANTIALIAS)
            self.plant_image = ImageTk.PhotoImage(image)
            self.plant_image_label.config(image=self.plant_image)
            self.plant_image_label.image = self.plant_image
        except FileNotFoundError:
            self.plant_image_label.config(image='')
            self.plant_description_text.insert(tk.END, "\nImage not found.")

    def read_description(self):
        # Get the current text in the description widget
        description = self.plant_description_text.get(1.0, tk.END)
        self.tts_engine.say(description)
        self.tts_engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = HerbalGardenApp(root)
    root.mainloop()
