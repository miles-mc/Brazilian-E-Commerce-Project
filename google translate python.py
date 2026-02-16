from googletrans import Translator
import pandas as pd
from deep_translator import GoogleTranslator
from tqdm import tqdm
import time
import re

file_path = 'TEXTONLYcleanedreviews.csv'
df = pd.read_csv(file_path)

#translator
translator = GoogleTranslator(source='pt', target='en')


def batch_translate(series):
   
    texts = series.fillna("").astype(str).tolist()

    batch_size = 500 #can change value between 100-500 depending on system, 500 was stable for me
    results = []

    for i in tqdm(range(0, len(texts), batch_size), desc="Batch translating"):
        batch = texts[i:i + batch_size]

        try:
            translated_batch = translator.translate_batch(batch)
        except Exception:   
            translated_batch = ["Error"] * len(batch)


        results.extend(translated_batch)

    return results

df['message_english'] = batch_translate(df['review_comment_message'])
df['title_english'] = batch_translate(df['review_comment_title'])

output_filename = 'olist_reviews_translated_batch.csv'
df.to_csv(output_filename, index=False)
