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

    # Imatges noves T03
    "livingstone.jpg":         "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/David_Livingstone_-_Project_Gutenberg_eText_13262.jpg/400px-David_Livingstone_-_Project_Gutenberg_eText_13262.jpg",
    "berlin_conference.jpg":   "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Konferenz_von_Berlin_1884-85-2.jpg/800px-Konferenz_von_Berlin_1884-85-2.jpg",
    "africa_1880.jpg":         "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Colonisation_1800.png/800px-Colonisation_1800.png",
    "boer_war_camp.jpg":       "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/BoerWomen.jpg/600px-BoerWomen.jpg",
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

# IMATGES T05 — Entreguerres i feixismes
imatges_t05 = {
    "wall_street_crash.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Crowd_outside_nyse.jpg/800px-Crowd_outside_nyse.jpg",
    "great_depression_usa.jpg":  "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Lange-MigrantMother02.jpg/532px-Lange-MigrantMother02.jpg",
    "mussolini_march_rome.jpg":  "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/March_on_Rome_1922.jpg/800px-March_on_Rome_1922.jpg",
    "hitler_reichstag.jpg":      "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Bundesarchiv_Bild_102-14597%2C_Hitler-Putsch%2C_M%C3%BCnchen%2C_Feldherrnhalle.jpg/800px-Bundesarchiv_Bild_102-14597%2C_Hitler-Putsch%2C_M%C3%BCnchen%2C_Feldherrnhalle.jpg",
    "kristallnacht.jpg":         "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Kristallnacht.jpg/800px-Kristallnacht.jpg",
    "new_deal_poster.jpg":       "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/New_deal_poster.jpg/573px-New_deal_poster.jpg",
    "nazi_rally_nuremberg.jpg":  "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Bundesarchiv_Bild_183-1987-0922-500%2C_N%C3%BCrnberg%2C_Reichsparteitag%2C_Aufmarsch_SS_und_SA.jpg/800px-Bundesarchiv_Bild_183-1987-0922-500%2C_N%C3%BCrnberg%2C_Reichsparteitag%2C_Aufmarsch_SS_und_SA.jpg",
    "spanish_republic.jpg":      "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Proclamaci%C3%B3n_de_la_II_Rep%C3%BAblica_Espa%C3%B1ola.jpg/800px-Proclamaci%C3%B3n_de_la_II_Rep%C3%BAblica_Espa%C3%B1ola.jpg",
}
imatges.update(imatges_t05)

# IMATGES T06 — Segona Guerra Mundial
imatges_t06 = {
    "munich_1938.jpg":           "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Bundesarchiv_Bild_183-R69173%2C_M%C3%BCnchener_Abkommen%2C_Staatschefs.jpg/800px-Bundesarchiv_Bild_183-R69173%2C_M%C3%BCnchener_Abkommen%2C_Staatschefs.jpg",
    "wwii_europe_map.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Second_world_war_europe_1941_map_de.png/800px-Second_world_war_europe_1941_map_de.png",
    "battle_of_britain.jpg":      "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Royal_Air_Force_Fighter_Command%2C_1939-1945._CH2390.jpg/800px-Royal_Air_Force_Fighter_Command%2C_1939-1945._CH2390.jpg",
    "stalingrad.jpg":             "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Bundesarchiv_Bild_183-W0506-316%2C_Russland%2C_Kampf_um_Stalingrad%2C_Siegesflagge.jpg/546px-Bundesarchiv_Bild_183-W0506-316%2C_Russland%2C_Kampf_um_Stalingrad%2C_Siegesflagge.jpg",
    "dday_normandy.jpg":          "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Into_the_Jaws_of_Death_23-0455M_edit.jpg/800px-Into_the_Jaws_of_Death_23-0455M_edit.jpg",
    "holocaust_auschwitz.jpg":    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Birkenau_gate.JPG/800px-Birkenau_gate.JPG",
    "holocaust_liberation.jpg":   "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Buchenwald_Survivors_19450416.jpg/800px-Buchenwald_Survivors_19450416.jpg",
    "nuremberg_trials.jpg":       "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Nuremberg_Trials_retouched.jpg/800px-Nuremberg_Trials_retouched.jpg",
    "hiroshima.jpg":              "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Atomic_bombing_of_Japan.jpg/800px-Atomic_bombing_of_Japan.jpg",
}
imatges.update(imatges_t06)

# IMATGES T07 — Guerra Civil i Franquisme
imatges_t07 = {
    "guernica_bombardeig.jpg":   "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Guernica_bombing_1937.jpg/800px-Guernica_bombing_1937.jpg",
    "brigades_internacionals.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/International_Brigades_poster.jpg/529px-International_Brigades_poster.jpg",
    "refugiats_republicans.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Spanish_refugees_crossing_into_France.jpg/800px-Spanish_refugees_crossing_into_France.jpg",
    "franco_victoria.jpg":       "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Franco_en_el_desfile_de_la_victoria_1939.jpg/800px-Franco_en_el_desfile_de_la_victoria_1939.jpg",
    "valle_caidos.jpg":          "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Valle_de_los_Ca%C3%ADdos_-_2007_05_02.jpg/800px-Valle_de_los_Ca%C3%ADdos_-_2007_05_02.jpg",
    "transicio_eleccions.jpg":   "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Elecciones_generales_de_1977_%28cartel%29.jpg/473px-Elecciones_generales_de_1977_%28cartel%29.jpg",
    "23f_congres.jpg":           "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/23F.jpg/800px-23F.jpg",
    "fosses_comunes.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Exhumacion_de_victimas_del_franquismo.jpg/800px-Exhumacion_de_victimas_del_franquismo.jpg",
}
imatges.update(imatges_t07)

# IMATGES T08 — Guerra Freda i món actual
imatges_t08 = {
    "berlin_wall.jpg":          "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Berlinermauer.jpg/800px-Berlinermauer.jpg",
    "berlin_wall_fall.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Fall_of_the_Berlin_Wall_1989.jpg/800px-Fall_of_the_Berlin_Wall_1989.jpg",
    "cuba_missiles.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Cuban_Missile_Crisis_-_Kennedy_Signs_Cuba_Quarantine.jpg/800px-Cuban_Missile_Crisis_-_Kennedy_Signs_Cuba_Quarantine.jpg",
    "vietnam_war.jpg":          "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Nick_Ut%2C_the_Terror_of_War%2C_1972.jpg/800px-Nick_Ut%2C_the_Terror_of_War%2C_1972.jpg",
    "prague_spring.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Prague_Spring_1968.jpg/800px-Prague_Spring_1968.jpg",
    "thatcher_reagan.jpg":      "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Reagan_Thatcher_1984.jpg/800px-Reagan_Thatcher_1984.jpg",
    "gorbatxov.jpg":            "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Mikhail_Gorbachev_1987.jpg/600px-Mikhail_Gorbachev_1987.jpg",
}
imatges.update(imatges_t08)

# Imatges addicionals de revisió
imatges_revisio = {
    "enclosures.jpg":           "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Open_field_system.jpg/800px-Open_field_system.jpg",
    "slums_england.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Gustave_dore_london_over_london_by_rail.jpg/793px-Gustave_dore_london_over_london_by_rail.jpg",
    "lenin_1917.jpg":           "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Lenin_1920-03-30_2.jpg/486px-Lenin_1920-03-30_2.jpg",
    "bandung_conference.jpg":   "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Bandung_conference_1955.jpg/800px-Bandung_conference_1955.jpg",
    "gandhi_salt_march.jpg":    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Salt_March.jpg/800px-Salt_March.jpg",
}
imatges.update(imatges_revisio)
