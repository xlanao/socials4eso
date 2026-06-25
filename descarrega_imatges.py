#!/usr/bin/env python3
"""
Executa aquest script a la carpeta del projecte.
Descarrega totes les imatges i les desa a la carpeta images/.
Després puja la carpeta images/ a GitHub juntament amb els HTML.
"""

import urllib.request
import os
import time

os.makedirs("images", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://commons.wikimedia.org/",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
}

imatges = {
    # T01 — Antic Règim
    "estaments_alegoria.jpg":   "https://upload.wikimedia.org/wikipedia/commons/thumb/5/fifty/Fotothek_df_tg_0000302_Allegorie_%5E_Gesellschaft_%5E_Stand.jpg/640px-Fotothek_df_tg_0000302_Allegorie_%5E_Gesellschaft_%5E_Stand.jpg",
    "versailles.jpg":           "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Palace_of_Versailles%2C_view_from_the_Avenue_de_Paris_2011.jpg/800px-Palace_of_Versailles%2C_view_from_the_Avenue_de_Paris_2011.jpg",
    "encyclopedie.jpg":         "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Encyclopedie_de_D%27Alembert_et_Diderot_-_Premiere_Page_-_ENC_1-NA5.jpg/543px-Encyclopedie_de_D%27Alembert_et_Diderot_-_Premiere_Page_-_ENC_1-NA5.jpg",
    "triangular_trade.png":     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Triangular_trade.png/800px-Triangular_trade.png",
    "slave_ship.jpg":           "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Slaveshipposter.jpg/800px-Slaveshipposter.jpg",
    "bastilla.jpg":             "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Prise_de_la_Bastille.jpg/800px-Prise_de_la_Bastille.jpg",
    "declaracio_drets.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Declaracion_de_los_Derechos_del_Hombre.jpg/387px-Declaracion_de_los_Derechos_del_Hombre.jpg",
    "guillotina.jpg":           "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Execution_of_Louis_XVI.jpg/800px-Execution_of_Louis_XVI.jpg",
    "napoleon.jpg":             "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project_2.jpg/595px-Jacques-Louis_David_-_The_Emperor_Napoleon_in_His_Study_at_the_Tuileries_-_Google_Art_Project_2.jpg",

    # T02 — Revolució Industrial
    "watt_steam.jpg":           "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Maquina_vapor_Watt_ETSIIM.jpg/479px-Maquina_vapor_Watt_ETSIIM.jpg",
    "rocket_stephenson.jpg":    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Stephenson_Rocket.jpg/800px-Stephenson_Rocket.jpg",
    "child_labor_mine.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Child_labor_in_coal_mine.jpg/800px-Child_labor_in_coal_mine.jpg",
    "karl_marx.jpg":            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Karl_Marx_001.jpg/532px-Karl_Marx_001.jpg",

    # T03 — Imperialisme
    "benz_motorwagen.jpg":      "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/BenzPatentMotorwagen1885.jpg/800px-BenzPatentMotorwagen1885.jpg",
    "ford_assembly.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/A_line_of_Model_T_Fords.jpg/800px-A_line_of_Model_T_Fords.jpg",
    "africa_scramble.gif":      "https://upload.wikimedia.org/wikipedia/commons/6/62/Scramble_for_Africa_1880_to_1913.gif",
    "congo_mutilation.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Congomutilation.jpg/400px-Congomutilation.jpg",
    "opium_war.jpg":            "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/British_vessels_on_the_Canton_river.jpg/800px-British_vessels_on_the_Canton_river.jpg",

    # T04 — Primera Guerra Mundial
    "europe_1914.jpg":          "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Europe_1914.jpg/800px-Europe_1914.jpg",
    "alliances_1914.png":       "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Map_Europe_alliances_1914-en.svg/800px-Map_Europe_alliances_1914-en.svg.png",
    "sarajevo_1914.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Sarajevo_assassination_sites.jpg/640px-Sarajevo_assassination_sites.jpg",
    "western_front.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Western_front_1917b.jpg/800px-Western_front_1917b.jpg",
    "trenches_somme.jpg":       "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Cheshire_Regiment_trench_Somme_1916_%28higher_res%29.png/640px-Cheshire_Regiment_trench_Somme_1916_%28higher_res%29.png",
    "kitchener_poster.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kitchener-poster.jpg/399px-Kitchener-poster.jpg",
    "europe_1923.png":          "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Europe_1923_map_en.png/800px-Europe_1923_map_en.png",
}

for nom, url in imatges.items():
    dest = os.path.join("images", nom)
    if os.path.exists(dest) and os.path.getsize(dest) > 5000:
        print(f"  ja existeix: {nom}")
        continue
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        print(f"  OK ({len(data)//1024}KB): {nom}")
    except Exception as e:
        print(f"  ERROR {nom}: {e}")
    time.sleep(0.5)

print("\nFet! Ara puja la carpeta images/ a GitHub.")
