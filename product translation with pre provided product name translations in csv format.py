import pandas as pd
 
main_csv = "olist_products_dataset.csv"
lookup_csv = "product_category_name_translation.csv"
 
replace_this = "product_category_name"  
key = "product_category_name"
value = "product_category_name_english"
 
output = "olist_products_dataset_translated.csv"
 
 
dftoreplace = pd.read_csv(main_csv)
dftolookup = pd.read_csv(lookup_csv)
 
mapping = dict(zip(dftolookup[key], dftolookup[value]))
 
dftoreplace[replace_this] = dftoreplace[replace_this].map(mapping).fillna(dftoreplace[replace_this])
 
dftoreplace.to_csv(output, index=False)
