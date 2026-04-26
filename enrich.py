import pandas as pd

# read csv file
df = pd.read_csv("data.csv")

linkedin_links = []
industry_list = []
status_list = []

for company in df["Company Name"]:

    # linkedin search url
    link = "https://www.linkedin.com/search/results/companies/?keywords=" + company.replace(" ", "%20")
    linkedin_links.append(link)

    # industry
    industry_list.append("Advanced Materials / Composites")

    # status
    status_list.append("Ready for Outreach")

# add new columns
df["LinkedIn Search"] = linkedin_links
df["Industry"] = industry_list
df["Status"] = status_list

# save new file
df.to_csv("enriched.csv", index=False)

print("Enriched file created successfully")
print(df.head())