import pandas as pd

df = pd.read_csv("enriched.csv")

lines = []

for company in df["Company Name"]:

    if "Hexcel" in company:
        line = "Noticed Hexcel's focus on lightweight composite materials, curious how you are helping aerospace manufacturers reduce weight without compromising strength."

    elif "Toray" in company:
        line = "Saw Toray Advanced Composites at CAMX, interested in how you are positioning thermoplastic solutions for next generation manufacturing."

    elif "Huntsman" in company:
        line = "Noticed Huntsman's innovation in advanced materials, curious how you are supporting manufacturers looking for faster and durable production systems."

    elif "Owens" in company:
        line = "Saw Owens Corning's continued push in composites, interested in how you are helping industrial teams improve durability and efficiency."

    elif "Airtech" in company:
        line = "Noticed Airtech's presence at CAMX, curious how you are enabling manufacturers with tooling and process materials for scalable production."

    elif "SABIC" in company:
        line = "Saw SABIC exhibiting at CAMX, interested in how you are helping manufacturers adopt high performance material solutions."

    elif "Strongwell" in company:
        line = "Noticed Strongwell's expertise in pultruded composites, curious how you are supporting customers seeking long lasting structural solutions."

    elif "Composites One" in company:
        line = "Saw Composites One at CAMX, interested in how you are helping customers source materials and streamline production."

    elif "Arkema" in company:
        line = "Noticed Arkema's material innovation focus, curious how you are supporting next generation composite applications."

    elif "Teijin" in company:
        line = "Saw Teijin exhibiting at CAMX, interested in how you are helping manufacturers with lightweight and sustainable material solutions."

    else:
        line = f"Noticed {company} exhibiting at CAMX 2025, curious how you are exploring partnerships with manufacturers focused on advanced composite solutions."

    lines.append(line)

df["Personalized First Line"] = lines

df.to_csv("final_output.csv", index=False, encoding="utf-8-sig")

print("Updated final file created successfully")
print(df.head())