import pandas as pd

df = pd.read_csv('./data/funnel.csv')

res_df = df[['client_id']]

res_df['target'] = 0.5

res_df.to_csv('submission.csv', index=False)